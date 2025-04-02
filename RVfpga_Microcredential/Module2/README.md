# Module 2 - Input/Output in the RVfpga SoC

## Module General Contents
In this second module, students will learn how to use and extend the input/output (I/O) system of RVfpga to enable the RISC-V processor to interact with peripheral devices. Since the SoC used in the course is programmed in Verilog, we will begin with an introduction to this hardware description language (Topic 1).
In Topic 2 of this second module, we will first describe the main features of a general-purpose I/O system and the one used in the RVfpga system. Then, a simplified theoretical version of a generic GPIO controller will be presented. Finally, we will focus on the GPIO controller used in SweRVolfX: first, its high-level specification will be analyzed and basic exercises will be presented, followed by a deeper look into its low-level implementation and more advanced exercises where new GPIO-based peripherals will be added.
Next, following a similar structure, Topics 3 and 4 will provide a detailed study of 7-segment displays and counters, including both basic and advanced exercises where these devices will be modified to include new functionalities.
In Topic 5, we will introduce interrupt-based I/O and develop programs that use this mechanism, comparing them to similar polling-based programs.
Finally, in Topic 6, serial buses will be introduced, and we will work with the accelerometer available on the board.

## Module Workflow
Follow the next steps to analyze the RVfpga Input/Output System, first at a high-level and then at a low-level.

**To complete between June 2 and June 5:**

1. Look at Chapter 4 (System Verilog) and Chapter 9 (Input/Output) of the H&H book.

2. View this video [InputOutputVideo](https://www.youtube.com/watch?v=8fK-CoEbo0Y) (the video is in Spanish, but you can watch an AI-translated-to-English version of the video here: [InputOutputEnglishVideo](https://www.youtube.com/watch?v=oIRFxQEBNAc), you can watch an AI-translated-to-Chinese version of the video here: [InputOutputChineseVideo](https://www.youtube.com/watch?v=gG0HSeJ9ew8), or you can enable the subtitles in the video in Spanish). The video describes the RVfpga I/O System in detail. You can download the slides [here](https://drive.google.com/file/d/1Fv4-I8DwISdqqDpol4i_BMZNzK4QmpOe/view?usp=sharing).

3. Resolve the following I/O high-level exercises (note that these exercises just require you to understand and execute some provided programs):
   * [Exercise-1](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab4#exercise-1).
   * [Exercise-3](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab4#exercise-3).
   * [Exercise-5](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab4#exercise-5).

**JUNE 6 SESSION:**

4. Complete the following exercises:
   * To be provided.
<!--
   * [Exercise-2](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab4#exercise-2).
   * [Exercise-4](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab4#exercise-4).
   * [Exercise-6](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab4#exercise-6).
   * [Exercise-7](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab4#exercise-7).
-->

5. If you want to continue practicing after completing the proposed exercises, you can find more exercises in [RVfpga](https://university.imgtec.com/rvfpga-el2-v3-0-english-downloads-page/) labs 5 to 10.

**To complete between June 9 and June 12:**

6. Understand in detail the 8-Digit 7-Segment-Displays controller Verilog controller implemented in file *Simuladores_EC_24-25/RVfpga/src/SweRVolfSoC/Peripherals/SystemController/swervolf_syscon.sv*. Use a simulation in RVfpga-Trace to help you understand the module. Note that the counter is prepared for the board, and you must significantly decrease its period to work in simulation.

**JUNE 13 SESSION:**

7. Complete the following exercises:
   * To be provided.
<!--
   * Resolve the I/O low-level exercises included at: [Exercises_InputOutput_LowLevel](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Integrated_Systems_Architecture/Lab8#exercise-1).
-->

8. If you want to continue practicing after completing the proposed exercises, you can find more exercises in [RVfpga](https://university.imgtec.com/rvfpga-el2-v3-0-english-downloads-page/) labs 5 to 10.
