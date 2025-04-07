# Other RISC-V Cores

In recent years, the open-source hardware ecosystem has witnessed a remarkable surge in the development and adoption of RISC-V cores. Thanks to its open and modular instruction set architecture, RISC-V has empowered academia, industry, and hobbyists to design and share a wide variety of cores tailored to different needs—from ultra-minimal implementations for microcontrollers to complex out-of-order processors for high-performance computing. In this page we explore a selection of these open RISC-V cores, highlighting their features, use cases, and the vibrant community driving this innovation.

1. Look at the following presentation: [OtherRiscvCores](https://drive.google.com/file/d/1N_pWZ8oRKA0aUdZg2EKY66rlhnqzTMtF/view?usp=sharing).
2. Look at the following video showing the execution of CVW Wally in Verilator: ...
3. Follow these steps to replicate the simulation in the VM:
    * You must use specific versions of Verilator (5.032) and RISC-V toolchain (14.2.0). You can download them here: [Verilator](https://ucomplutense-my.sharepoint.com/:u:/g/personal/dani02_ucm_es/EQpVNYBVJU1Loxn6iQGpHOABhR8v2-vyy88wdoDhW6lK6w?e=EnotZD) and [Toolchain](https://ucomplutense-my.sharepoint.com/:u:/g/personal/dani02_ucm_es/EQpVNYBVJU1Loxn6iQGpHOABhR8v2-vyy88wdoDhW6lK6w?e=EnotZD), and move them to the home of the VM.
    * Clone recursively the sources from the [CVW Wally repo](https://github.com/openhwgroup/cvw). You can also download it here: [Wally](https://ucomplutense-my.sharepoint.com/:u:/g/personal/dani02_ucm_es/EYY6Vou-SONEj9FqHHnBZ44BT5nQaA02E27KNKz-nXCeKg?e=5lOg5A), and move it to the home of the VM.
    * Arrange the paths properly:

       ```
       export VERILATOR_ROOT=/home/rvfpga/verilator_5-032/
       export PATH=$VERILATOR_ROOT/bin:$PATH
       export INCLUDE_PATH=$VERILATOR_ROOT/include
       export RISCV=/home/rvfpga/RiscvToolchain/
       export PATH=$RISCV/bin:$PATH
       export WALLY=/home/rvfpga/Wally/cvw/
       export PATH=$WALLY/bin:$PATH
       ```

    * In the Makefile used for Verilator (~/cvw/sim/verilator/Makefile), add the option to generate a trace (PARAMS?=--trace)
    * This is an example of commands to compile and simulate an example program (you can download the program here: [ExampleExtended](https://drive.google.com/file/d/1Uw06q4ee5MpxFQbyur60pgeGmBbOzFaC/view?usp=sharing)), and to visualize the trace:

          ```
          cd ~/Wally/cvw/examples/asm/example_extended
          riscv64-unknown-elf-gcc -march=rv64im -mabi=lp64 -nostdlib -o example_extended example_extended.S
          riscv64-unknown-elf-objdump -d example_extended > example_extended.objdump
          wsim --vcd --sim verilator rv64gc --elf example_extended
          gtkwave ~/Wally/cvw/sim/verilator/testbench.vcd
          ```

    * This is an example of the trace generated:

![image](https://github.com/user-attachments/assets/51e0e026-6e9b-4f45-82dd-fb757ba7f505)
    

4. Look at the following video showing the execution of CVW Wally in FPGA: ...
5. Look at the following video showing the execution of CVA6 in Verilator: ...
6. Look at the following video showing the execution of CVA6 in Verilator: ...
