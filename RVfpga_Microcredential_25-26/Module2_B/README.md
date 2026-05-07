# Module 2 - Low-Level Input/Output in the RVfpga SoC

## General Contents
In this second module, students will work with the input/output (I/O) system of the RVfpga SoC and learn how the RISC-V processor interacts with external peripherals implemented in hardware. Throughout the module, students will use and modify existing peripherals such as GPIOs, LEDs, switches, counters, and 7-segment displays, combining software development in C and assembly with hardware design in SystemVerilog.

The module includes both high-level programming exercises using the existing RVfpga platform and lower-level activities focused on understanding and extending the internal hardware implementation of the SoC. Students will also explore interrupt-based I/O, as well as simulation and debugging workflows using RVfpga-Trace and Vivado tools.

---

## Previous work to complete between May 25 and 28:

1. Understand in detail the 8-Digit 7-Segment-Displays controller Verilog controller implemented in file */home/rvfpga/RVfpga_MasterUCLM/src/SweRVolfSoC/Peripherals/SystemController/swervolf_syscon.sv*. Use a simulation in RVfpga-Trace to help you understand the module. Note that the scanning frequency of the displays controller in the baseline SoC is prepared for running on the board, so we must significantly decrease its period to work in simulation. Follow these steps to run a simulation in RVfpga-Trace:

    * Download the following project, which writes the value 1-3-5-7-2-4-6-8 in the 8-digit 7-Segment displays, and move it to the home of the Virtual Machine: [Project_RVfpgaTrace_7SegDisplays](https://drive.google.com/file/d/1WIYOgUAcneO_M4VfKQ0ZhYQ7s_tyD-tS/view?usp=sharing).
    * Note that the project includes a new version of the RVfpga-Trace simulator, provided inside the project itself (file ```Vrvfpgasim```), in which the scanning frequency of the displays controller has been significantly reduced.
    * This is the RVfpga-Trace simulation that you should obtain, using the signals included in the ```test.tcl``` provided file. 

      ![image](https://github.com/user-attachments/assets/c7c58d6c-b1ea-4f50-9b1d-03850db7ba97)

    * Later, when you need to regenerate the binary of the simulator to debug your changes in *Exercise-1_InputOutput_LowLevel*, you can follow the instructions provided in Chapter 7 of the Getting Started Guide of the complete RVfpga package (document ```RVfpgaEH1/RVfpga/Documents/RVfpga_GettingStartedGuide.pdf```). Specifically, in the Virtual Machine:

        * Go into ```/home/rvfpga/RVfpga_MasterUCLM/src``` and perform the changes you consider to the 7-Segment displays controller.
        * In a terminal, go into ```/home/rvfpga/RVfpga_MasterUCLM/verilatorSIM_Trace``` and regenerate the simulator binary by typing ```make```.
        * Using the new binary (```/home/rvfpga/RVfpga_MasterUCLM/verilatorSIM_Trace/Vrvfpgasim```), run the project provided above in this item to debug your implementation.

2. In case you need it, you can find more theoretical details about the RVfpga I/O System in Labs 6 to 10 of the full package.

3. Install Vivado in your computer. To install Vivado in Windows, follow these instructions (in the GSG of the RVfpga course you can find more detailed instructions):
  * Go into the [Vivado Download Website](https://www.xilinx.com/support/download/index.html/content/xilinx/en/downloadNav/vivado-design-tools/archive.html). You will be asked to log in to your Xilinx account before you can download the installer; if you don’t already have an account, you will need to create one.
  * Select the Vivado version that you wish to download (we recommend version 2022.2, but version 2019.2 is also verified for RVfpga and more modern versions should also work). For example, in Windows, click on *Xilinx Unified Installer 2022.2: Windows Self Extracting Web Installer*.
  * The Vivado installer will walk you through the installation process. Important notes:
    * Select *Vivado* as the Product to install.
    * Select version *Vivado ML Standard* (not *Vivado ML Enterprise*), as this is the no-cost version.
    * Set all the I Agree boxes.
    * Otherwise, defaults should be selected.
    * When you are creating a Vivado project, at the point where you must select the board (in our case Nexys A7 or Nexys 4 DDR), you first need to click on the *Refresh* button to add these boards. If this does not work, you can also manually install the Board Files:
      * Download the archive [vivado-boards](https://github.com/Digilent/vivado-boards/archive/master.zip?_ga=2.158467251.828100773.1587959567-2022567073.1577108610) and extract it.
      * Open the folder extracted from the archive and navigate to its ```new/board_files``` directory. Select this directory and copy it.
      * Open the folder that Vivado was installed in your system. Under this folder, navigate to its ```<version>/data/boards``` directory, then paste the ```board_files``` into this directory.

4. Once you have installed Vivado, try to complete Lab 5 of the RVfpga package (you can find the document at ```RVfpga/RVfpgaEH1/RVfpga/Labs/Lab05```), where the bitstream for the RVfpga SoC is created. When you are creating the project in Vivado, at the point where you must select the board (in our case Nexys A7 or Nexys 4 DDR), you first need to click on the *Refresh* button to add these boards. If this does not work, you can also manually install the Board Files:
    * Download the archive [vivado-boards](https://github.com/Digilent/vivado-boards/archive/master.zip?_ga=2.158467251.828100773.1587959567-2022567073.1577108610) and extract it.
    * Open the folder extracted from the archive and navigate to its ```new/board_files``` directory. Select this directory and copy it.
    * Open the folder that Vivado was installed in your system. Under this folder, navigate to its ```<version>/data/boards``` directory, then paste the ```board_files``` into this directory.

---


## To complete on May 29:

5. Complete the following exercises:
   * [Exercise-1_InputOutput_LowLevel](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Integrated_Systems_Architecture/Lab8#exercise-1).
   * [Exercise-2_InputOutput_LowLevel](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Integrated_Systems_Architecture/Lab8#exercise-2).
6. (OPTIONAL) You can continue practicing after completing the previous exercises. You can find more exercises at [RVfpga](https://university.imgtec.com/rvfpga-el2-v3-0-english-downloads-page/) labs 5 to 10. For example, you can try to complete the following exercises (the programs must be developed for VeeR EH1, but in this case we refer to the VeeR EL2 documentation, as it is more up-to-date and the instructions are identical for both cores):
   * Exercises 2 and 3 of ```RVfpga/RVfpgaEL2/RVfpga_NexysA7-DDR/Labs/Lab06/RVfpga_Lab06_VeeR-EL2_NexysA7-DDR.pdf```, which extend the SoC with support to communicate with the buttons included in the Nexys A7 board.
   * Exercises 2 and 3 of ```RVfpga/RVfpgaEL2/RVfpga_NexysA7-DDR/Labs/Lab08/RVfpga_Lab08_VeeR-EL2_NexysA7-DDR.pdf```, which work with the PTC and specifically use the PWM tri-color LED included in the Nexys A7 board.
   * Exercises 2 and 3 of ```RVfpga/RVfpgaEL2/RVfpga_NexysA7-DDR/Labs/Lab09/RVfpga_Lab09_VeeR-EL2_NexysA7-DDR.pdf```.

