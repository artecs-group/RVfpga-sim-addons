# Module 2 - Input/Output in the RVfpga SoC

## General Contents
In this second module, students will learn how to use and extend the input/output (I/O) system of RVfpga to enable the RISC-V processor to interact with peripheral devices. Since the SoC used in the course is programmed in Verilog, we will begin with an introduction to this hardware description language (Topic 1).
In Topic 2 of this second module, we will first describe the main features of a general-purpose I/O system and the one used in the RVfpga system. Then, a simplified theoretical version of a generic GPIO controller will be presented. Finally, we will focus on the GPIO controller used in SweRVolfX: first, its high-level specification will be analyzed and basic exercises will be presented, followed by a deeper look into its low-level implementation and more advanced exercises where new GPIO-based peripherals will be added.
Next, following a similar structure, Topics 3 and 4 will provide a detailed study of 7-segment displays and counters, including both basic and advanced exercises where these devices will be modified to include new functionalities.
In Topic 5, we will introduce interrupt-based I/O and develop programs that use this mechanism, comparing them to similar polling-based programs.
Finally, in Topic 6, serial buses will be introduced, and we will work with the accelerometer available on the board.

## Workflow
Follow the next steps to analyze the RVfpga Input/Output System, first at a high-level and then at a low-level.

**To complete between June 2 and 5:**

1. Look at Chapter 4 (System Verilog) and Chapter 9 (Input/Output) of the H&H book.

2. View this video [InputOutputVideo](https://www.youtube.com/watch?v=8fK-CoEbo0Y) (the video is in Spanish, but you can watch an AI-translated-to-English version of the video here: [InputOutputEnglishVideo](https://www.youtube.com/watch?v=oIRFxQEBNAc), you can watch an AI-translated-to-Chinese version of the video here: [InputOutputChineseVideo](https://www.youtube.com/watch?v=gG0HSeJ9ew8), or you can enable the subtitles in the video in Spanish). The video describes the RVfpga I/O System in detail. You can download the slides [here](https://drive.google.com/file/d/1Fv4-I8DwISdqqDpol4i_BMZNzK4QmpOe/view?usp=sharing).

3. Resolve the following I/O high-level exercises (note that these exercises just require you to understand and execute some provided programs):
   * [Exercise-1](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab4#exercise-1)
   * [Exercise-3](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab4#exercise-3)
   * [Exercise-5](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab4#exercise-5)

**JUNE 6 SESSION:**

TO BE PROVIDED

<!--
4. Complete the following exercises:
   * [Exercise-2](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab4#exercise-2)
   * [Exercise-4](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab4#exercise-4)
   * [Exercise-6](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab4#exercise-6)
   * [Exercise-7](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab4#exercise-7)

5. If you want to continue practicing after completing the proposed exercises, you can find more exercises in [RVfpga](https://university.imgtec.com/rvfpga-el2-v3-0-english-downloads-page/) labs 5 to 10. For example, you can try to complete the following exercises:
   * Exercise 1 of ```RVfpga/RVfpgaEH1/RVfpga/Labs/Lab08/RVfpga_Lab08.pdf```.
   * Exercise 1 of ```RVfpga/RVfpgaEH1/RVfpga/Labs/Lab09/RVfpga_Lab09.pdf```.
   * Exercise 1 of ```RVfpga/RVfpgaEH1/RVfpga/Labs/Lab10/RVfpga_Lab10.pdf```.
-->

**To complete between June 9 and 12:**

6. Understand in detail the 8-Digit 7-Segment-Displays controller Verilog controller implemented in file *Simuladores_EC_24-25/RVfpga/src/SweRVolfSoC/Peripherals/SystemController/swervolf_syscon.sv*. Use a simulation in RVfpga-Trace to help you understand the module. Note that the counter is prepared for the board, and you must significantly decrease its period to work in simulation.

7. Install Vivado in your computer. For example, to install Vivado in Windows, follow these instructions (in the GSG of the RVfpga course you can find more detailed instructions):
    * Go into the [Vivado Download Website](https://www.xilinx.com/support/download/index.html/content/xilinx/en/downloadNav/vivado-design-tools/archive.html). You will be asked to log in to your Xilinx account before you can download the installer; if you don’t already have an account, you will need to create one.
    * Select the Vivado version that you wish to download (we recommend version 2022.2, but version 2019.2 is also verified for RVfpga and more modern versions should also work). For example, in Windows, click on *Xilinx Unified Installer 2022.2: Windows Self Extracting Web Installer*.
    * The Vivado installer will walk you through the installation process. Important notes:
      * Select *Vivado* as the Product to install.
      * Select version *Vivado ML Standard* (not *Vivado ML Enterprise*), as this is the no-cost version.
      * Set all the I Agree boxes.
      * Otherwise, defaults should be selected.

8. Once you have installed Vivado, try to complete Lab 5 of the RVfpga package (you can find the document at ```RVfpga/RVfpgaEH1/RVfpga/Labs/Lab05```), where the bitstream for the RVfpga SoC is created. When you are creating the project in Vivado, at the point where you must select the board (in our case Nexys A7 or Nexys 4 DDR), you first need to click on the *Refresh* button to add these boards. If this does not work, you can also manually install the Board Files:
    * Download the archive [vivado-boards](https://github.com/Digilent/vivado-boards/archive/master.zip?_ga=2.158467251.828100773.1587959567-2022567073.1577108610) and extract it.
    * Open the folder extracted from the archive and navigate to its ```new/board_files``` directory. Select this directory and copy it.
    * Open the folder that Vivado was installed in your system. Under this folder, navigate to its ```<version>/data/boards``` directory, then paste the ```board_files``` into this directory.

**JUNE 13 SESSION:**

TO BE PROVIDED

<!--
9. Complete the following exercises:
   * [Exercise-1_InputOutput_LowLevel](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Integrated_Systems_Architecture/Lab8#exercise-1).
   * [Exercise-2_InputOutput_LowLevel](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Integrated_Systems_Architecture/Lab8#exercise-2).
10. If you want to continue practicing after completing the proposed exercises, you can find more exercises in [RVfpga](https://university.imgtec.com/rvfpga-el2-v3-0-english-downloads-page/) labs 5 to 10. For example, you can try to complete the following exercises (the programs must be developed for VeeR EH1, but in this case we refer to the VeeR EL2 documentation, as it is more up-to-date and the instructions are identical for both cores):
   * Exercises 2 and 3 of ```RVfpga/RVfpgaEL2/RVfpga_NexysA7-DDR/Labs/Lab06/RVfpga_Lab06_VeeR-EL2_NexysA7-DDR.pdf```.
   * Exercises 2 and 3 of ```RVfpga/RVfpgaEL2/RVfpga_NexysA7-DDR/Labs/Lab08/RVfpga_Lab08_VeeR-EL2_NexysA7-DDR.pdf```.
   * Exercises 2 and 3 of ```RVfpga/RVfpgaEL2/RVfpga_NexysA7-DDR/Labs/Lab09/RVfpga_Lab09_VeeR-EL2_NexysA7-DDR.pdf```.

For example, you can look at Lab 6 (you can find the document at ```RVfpga/RVfpgaEL2/RVfpga_NexysA7-DDR/Labs/Lab06```), which extends the SoC with support to communicate with the buttons included in the Nexys A7 board, or at Lab 8 (you can find the document at ```RVfpga/RVfpgaEL2/RVfpga_NexysA7-DDR/Labs/Lab08```), which works with the PTC and specifically uses the PWM tri-color LED included in the Nexys A7 board.
-->
