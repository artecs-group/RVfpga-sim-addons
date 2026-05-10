# Other RISC-V Cores

In recent years, the open-source hardware ecosystem has witnessed a remarkable surge in the development and adoption of RISC-V cores. Thanks to its open and modular instruction set architecture, RISC-V has empowered academia, industry, and hobbyists to design and share a wide variety of cores tailored to different needs—from ultra-minimal implementations for microcontrollers to complex out-of-order processors for high-performance computing. In this page we explore a selection of these open RISC-V cores, highlighting their features, use cases, and the vibrant community driving this innovation.


1. Look at the following presentation: [OtherRiscvCores](https://drive.google.com/file/d/1N_pWZ8oRKA0aUdZg2EKY66rlhnqzTMtF/view?usp=sharing).


2. Follow these steps to replicate the Verilator CVW-Wally simulation in the VM:
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


3. Follow these steps to execute CVW-Wally on the Nexys A7 board:

    * Clone the repository:

      ```bash
      cd ~
      git clone https://github.com/mmiral04/cvw.git
      cd cvw
      git checkout apb_periph
      ```

    * Configure the Wally environment:

      ```bash
      mkdir -p ~/riscv
      ln -s /home/rvfpga/.platformio/packages/toolchain-riscv/* ~/riscv/
      touch ~/riscv/site-setup.sh
      source setup.sh
      ```

    * Download the prebuilt FPGA bitstream from the following link: [WallyBitstreamNexysA7](https://drive.google.com/file/d/1ffxz49z0T0R1YgDlZwsEVhFK-yr3Ll2f/view?usp=drive_link)

      Save the file as:

      ```text
      fpgaTop.bit
      ```

    * Connect the hardware:

        * Nexys A7 board
        * microUSB cable
        * preconfigured microSD card

      Insert the microSD card into the on-board SD slot.

    * Program the FPGA using the programming tool provided by the instructor.

      Load:

      ```text
      .platformio/packages/tool-openocd-riscv-chipsalliance/bin/openocd -c "set BITFILE fpgaTop.bit" -f ../RVfpga_MasterUCLM/src/OtherSources/ConfigFiles/swervolf_nexys_program.cfg
      ```

      Wait until programming finishes successfully.

    * Open the UART terminal:

      ```bash
      sudo apt install screen
      screen /dev/ttyUSB1 115200
      ```

      Check available serial devices with:

      ```bash
      ls /dev/ttyUSB*
      ```

    * Press the **RESET** button on the Nexys A7 board.

      If everything works correctly you should see:

        * BootROM messages
        * OpenSBI messages
        * Linux boot logs

      Finally:

      ```text
      #
      ```

    * Create a mount point:

      ```bash
      mkdir -p /mnt/sd
      ```

    * Mount the Linux partition:

      ```bash
      mount /dev/mmcblk0p4 /mnt/sd
      ```

      Check contents:

      ```bash
      ls /mnt/sd
      ```

    * Test the GPIO peripheral.

      The LEDs LD0-LD4 are connected to the GPIO peripheral.

      Configure GPIO direction:

      ```bash
      devmem 0x10060008 32 0x1F
      ```

      Enable GPIO outputs:

      ```bash
      devmem 0x1006000C 32 0x1F
      ```

      Expected result:

        * LEDs LD0-LD4 should turn on.

    * Test the seven-segment display peripheral.

      The seven-segment display peripheral is connected through APB.

      Peripheral base address:

      ```text
      0x00100000
      ```

      Write segment pattern:

      ```bash
      devmem 0x00100000 32 0x77
      ```

      Enable the first display:

      ```bash
      devmem 0x00100004 32 0x1
      ```

      Expected result:

        * The display should show the character `A`.

    * Exit the UART terminal.

      To exit `screen`:

      ```text
      Ctrl+A
      K
      ```
