# Lab 4 - Execution of basic instructions and adding new instructions on the VeeR EH1 core
In this lab we continue the analysis of the VeeR EH1 core, analyzing the execution of basic instructions and adding new instructions to the core. The exercises proposed can be performed both in simulation and on the FPGA board. In this repository, we explain how to use the simulators, and you can find all the instructions for running on the board in the complete [RVfpga](https://university.imgtec.com/rvfpga-el2-v3-0-english-downloads-page/) course.

Follow the next steps:

1. At time 11:12 of the following video, you can visualize an example of the RVfpga-Trace simulator running a program: [RVfpgaToolsVideo](https://www.youtube.com/watch?v=Z8QcQRW7F4s) (the video is in Spanish, but you can watch an AI-translated-to-English version of the video here [RVfpgaToolsEnglishVideo](https://www.youtube.com/watch?v=HuAF2XOMQmQ), you can watch an AI-translated-to-Chinese version of the video here [RVfpgaToolsChineseVideo](https://www.youtube.com/watch?v=A_c8GACrW9w), or you can enable the subtitles in the original video).

2. View this video [PerformanceBenchmarkingVideo](https://www.youtube.com/watch?v=GqaDEW3W4X0) (the video is in Spanish, but you can watch an AI-translated-to-English version of the video here: [PerformanceBenchmarkingEnglishVideo](https://www.youtube.com/watch?v=DXB7jl1iGq8), or you can enable the subtitles in the video in Spanish). You can download the [slides](https://drive.google.com/file/d/146nEyUkGkXn85cS15EiUM7R0Bv1nKyoT/view?usp=sharing). The video illustrates the following items:
    * How to extend the VeeR EH1 processor with new instructions and how we can improve its peformance using them (a description of how to add new instructions to VeeR EH1 is at time 6:29 and an example running on RVfpga-ViDBo is at time 14:49).

3. Perform the following exercises.


## Exercise 1
*→ View the above PerformanceBenchmarkingVideo at time 18:00 to see an example running on RVfpga-ViDBo.*

Follow the instructions explained in the slides and the video in order to test the extended core with the simple example that does a floating point addition. You can download the project with the program from this link: [Project_RVfpgaViDBo_FPU_Example.zip](https://drive.google.com/file/d/1uo8-gNwMsI5FdqHA_IdATUjjIipB3zYw/view?usp=drive_link). Once downloaded and uncompressed, move it to your home directory inside the Virtual Machine.

Note that you do not need to modify the core sources nor recompile the simulator binary, as we provide the binary through the following link: [Vrvfpgasim](https://drive.google.com/file/d/1PtQBGKW1Z3E_h3deqgwIjjDKWUeLiDrq/view?usp=sharing). Once downloaded, move it to your home directory inside the Virtual Machine and give it execution rights: ```chmod 777 Vrvfpgasim```. In case you want to analyze the core sources and create the binary/bitstream yourself, you can download the extended core sources here: [src_FPU](https://drive.google.com/file/d/1199soZSgC8ZiqvnQjMRLNSkZAyRviOb5/view?usp=sharing).


**TASK:**
Do the same tests for a multiplication and a division instead of an addition. Analyze the results obtained for the operations and for the HW counter events.

These are the 32-bit formats for these two FP instructions:

<p align="center">
  <img src="Images/MultDiv.png" width=40% height=40%>
</p>


## Exercise 2
In this exercise you will test a program with floating point operations, using the extended SoC. Follow the next steps:

   1. Download the following program, which computes the dot product of two vectors: [DotProduct](https://drive.google.com/file/d/1FxCZzNDfhHamieTfrMSGTSZLJr-9cMYl/view?usp=sharing). Unzip the file and move the obtained folder to the home directory.
   2. Open the project in VSCode and analyze the program in detail.
   3. Execute the program on the ViDBo simulator that you downloaded in the previous exercise and explain the results obtained.



## Exercise 3
In this exercise you will upgrade the gcc simulator in PlatformIO to a version that supports the Zfinx extension. Follow the next steps:

- Download this simple project, that computes a FP addition and move it to the home directory: [Project_RVfpgaViDBo_FPU_Example_NewCompiler.zip](https://drive.google.com/file/d/1CGB2MIz0s7XzF475xfu6WPXIkpyvQ8lF/view?usp=sharing)

- Replace the following file (keep a backup copy of this file before replacing it): ```~/.platformio/platforms/chipsalliance/builder/main.py``` for the one that you can download here: [main.py](https://drive.google.com/file/d/1dlx2YjdlljqLzgwz1vNzZ9FJVIOsBjbs/view?usp=sharing)
  
Then, do the following tasks:

1. Execute the provided program in RVfpga-ViDBo using the extended SoC (you should have the simulator binary in the home directory, as you used it in the previous tasks). In file ```platformio.ini``` you can see the ```build_flags``` set as follows, which enable the Zfinx extension in the compiler:

<p align="center">
  <img src="Images/Zfinx.png" width=40% height=40%>
</p>

   - First test it with Zfinx extension enabled (the default option shown in the figure).
      - Check the number of cycles needed to execute the addition.
      - Analyze the disassembly code generated by the compiler. The floating point addition in C should have been transformed to an ```fadd``` instruction by the compiler.
   - Then, disable the Zfinx extension in file platformio.ini by removing the ```_zfinx``` text in the two places where it’s found in that file:
      - Check the number of cycles needed to execute the addition.
      - Analyze the disassembly code generated by the compiler. The floating point addition in C should have been transformed to an emulation of the operation.
   - Compare and explain the number of cycles that are obtained in the two cases.

2. Do the same tests for the other floating point instructions implemented in the extended SoC: ```fmul``` and ```fdiv```.

To go back to the previous compiler, follow the next steps:

1. Close the Project_RVfpgaViDBo_FPU_Example_NewCompiler project.
2. Go into the Extensions tab in VSCode and uninstall the PlatformIO IDE. Close VSCode.
3. Open a terminal, go into the home directory, and delete directory ```.platformio``` using the following command: ```rm -rf .platformio```
4. Open VSCode, reinstall the PlatformIO IDE extension and test a program from a previous task.
