# Other RISC-V Cores

In recent years, the open-source hardware ecosystem has witnessed a remarkable surge in the development and adoption of RISC-V cores. Thanks to its open and modular instruction set architecture, RISC-V has empowered academia, industry, and hobbyists to design and share a wide variety of cores tailored to different needs—from ultra-minimal implementations for microcontrollers to complex out-of-order processors for high-performance computing. In this page we explore a selection of these open RISC-V cores, highlighting their features, use cases, and the vibrant community driving this innovation.

1. Look at the following presentation: [OtherRiscvCores](https://drive.google.com/file/d/1N_pWZ8oRKA0aUdZg2EKY66rlhnqzTMtF/view?usp=sharing).
2. Look at the following video showing the execution of CVW Wally in Verilator: ... Take this into account:
    * Arrange the paths conveniently
    * You must use specific versions of Verilator (5.032) and RISC-V toolchain (14.2.0).
    * In the Makefile used for Verilator (~/cvw/sim/verilator/Makefile), add the option to generate a trace (PARAMS?=--trace)
    * This is an example of commands to compile and simulate an example program, and to visualize the trace:

          cd ~/cvw/examples/example_extended (you can download the program here: [ExampleExtended]())
          riscv64-unknown-elf-gcc -march=rv64im -mabi=lp64 -nostdlib -o example_extended example_extended.S
          riscv64-unknown-elf-objdump -d example_extended > example_extended.objdump
          wsim --vcd --sim verilator rv64gc --elf example_extended
          gtkwave ~/cvw/sim/verilator/testbench.vcd

    * This is an example of the trace generated at ~/cvw/sim/verilator/testbench.vcd:

    

3. Look at the following video showing the execution of CVW Wally in FPGA: ...
4. Look at the following video showing the execution of CVA6 in Verilator: ...
5. Look at the following video showing the execution of CVA6 in Verilator: ...
