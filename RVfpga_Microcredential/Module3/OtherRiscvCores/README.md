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

    * Prepare or buy a compatible microSD card.

      Wally boots Linux from a microSD card. Therefore, each student needs a microSD card that will be flashed with the Linux image used in this activity.

      Recommended characteristics:

        * Capacity: 32 GB or larger.
        * Type: microSDHC or microSDXC.
        * Speed class: Class 10 / UHS-I recommended.
        * Adapter: an SD adapter or USB microSD reader is needed to write the image from the computer.

      Tested cards:

      | microSD card | Capacity | Status |
      |---|---:|---|
      | SanDisk Ultra microSDHC / microSDXC | 32 GB | Tested successfully |
      | Kingston microSD | 32 GB | Tested successfully |

      > [!IMPORTANT]
      > The microSD card will be erased during the preparation process. Do not use a card containing important data.

    * Download the required prebuilt files from the following GitHub release:

      [CVW-Wally Nexys A7 Files](https://github.com/artecs-group/RVfpga-sim-addons/releases/tag/v1.0-wally-nexysa7)

      Download the following files:

        * `WallyNexysA7_SD.img.xz`
        * `fpgaTop.bit`

      Move both files to the `Downloads` folder of the VM.

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

    * Flash the microSD card.

      Insert the microSD card into the computer and identify its device name:

      ```bash
      lsblk
      ```

      Look for the device corresponding to the microSD card. It will typically appear as something like `/dev/sda`, `/dev/sdb`, or `/dev/mmcblk0`.

      > [!WARNING]
      > Be very careful when selecting the device. The next command will completely erase the selected device. Make sure that you select the microSD card, not your main hard drive.

      If any partition of the microSD card has been automatically mounted, unmount it before flashing. For example, if the card appears as `/dev/sdX`, run:

      ```bash
      sudo umount /dev/sdX1 2>/dev/null
      sudo umount /dev/sdX2 2>/dev/null
      sudo umount /dev/sdX3 2>/dev/null
      sudo umount /dev/sdX4 2>/dev/null
      ```

      Replace `sdX` with the actual device name of your microSD card.

      Flash the SD card image:

      ```bash
      xzcat ~/Downloads/WallyNexysA7_SD.img.xz | sudo dd of=/dev/sdX bs=4M status=progress conv=fsync
      sync
      ```

      Replace `/dev/sdX` with the actual microSD device.

      > [!IMPORTANT]
      > Use the device name, for example `/dev/sdX`, not a partition such as `/dev/sdX1`.

      When the command finishes, safely remove the microSD card and insert it into the Nexys A7 board.

    * Connect the hardware:

        * Nexys A7 board
        * microUSB cable
        * microSD card prepared in the previous step

    * Program the FPGA using the programming tool provided by the instructor.

      Load the bitstream:

      ```bash
      cd ~
      ~/.platformio/packages/tool-openocd-riscv-chipsalliance/bin/openocd -c "set BITFILE /home/rvfpga/Downloads/fpgaTop.bit" -f ~/RVfpga_MasterUCLM/src/OtherSources/ConfigFiles/swervolf_nexys_program.cfg
      ```

      Wait until programming finishes successfully.

    * Open the UART terminal.

      You may need to change `ttyUSB1` to another number, such as `ttyUSB0`.

      ```bash
      sudo apt install screen
      screen /dev/ttyUSB1 115200
      ```

    * Press the **RESET** button on the Nexys A7 board.

      If everything works correctly, you should see:

        * BootROM messages
        * OpenSBI messages
        * Linux boot logs
        * A Linux login prompt

      Log in as:

      ```text
      root
      ```

      After logging in, you should see a Linux shell prompt similar to:

      ```text
      #
      ```

    * Mount the fourth partition of the microSD card.

      The following commands must be executed inside the UART terminal, after Linux has booted on Wally:

      ```bash
      mkdir -p /mnt/sd
      mount /dev/mmcblk0p4 /mnt/sd
      ```

      Check the contents:

      ```bash
      ls /mnt/sd
      ```

    * Test the GPIO peripheral.

      The LEDs LD0-LD4 are connected to the GPIO peripheral.

      Enable GPIO outputs:

      ```bash
      devmem 0x10060008 32 0x1F
      devmem 0x1006000C 32 0x1F
      ```

      Expected result: LEDs LD0-LD4 should turn on.

    * Test the seven-segment display peripheral.

      Write the segment pattern:

      ```bash
      devmem 0x00100000 32 0x77
      ```

      Expected result: the seven-segment display should show the character `A`.

    * Exit the UART terminal.

      To exit `screen`:

      ```text
      Ctrl+A
      K
      ```

    * Optional: read the implementation details.

      The implementation of the seven-segment display as an APB peripheral for CVW-Wally is documented in Mario Miralles' repository:

      [Nexys A7: Seven Segment Display peripheral](https://github.com/mmiral04/cvw_apb_peripheral)
