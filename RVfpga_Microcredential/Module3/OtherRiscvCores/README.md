# Other RISC-V Cores

In recent years, the open-source hardware ecosystem has witnessed a remarkable surge in the development and adoption of RISC-V cores. Thanks to its open and modular instruction set architecture, RISC-V has empowered academia, industry, and hobbyists to design and share a wide variety of cores tailored to different needs—from ultra-minimal implementations for microcontrollers to complex out-of-order processors for high-performance computing. In this page we explore a selection of these open RISC-V cores, highlighting their features, use cases, and the vibrant community driving this innovation.

## Introduction
Look at the following presentation: [OtherRiscvCores](https://drive.google.com/file/d/1N_pWZ8oRKA0aUdZg2EKY66rlhnqzTMtF/view?usp=sharing).


## Verilator CVW-Wally simulation
Follow these steps to replicate the Verilator CVW-Wally simulation in the VM:
 * Install version 5.032 of Verilator. (You can also download a pre-compiled version here: [Verilator](https://ucomplutense-my.sharepoint.com/:u:/g/personal/dani02_ucm_es/EQpVNYBVJU1Loxn6iQGpHOABhR8v2-vyy88wdoDhW6lK6w?e=EnotZD). Once downloaded, unzip and move it to the home of the VM.)
 * Install version 14.2.0 of the RISC-V toolchain. (You can also download a pre-compiled version here: [Toolchain](https://ucomplutense-my.sharepoint.com/:u:/g/personal/dani02_ucm_es/EWcHZ40cZQtNtRncy7UWnIgBIi7chrEkSuS_IhD6Z4KkVw?e=Sgd3jE). Once downloaded, unzip and move it to the home of the VM.)
 * Clone recursively the sources from the [CVW Wally repo](https://github.com/openhwgroup/cvw). (You can also download a prepared version of Wally here: [Wally](https://ucomplutense-my.sharepoint.com/:u:/g/personal/dani02_ucm_es/EYY6Vou-SONEj9FqHHnBZ44BT5nQaA02E27KNKz-nXCeKg?e=5lOg5A). Once downloaded, unzip and move it to the home of the VM.)
 * Arrange the paths properly. We next show how to set the paths in case you download the pre-compiled tools mentioned above:

    ```
    export VERILATOR_ROOT=/home/rvfpga/verilator_5-032/
    export PATH=$VERILATOR_ROOT/bin:$PATH
    export INCLUDE_PATH=$VERILATOR_ROOT/include
    export RISCV=/home/rvfpga/RiscvToolchain/
    export PATH=$RISCV/bin:$PATH
    export WALLY=/home/rvfpga/Wally/cvw/
    export PATH=$WALLY/bin:$PATH
    ```

 * In the Makefile used for Verilator (```~/cvw/sim/verilator/Makefile```), add the option to generate a trace (```PARAMS?=--trace```).
 * We next show an example execution of this [ExampleExtended](https://drive.google.com/file/d/1Uw06q4ee5MpxFQbyur60pgeGmBbOzFaC/view?usp=sharing). This is the program obtained using the ```riscv64-unknown-elf-objdump``` aplication.

   ```
   00000000000100b0 <rvtest_entry_point>:
      100b0:	02a00513          	li	a0,42
      100b4:	00000393          	li	t2,0
      100b8:	24000813          	li	a6,576
   
   00000000000100bc <REPEAT>:
      100bc:	00138393          	addi	t2,t2,1
      100c0:	ff039ee3          	bne	t2,a6,100bc <REPEAT>
   
   00000000000100c4 <self_loop>:
      100c4:	0000006f          	j	100c4 <self_loop>
   ```


 * This is an example of commands to compile and simulate the example program, and to then visualize the trace:

    ```
    cd ~/Wally/cvw/examples/asm/example_extended
    riscv64-unknown-elf-gcc -march=rv64im -mabi=lp64 -nostdlib -o example_extended example_extended.S
    riscv64-unknown-elf-objdump -d example_extended > example_extended.objdump
    wsim --vcd --sim verilator rv64gc --elf example_extended
    gtkwave ~/Wally/cvw/sim/verilator/testbench.vcd
    ```

 * You can use this [tcl file](https://ucomplutense-my.sharepoint.com/:u:/g/personal/dani02_ucm_es/ES3IKkkHj5JIsaDzGuW2dnoBrl2g4S7_kOiw1v7Rcy93dw?e=je4Sdb) to add signals to the gtkwave. For example, this is an example of the trace showing the clock, the 32-bit instruction, and the ALU result:

      ![image](https://github.com/user-attachments/assets/351390d6-9564-4a3f-b3bc-4b020080caac)


 * In the figure, you can see the instructions within the first and second iteration of the loop and the value obtained in the ALU for the addition.


## CVW-Wally on the Nexys A7 board

Follow these steps to execute CVW-Wally on the Nexys A7 board.

### Required hardware

For this activity, the instructor will provide the Nexys A7 board. Each student must provide the remaining accessories needed to prepare and run the experiment.

Required items:

| Item | Required? | Notes |
|---|---:|---|
| Nexys A7 board | Provided by the instructor | Used to run CVW-Wally on FPGA |
| microSD card | Yes | 32 GB or larger recommended |
| microSD card reader | Yes | Needed to flash the SD image from the Linux computer |
| microUSB cable | Yes | Needed to power the board and access the UART interface |
| FPGA programmer / JTAG adapter | Yes | Use the exact model specified by the instructor |

Recommended microSD cards tested successfully:

| microSD model | Capacity | Status |
|---|---:|---|
| SanDisk Ultra | 32 GB | Tested successfully |
| Kingston Canvas Select Plus | 32 GB | Tested successfully |

> [!IMPORTANT]
> The microSD card will be completely erased when flashing the Wally SD image. Do not use a card containing important data.

> [!WARNING]
> Do not buy a random FPGA programmer or JTAG adapter. Use only the model specified by the instructor, since different programmers may require different OpenOCD configuration files.

### Repository and environment setup

Clone the repository:

```bash
cd ~
git clone https://github.com/mmiral04/cvw.git
cd cvw
git checkout apb_periph
```

Configure the Wally environment:

```bash
mkdir -p ~/riscv
ln -s /home/rvfpga/.platformio/packages/toolchain-riscv/* ~/riscv/
touch ~/riscv/site-setup.sh
source setup.sh
```

### Download the prebuilt files

Download the prebuilt files from the following GitHub release:

https://github.com/artecs-group/RVfpga-sim-addons/releases/tag/v1.0-wally-nexysa7

The release contains:

* A prebuilt Linux microSD image for the Nexys A7 board: `WallyNexysA7_SD.img.xz`
* A prebuilt FPGA bitstream for the CVW-Wally system: `fpgaTop.bit`

Move both files to the `Downloads` folder of the VM.

### Prepare the microSD card

Insert the microSD card into your Linux computer and identify the corresponding device:

```bash
lsblk
```

Example output:

```text
sda      8:0    1  29.7G  0 disk
└─sda1   8:1    1  29.7G  0 part
```

In this example, the microSD card is `/dev/sda`.

Unmount any automatically mounted partitions:

```bash
sudo umount /dev/sdX1 2>/dev/null
sudo umount /dev/sdX2 2>/dev/null
sudo umount /dev/sdX3 2>/dev/null
sudo umount /dev/sdX4 2>/dev/null
```

Replace `sdX` with the actual device name of your microSD card.

Flash the SD image:

```bash
xzcat ~/Downloads/WallyNexysA7_SD.img.xz | sudo dd of=/dev/sdX bs=4M status=progress conv=fsync
sync
```

Replace `/dev/sdX` with the correct device corresponding to your microSD card.

> [!WARNING]
> Double-check the target device before executing the `dd` command. Selecting the wrong device may overwrite your computer disk.

> [!IMPORTANT]
> Use the device name, for example `/dev/sdX`, not a partition such as `/dev/sdX1`.

When the command finishes, safely remove the microSD card and insert it into the Nexys A7 board.

### Connect the hardware

Connect the following elements:

* Nexys A7 board
* microUSB cable
* prepared microSD card
* FPGA programmer / JTAG adapter specified by the instructor

### Program the FPGA

Use the following command:

```bash
~/.platformio/packages/tool-openocd-riscv-chipsalliance/bin/openocd -c "set BITFILE Downloads/fpgaTop.bit" -f ~/RVfpga_MasterUCLM/src/OtherSources/ConfigFiles/swervolf_nexys_program.cfg
```

Wait until programming finishes successfully.

### Open the UART terminal

Open the UART terminal. You may need to change `ttyUSB1` to another value, such as `ttyUSB0`.

```bash
sudo apt install screen
screen /dev/ttyUSB1 115200
```

Press the **RESET** button on the Nexys A7 board.

If everything works correctly you should see:

* BootROM messages
* OpenSBI messages
* Linux boot logs
* A login prompt

Login as:

```text
root
```

After login you should obtain a BusyBox shell prompt:

```text
#
```

### Test the GPIO output LEDs

The LEDs LD0-LD4 are connected to GPIO output bits 0 to 4.

Configure GPIO outputs:

```bash
devmem 0x10060008 32 0x1F
```

Turn LEDs on:

```bash
devmem 0x1006000C 32 0x1F
```

Turn LEDs off:

```bash
devmem 0x1006000C 32 0x00
```

### Test the GPIO input buttons

The on-board buttons are connected to the GPIO input pins:

| Button | GPIO input bit |
|---|---:|
| BTNC | 0 |
| BTNU | 1 |
| BTNL | 2 |
| BTNR | 3 |

First, enable GPIO inputs for bits 0 to 3:

```bash
devmem 0x10060004 32 0x0F
```

Then read the GPIO input register:

```bash
devmem 0x10060000 32
```

Press one of the buttons and repeat the read command. The value should change according to the button being pressed.

Expected values:

| Pressed button | Expected value |
|---|---:|
| none | `0x00000000` |
| BTNC | `0x00000001` |
| BTNU | `0x00000002` |
| BTNL | `0x00000004` |
| BTNR | `0x00000008` |

> [!NOTE]
> The Nexys A7 switches are not connected to the GPIO input in this bitstream. The available GPIO inputs are the four push buttons listed above.

### Test the seven-segment display peripheral

Write a segment pattern:

```bash
devmem 0x00100000 32 0x77
```

Expected result:

* The display should show the character `A`.

### Example: using buttons, LEDs, and the seven-segment display together

In this example, the push buttons are used as GPIO inputs. Depending on the button being pressed, the program turns on one LED and shows one hexadecimal digit on the seven-segment display.

Create the following script inside the Wally Linux shell:

```bash
cat > button_demo.sh <<'EOF'
#!/bin/sh

# Enable GPIO inputs BTNC-BTNR
devmem 0x10060004 32 0x0F

# Enable GPIO outputs LD0-LD4
devmem 0x10060008 32 0x1F

while true
do
    value=$(devmem 0x10060000 32)

    case "$value" in
        0x00000001|0x1)
            # BTNC pressed: LED0 on, display shows 1
            devmem 0x1006000C 32 0x01
            devmem 0x00100000 32 0x06
            ;;
        0x00000002|0x2)
            # BTNU pressed: LED1 on, display shows 2
            devmem 0x1006000C 32 0x02
            devmem 0x00100000 32 0x5B
            ;;
        0x00000004|0x4)
            # BTNL pressed: LED2 on, display shows 3
            devmem 0x1006000C 32 0x04
            devmem 0x00100000 32 0x4F
            ;;
        0x00000008|0x8)
            # BTNR pressed: LED3 on, display shows 4
            devmem 0x1006000C 32 0x08
            devmem 0x00100000 32 0x66
            ;;
        *)
            # No button pressed, or more than one button pressed
            devmem 0x1006000C 32 0x00
            devmem 0x00100000 32 0x00
            ;;
    esac

    sleep 1
done
EOF
```

Make the script executable:

```bash
chmod +x button_demo.sh
```

Run it:

```bash
./button_demo.sh
```

Expected behavior:

| Action | LEDs | Seven-segment display |
|---|---|---|
| No button pressed | off | off |
| Press BTNC | LD0 on | `1` |
| Press BTNU | LD1 on | `2` |
| Press BTNL | LD2 on | `3` |
| Press BTNR | LD3 on | `4` |

Stop the program with:

```text
Ctrl+C
```

### Exercise

Modify the previous script so that it implements the following behavior:

| Button | Required LED output | Required display output |
|---|---|---|
| BTNC | LD0 and LD4 on | `A` |
| BTNU | LD1 and LD3 on | `b` |
| BTNL | LD2 on | `C` |
| BTNR | all LEDs on | `F` |

Useful seven-segment codes:

| Character | Code |
|---|---:|
| `A` | `0x77` |
| `b` | `0x7C` |
| `C` | `0x39` |
| `F` | `0x71` |

Useful LED values:

| LEDs | Value |
|---|---:|
| LD0 | `0x01` |
| LD1 | `0x02` |
| LD2 | `0x04` |
| LD3 | `0x08` |
| LD4 | `0x10` |
| LD0 + LD4 | `0x11` |
| LD1 + LD3 | `0x0A` |
| LD0 + LD1 + LD2 + LD3 + LD4 | `0x1F` |

Submit:

* the modified script
* a short explanation of:
  * which GPIO register is used to read the buttons
  * which GPIO register is used to control the LEDs
  * which address is used to control the seven-segment display

### Exit the UART terminal

To exit `screen`:

```text
Ctrl+A
K
```

---

### Additional reference

Mario Miralles provides a detailed guide about the implementation of the seven-segment display peripheral for CVW-Wally, including APB integration, Linux support, devicetree modifications, and driver development:

https://github.com/mmiral04/cvw_apb_peripheral
