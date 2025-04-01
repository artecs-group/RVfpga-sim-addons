# Module 2 - Input/Output in the RVfpga SoC

## Module General Contents
In this second module, students will learn how to use and extend the input/output (I/O) system of RVfpga to enable the RISC-V processor to interact with peripheral devices. Since the SoC used in the course is programmed in Verilog, we will begin with an introduction to this hardware description language (Topic 1).
In Topic 2 of this second module, we will first describe the main features of a general-purpose I/O system and the one used in the RVfpga system. Then, a simplified theoretical version of a generic GPIO controller will be presented. Finally, we will focus on the GPIO controller used in SweRVolfX: first, its high-level specification will be analyzed and basic exercises will be presented, followed by a deeper look into its low-level implementation and more advanced exercises where new GPIO-based peripherals will be added.
Next, following a similar structure, Topics 3 and 4 will provide a detailed study of 7-segment displays and counters, including both basic and advanced exercises where these devices will be modified to include new functionalities.
In Topic 5, we will introduce interrupt-based I/O and develop programs that use this mechanism, comparing them to similar polling-based programs.
Finally, in Topic 6, serial buses will be introduced, and we will work with the accelerometer available on the board.

## Module Workflow
Follow the next steps to analyze the RVfpga Input/Output System, first at a high-level and then at a low-level.
1. Take a look at Chapter 4 (System Verilog) and Chapter 9 (Input/Output) of the H&H book.
2. Then, view this video [InputOutputVideo](https://www.youtube.com/watch?v=8fK-CoEbo0Y) (the video is in Spanish, but you can watch an AI-translated-to-English version of the video here: [InputOutputEnglishVideo](https://www.youtube.com/watch?v=oIRFxQEBNAc), you can watch an AI-translated-to-Chinese version of the video here: [InputOutputChineseVideo](https://www.youtube.com/watch?v=gG0HSeJ9ew8), or you can enable the subtitles in the video in Spanish). The video describes the RVfpga I/O System in detail. You can download the slides [here](https://drive.google.com/file/d/1Fv4-I8DwISdqqDpol4i_BMZNzK4QmpOe/view?usp=sharing).
3. Then, you can resolve the I/O high-level exercises included at: [Exercises_InputOutput_HighLevel](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab4#exercise-1). Note that exercises 1, 3 and 5 just require you to replicate some provided programs.
4. Then, you can resolve the I/O low-level exercises included at: [Exercises_InputOutput_LowLevel](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Integrated_Systems_Architecture/Lab8#exercise-1).
5. Finally, if you want to continue practicing after completing the proposed exercises, you can find more complex exercises in [RVfpga](https://university.imgtec.com/rvfpga-el2-v3-0-english-downloads-page/) labs 5 to 10.
