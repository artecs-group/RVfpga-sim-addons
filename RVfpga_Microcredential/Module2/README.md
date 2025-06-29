# Module 2 - Input/Output in the RVfpga SoC

## General Contents
In this second module, students will learn how to use and extend the input/output (I/O) system of RVfpga to enable the RISC-V processor to interact with peripheral devices. Since the SoC used in the course is programmed in Verilog, we will begin with an introduction to this hardware description language (Topic 1).
In Topic 2 of this second module, we will first describe the main features of a general-purpose I/O system and the one used in the RVfpga system. Then, a simplified theoretical version of a generic GPIO controller will be presented. Finally, we will focus on the GPIO controller used in SweRVolfX: first, its high-level specification will be analyzed and basic exercises will be presented, followed by a deeper look into its low-level implementation and more advanced exercises where new GPIO-based peripherals will be added.
Next, following a similar structure, Topics 3 and 4 will provide a detailed study of 7-segment displays and counters, including both basic and advanced exercises where these devices will be modified to include new functionalities.
In Topic 5, we will introduce interrupt-based I/O and develop programs that use this mechanism, comparing them to similar polling-based programs.
Finally, in Topic 6, serial buses will be introduced, and we will work with the accelerometer available on the board.

## Workflow
Follow the next steps to analyze the RVfpga Input/Output System, first at a high-level and then at a low-level.

### To complete between June 9 and 12:

1. Look at Chapter 4 (System Verilog) and Chapter 9 (Input/Output) of the [H&H book](https://www.amazon.es/Digital-Design-Computer-Architecture-RISC-V/dp/0128200642).

2. View this video [InputOutputVideo](https://www.youtube.com/watch?v=8fK-CoEbo0Y) (the video is in Spanish, but you can watch an AI-translated-to-English version of the video here: [InputOutputEnglishVideo](https://www.youtube.com/watch?v=oIRFxQEBNAc), you can watch an AI-translated-to-Chinese version of the video here: [InputOutputChineseVideo](https://www.youtube.com/watch?v=gG0HSeJ9ew8), or you can enable the subtitles in the video in Spanish). The video describes the RVfpga I/O System in detail. You can download the slides [here](https://drive.google.com/file/d/1Fv4-I8DwISdqqDpol4i_BMZNzK4QmpOe/view?usp=sharing).

3. In case you need it, you can find more theoretical details about the RVfpga I/O System in Labs 6 to 10 of the full package. You can also find the solutions to most of these exercises at ```RVfpgaEH1/RVfpga/Labs/RVfpgaLabsSolutions/ProgramsAndDocuments```.

4. Look at the following I/O high-level exercises. Note that they just require you to understand and test some provided programs, that you will use as the base to develop other programs:
   * [Exercise-1](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab4#exercise-1)
   * [Exercise-3](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab4#exercise-3)
   * [Exercise-5](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab4#exercise-5)

### JUNE 13 SESSION:
<!--
-->
5. Complete the following exercises:
   * [Exercise-4](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab4#exercise-4)
   * [Exercise-6](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab4#exercise-6)
   * [Exercise-7](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab4#exercise-7)
   * (OPTIONAL) [Exercise-2](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab4#exercise-2)

6. (OPTIONAL) You can continue practicing after completing the previous exercises. You can find more exercises at [RVfpga](https://university.imgtec.com/rvfpga-el2-v3-0-english-downloads-page/) labs 5 to 10. For example, you can try to complete the following exercises:
   * Exercise 1 of ```RVfpga/RVfpgaEH1/RVfpga/Labs/Lab08/RVfpga_Lab08.pdf```.
   * Exercise 1 of ```RVfpga/RVfpgaEH1/RVfpga/Labs/Lab09/RVfpga_Lab09.pdf```.
   * Program and execute each of the following modifications to the previous code:
       * The two least significant switches must be used, not just one.
       * The first switch will toggle between two counting speeds.
       * The second switch will toggle the counting direction:
           * Count from 1 to 9, incrementing by one.
           * Count from 9 to 1, decrementing by one.
       * Unlike the original code, the LEDs do not need to toggle their state on each 0-to-1 transition; instead, they should remain off.
   * Exercise 1 of ```RVfpga/RVfpgaEH1/RVfpga/Labs/Lab10/RVfpga_Lab10.pdf```.

### To complete between June 16 and 19:

7. Understand in detail the 8-Digit 7-Segment-Displays controller Verilog controller implemented in file *Simuladores_EC_24-25/RVfpga/src/SweRVolfSoC/Peripherals/SystemController/swervolf_syscon.sv*. Use a simulation in RVfpga-Trace to help you understand the module. Note that the scanning frequency of the displays controller in the baseline SoC is prepared for running on the board, so we must significantly decrease its period to work in simulation. Follow these steps to run a simulation in RVfpga-Trace:

    * Download the following project, which writes the value 1-3-5-7-2-4-6-8 in the 8-digit 7-Segment displays, and move it to the home of the Virtual Machine: [Project_RVfpgaTrace_7SegDisplays](https://drive.google.com/file/d/1WIYOgUAcneO_M4VfKQ0ZhYQ7s_tyD-tS/view?usp=sharing).
    * Note that the project includes a new version of the RVfpga-Trace simulator, provided inside the project itself (file ```Vrvfpgasim```), in which the scanning frequency of the displays controller has been significantly reduced.
    * This is the RVfpga-Trace simulation that you should obtain, using the signals included in the ```test.tcl``` provided file. 

      ![image](https://github.com/user-attachments/assets/c7c58d6c-b1ea-4f50-9b1d-03850db7ba97)

    * Later, when you need to regenerate the binary of the simulator to debug your changes in *Exercise-1_InputOutput_LowLevel*, you can follow the instructions provided in Chapter 7 of the Getting Started Guide of the RVfpga package (document ```RVfpgaEH1/RVfpga/Documents/RVfpga_GettingStartedGuide.pdf```). Specifically, in the Virtual Machine:

        * Go into ```/home/rvfpga/Simuladores_EC_24-25/RVfpga/src``` and perform the changes you consider to the 7-Segment displays controller.
        * In a terminal, go into ```/home/rvfpga/Simuladores_EC_24-25/RVfpga/verilatorSIM_Trace``` and regenerate the simulator binary by typing ```make```.
        * Using the new binary (```/home/rvfpga/Simuladores_EC_24-25/RVfpga/verilatorSIM_Trace/Vrvfpgasim```), run the project provided above in this item to debug your implementation.

8. In case you need it, you can find more theoretical details about the RVfpga I/O System in Labs 6 to 10 of the full package. You can also find the solutions to most of these exercises at ```RVfpgaEH1/RVfpga/Labs/RVfpgaLabsSolutions/Modified_RVfpgaSystem```.

9. Install Vivado in your computer. For example, to install Vivado in Windows, follow these instructions (in the GSG of the RVfpga course you can find more detailed instructions):
    * Go into the [Vivado Download Website](https://www.xilinx.com/support/download/index.html/content/xilinx/en/downloadNav/vivado-design-tools/archive.html). You will be asked to log in to your Xilinx account before you can download the installer; if you don’t already have an account, you will need to create one.
    * Select the Vivado version that you wish to download (we recommend version 2022.2, but version 2019.2 is also verified for RVfpga and more modern versions should also work). For example, in Windows, click on *Xilinx Unified Installer 2022.2: Windows Self Extracting Web Installer*.
    * The Vivado installer will walk you through the installation process. Important notes:
      * Select *Vivado* as the Product to install.
      * Select version *Vivado ML Standard* (not *Vivado ML Enterprise*), as this is the no-cost version.
      * Set all the I Agree boxes.
      * Otherwise, defaults should be selected.

10. Once you have installed Vivado, try to complete Lab 5 of the RVfpga package (you can find the document at ```RVfpga/RVfpgaEH1/RVfpga/Labs/Lab05```), where the bitstream for the RVfpga SoC is created. When you are creating the project in Vivado, at the point where you must select the board (in our case Nexys A7 or Nexys 4 DDR), you first need to click on the *Refresh* button to add these boards. If this does not work, you can also manually install the Board Files:
    * Download the archive [vivado-boards](https://github.com/Digilent/vivado-boards/archive/master.zip?_ga=2.158467251.828100773.1587959567-2022567073.1577108610) and extract it.
    * Open the folder extracted from the archive and navigate to its ```new/board_files``` directory. Select this directory and copy it.
    * Open the folder that Vivado was installed in your system. Under this folder, navigate to its ```<version>/data/boards``` directory, then paste the ```board_files``` into this directory.

### JUNE 20 SESSION:
<!--
-->
11. Complete the following exercises:
   * [Exercise-1_InputOutput_LowLevel](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Integrated_Systems_Architecture/Lab8#exercise-1).
   * [Exercise-2_InputOutput_LowLevel](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Integrated_Systems_Architecture/Lab8#exercise-2).
12. (OPTIONAL) You can continue practicing after completing the previous exercises. You can find more exercises at [RVfpga](https://university.imgtec.com/rvfpga-el2-v3-0-english-downloads-page/) labs 5 to 10. For example, you can try to complete the following exercises (the programs must be developed for VeeR EH1, but in this case we refer to the VeeR EL2 documentation, as it is more up-to-date and the instructions are identical for both cores):
   * Exercises 2 and 3 of ```RVfpga/RVfpgaEL2/RVfpga_NexysA7-DDR/Labs/Lab06/RVfpga_Lab06_VeeR-EL2_NexysA7-DDR.pdf```, which extend the SoC with support to communicate with the buttons included in the Nexys A7 board.
   * Exercises 2 and 3 of ```RVfpga/RVfpgaEL2/RVfpga_NexysA7-DDR/Labs/Lab08/RVfpga_Lab08_VeeR-EL2_NexysA7-DDR.pdf```, which work with the PTC and specifically use the PWM tri-color LED included in the Nexys A7 board.
   * Exercises 2 and 3 of ```RVfpga/RVfpgaEL2/RVfpga_NexysA7-DDR/Labs/Lab09/RVfpga_Lab09_VeeR-EL2_NexysA7-DDR.pdf```.
