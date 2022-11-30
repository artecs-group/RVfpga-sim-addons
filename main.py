# Copyright 2014-present PlatformIO <contact@platformio.org>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import time
import subprocess
import sys
import os

from SCons.Script import (
    ARGUMENTS,
    COMMAND_LINE_TARGETS,
    AlwaysBuild,
    Builder,
    Default,
    DefaultEnvironment,
    WhereIs,
)


def generate_vh(target, source, env):
    binary_file = source[0].get_path()
    assert binary_file.endswith(".bin")
    vh_file = binary_file.replace(".bin", ".vh")
    result = ""
    with open(binary_file, "rb") as fp:
        cnt = 7
        s = ["00"] * 8
        while True:
            data = fp.read(1)
            if not data:
                result = result + "".join(s) + "\n"
                break
            s[cnt] = "{:02X}".format(data[0])
            if cnt == 0:
                result = result + "".join(s) + "\n"
                s = ["00"] * 8
                cnt = 8
            cnt -= 1

    with open(vh_file, "wb") as fp:
        fp.write(bytes(result, "ascii"))


def generate_disassembly(target, source, env):
    elf_file = target[0].get_path()
    assert elf_file.endswith(".elf")
    env.Execute(
        " ".join(
            [
                env.subst("$CC").replace("-gcc", "-objdump"),
                "-d",
                '"%s"' % elf_file,
                ">",
                '"%s"' % elf_file.replace(".elf", ".dis"),
            ]
        )
    )


def run_verilator(target, source, env):
    trace_file = os.path.join(env.subst("$BUILD_DIR"), "trace.vcd")
    if os.path.isfile(trace_file):
        os.remove(trace_file)

    cmd = [
        os.path.join(
            platform.get_package_dir("tool-verilator-swervolf") or "",
            env.BoardConfig().get("debug.verilator.binary", "Vswervolf_core_tb")
        ),
        "+ram_init_file=" + os.path.basename(source[0].get_path()),
        "+vcd=1",
    ]

    p = subprocess.Popen(cmd, cwd=env.subst("$BUILD_DIR"))

    # Wait for some time while data is being collected
    time.sleep(3)
    p.terminate()



def run_RVfpgaViDBoPipeline(target, source, env):
    cmd = [
        env.BoardConfig().get("debug.verilator.binary"),
        "+ram_init_file=" + os.path.basename(source[0].get_path())
    ]

    p = subprocess.run(cmd, cwd=env.subst("$BUILD_DIR"))




env = DefaultEnvironment()
platform = env.PioPlatform()
board_config = env.BoardConfig()

env.Replace(
    AR="riscv64-unknown-elf-gcc-ar",
    AS="riscv64-unknown-elf-as",
    CC="riscv64-unknown-elf-gcc",
    GDB="riscv64-unknown-elf-gdb",
    CXX="riscv64-unknown-elf-g++",
    OBJCOPY="riscv64-unknown-elf-objcopy",
    RANLIB="riscv64-unknown-elf-gcc-ranlib",
    SIZETOOL="riscv64-unknown-elf-size",
    ARFLAGS=["rc"],
    SIZEPRINTCMD="$SIZETOOL -d $SOURCES",
    PROGSUFFIX=".elf",
)

# Allow user to override via pre:script
if env.get("PROGNAME", "program") == "program":
    env.Replace(PROGNAME="firmware")

env.Append(
    BUILDERS=dict(
        ElfToHex=Builder(
            action=env.VerboseAction(
                " ".join(["$OBJCOPY", "-O", "ihex", "$SOURCES", "$TARGET"]),
                "Building $TARGET",
            ),
            suffix=".hex",
        ),
        ElfToBin=Builder(
            action=env.VerboseAction(
                " ".join(["$OBJCOPY", "-O", "binary", "$SOURCES", "$TARGET"]),
                "Building $TARGET",
            ),
            suffix=".bin",
        ),
        BinToVh=Builder(
            action=env.VerboseAction(generate_vh, "Building $TARGET"), suffix=".vh"
        ),
    )
)

if not env.get("PIOFRAMEWORK"):
    env.SConscript("frameworks/_bare.py", exports="env")

#
# Target: Build executable and linkable firmware
#

target_elf = None
if "nobuild" in COMMAND_LINE_TARGETS:
    target_elf = os.path.join("$BUILD_DIR", "${PROGNAME}.elf")
    target_bin = os.path.join("$BUILD_DIR", "${PROGNAME}.bin")
    target_vh = os.path.join("$BUILD_DIR", "${PROGNAME}.vh")
else:
    target_elf = env.BuildProgram()
    target_bin = env.ElfToBin(os.path.join("$BUILD_DIR", "${PROGNAME}"), target_elf)
    target_vh = env.BinToVh(os.path.join("$BUILD_DIR", "${PROGNAME}"), target_bin)
    env.Depends(target_bin, "checkprogsize")

AlwaysBuild(env.Alias("nobuild", target_bin))
target_buildprog = env.Alias("buildprog", target_bin, target_bin)

env.AddPostAction(
    target_elf, env.VerboseAction(generate_disassembly, "Generating disassembly")
)

#
# Target: Print binary size
#

target_size = env.AddPlatformTarget(
    "size",
    target_elf,
    env.VerboseAction("$SIZEPRINTCMD", "Calculating size $SOURCE"),
    "Program Size",
    "Calculate program size",
)

#
# Target: Program FPGA
#

# Note: there is a precompiled bitstream in framework-wd-riscv-sdk package
bitstream_file = os.path.abspath(
    board_config.get("build.bitstream_file", "swervolf_0.bit"))

if not os.path.isfile(bitstream_file):
    bitstream_file = os.path.join(platform.get_dir(), "misc", "bitstream", "rvfpga.bit")

if "program_fpga" in COMMAND_LINE_TARGETS and not os.path.isfile(bitstream_file):
    sys.stderr.write("Error: Couldn't find bitstream file.\n")
    env.Exit(1)

env.AddPlatformTarget(
    "program_fpga",
    bitstream_file,
    env.VerboseAction(
        " ".join(
            [
                '"%s"'
                % os.path.join(
                    platform.get_package_dir("tool-openocd-riscv-chipsalliance") or "",
                    "bin",
                    "openocd",
                ),
                "-s",
                '"%s"'
                % os.path.join(
                    platform.get_package_dir("framework-wd-riscv-sdk") or "",
                    "board",
                    board_config.get("build.variant", ""),
                ),
                "-s",
                '"%s"'
                % os.path.join(
                    platform.get_package_dir("tool-openocd-riscv-chipsalliance") or "",
                    "share",
                    "openocd",
                    "scripts",
                ),
                "-c",
                '"set BITFILE {$SOURCE}"',
                "-f",
                "%s_program.cfg" % env.subst("$BOARD")
            ]
        ),
        "Programming bitstream $SOURCE",
    ),
    "Upload Bitstream",
)

#
# Target: Generate trace for GTKWave using Verilator
#

env.AddPlatformTarget("generate_trace", target_vh, env.VerboseAction(
    run_verilator, "Generating trace from Verilator"), "Generate Trace")


#
# Target: Run RVfpga-ViDBo/PipelineSimulator
#

env.AddPlatformTarget("ViDBo", target_vh, env.VerboseAction(
    run_RVfpgaViDBoPipeline, "Running Program in RVfpga-ViDBo or RVfpga-PipelineSimulator"), "RVfpga-ViDBo")



#
# Target: Run Verilator simulator to connect OpenOCD
#

env.AddPlatformTarget(
    "start_verilator",
    None,
    env.VerboseAction(
        " ".join(
            [
                '"%s"'
                % os.path.join(
                    platform.get_package_dir("tool-verilator-swervolf") or "",
                    board_config.get("debug.verilator.binary", "Vswervolf_core_tb"),
                ),
                "+jtag_vpi_enable=1",
            ]
        ),
        "Running Verilator",
    ),
    "Start Verilator",
)


#
# Target: Generate bitstream
#

vivado_path = ""
vivado_tcl_script = ""
vivado_design_project = ""
if "generate_bitstream" in COMMAND_LINE_TARGETS:
    vivado_path = WhereIs("vivado")
    if not vivado_path:
        sys.stderr.write("Error: Couldn't find Vivado tools!\n")
        env.Exit(1)

    vivado_tcl_script = os.path.abspath(
        board_config.get("build.swervolf_run_tc", "swervolf_0.6_run.tcl")
    )

    vivado_design_project = os.path.abspath(
        board_config.get("build.swervolf_xpr", "swervolf_0.6.xpr")
    )

    for f in (vivado_tcl_script, vivado_design_project):
        if not os.path.isfile(f):
            sys.stderr.write("Error: Couldn't find  file %s\n" % f)
            env.Exit(1)

env.AddPlatformTarget(
    "generate_bitstream", None, env.VerboseAction(
        " ".join(
            [
                vivado_path,
                "-notrace",
                "-mode",
                "batch",
                "-source",
                vivado_tcl_script,
                vivado_design_project,
            ]
        ),
        "Generating bitstream from $SOURCES",
    ), "Generate Bitstream"
)

#
# Target: Upload by default .bin file
#

upload_protocol = env.subst("$UPLOAD_PROTOCOL")
debug_tools = board_config.get("debug.tools", {})
upload_actions = []
upload_target = target_elf

if upload_protocol in debug_tools:
    openocd_args = [
        "-c",
        "debug_level %d" % (2 if int(ARGUMENTS.get("PIOVERBOSE", 0)) else 1),
        "-s",
        platform.get_package_dir("tool-openocd-riscv-chipsalliance") or "",
    ]
    openocd_args.extend(
        debug_tools.get(upload_protocol).get("server").get("arguments", [])
    )
    openocd_args.extend(
        [
            "-c", "reset halt",
            "-c", "load_image {$SOURCE} %s elf" % board_config.get(
                "upload").get("image_offset", "0x0"),
            "-c", "resume %s" % board_config.get("upload").get("image_offset", "0x0"),
            "-c", "shutdown"
        ]
    )
    env.Replace(
        UPLOADER="openocd",
        UPLOADERFLAGS=openocd_args,
        UPLOADCMD="$UPLOADER $UPLOADERFLAGS",
    )
    upload_actions = [env.VerboseAction("$UPLOADCMD", "Uploading $SOURCE")]

# custom upload tool
elif upload_protocol == "custom":
    upload_actions = [env.VerboseAction("$UPLOADCMD", "Uploading $SOURCE")]

else:
    sys.stderr.write("Warning! Unknown upload protocol %s\n" % upload_protocol)

env.AddPlatformTarget("upload", upload_target, upload_actions, "Upload")


#
# Setup default targets
#

Default([target_buildprog, target_size])
