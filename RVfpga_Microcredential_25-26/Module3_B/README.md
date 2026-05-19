# Module 3 - The VeeR EH1 core: Benchmarking, Performance Counters and ISA Extensions

## Previous work to complete between June 15 and 18:

### 1. Review of the memory hierarchy:

Look at Chapter 8 (Memory Systems) of the H&H book.

### 2. Watch the following video: 

[PerformanceBenchmarkingVideo](https://youtu.be/GqaDEW3W4X0?si=yf1rObPveS-RB-We&t=10) (the video is in Spanish, but you can watch an AI-translated-to-English version of the video here: [PerformanceBenchmarkingEnglishVideo](https://youtu.be/DXB7jl1iGq8?si=GODI7vlY9WCXIMny&t=10)).

  - From time 0:0 to time 6:25, the video shows a description of the VeeR Performance Counters and an example using RVfpga-ViDBo.
  - Then, from time 6:29 to time 24:18, the video describes how to extend the VeeR EH1 processor with new instructions and how we can improve its peformance using them.
  - Finally, from time 24:18 to the end, the video describes how to run the CoreMark benchmark on the RVfpga SoC.


### 3. Hw Counters example:

Test on the board the exercise shown in the video. Do the following steps:
   * Download the following project [HwCounters](https://drive.google.com/file/d/1OEnGku9_uccNFXdFMkXveIQuQzTUIfsJ/view?usp=sharing) and open it in VSCode. Note that this is the same program demonstrated in the video above, where the RVfpga-ViDBo simulator was used.
   * Run the program in RVfpga-ViDBo and on the board (if you have it).
      * RVfpga-Nexys (FPGA board): Set the path for the bitstream in the ```platformio.ini``` file as follows: ```board_build.bitstream_file = /home/rvfpga/Simuladores_EC_24-25/RVfpga/src/rvfpganexys.bit```
      * RVfpga-ViDBo (simulator): Set the path for the simulator in the ```platformio.ini``` file as follows: ```board_debug.verilator.binary = /home/rvfpga/Simuladores_EC_24-25/RVfpga/verilatorSIM_ViDBo/OriginalBinaries/RVfpga-ViDBo_Ubuntu22```
   * Analyze the results displayed in the serial console. Are they what you’d expect from the analyzed code?



## To complete in the 4th Session (Friday, June 12):

## Exercise 1 (mandatory)
Complete the following exercise: [Exercise-HwCounters_EH1](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Integrated_Systems_Architecture/Lab3#exercise-2) (second exercise).

## Exercise 2 (mandatory)
Complete the exercises proposed in the following link (Exercise 4 is optional): [Benchmarking and Memory System](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Integrated_Systems_Architecture/Lab6). Most of the exercises are already solved, so your task is to follow the steps, explain what you do, and justify the results you obtain.

## Exercise 3 (optional) - Adding new instructions in the VeeR EH1 core:
Use primarily the instructions provided in the video mentioned above and also, if you need more information, the document for Lab 18 of RVfpga (we recommend you to use the document provided both for the EH1 core and for the EL2 core, as some instructions are more up-to-date in the latter document). Do the tests both in RVfpga-ViDBo and on the board:
       * Integrate an FPU (Floating Point Unit) into the VeeR EH1 core, with support for addition, multiplication, and division. You can use the sources provided in the following link, which already provide the modified files: [SoC_Sources](https://drive.google.com/file/d/1199soZSgC8ZiqvnQjMRLNSkZAyRviOb5/view?usp=drive_link). Explain the differences versus the original SoC. Obtain the bitstream (in this case you can generate your own bitstream or use the one provided here: [SoC_FPU](https://drive.google.com/file/d/1DwSW22Nk8Ef6UOMWIHgC7AB96AzB-yJI/view?usp=drive_link)), as well as the simulator binary (in this case follow the instructions explained in the video to compile the simulator).
       * Test the implementation using a real algorithm. Use the Dot Product program provided in the following link: [DotProduct](https://drive.google.com/file/d/1FxCZzNDfhHamieTfrMSGTSZLJr-9cMYl/view?usp=drive_link)). First, understand the program, both the C and the assembly file. Then, execute the program both in simulation and on the board, and confirm that the results obtained for the dot product are correct. Finally, compare the performance obtained when executing the FP instructions using software emulation vs. hardware implementation.
       * (OPTIONAL) Upgrade the compiler to support the Zfinx extension following the instructions from this [Exercise 4](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Integrated_Systems_Architecture/Lab4#exercise-4).

## Exercise 4 (optional) - Other RISC-V cores:
In the following directory you can find some examples of other open RISC-V cores: [OtherRiscvCores](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/RVfpga_Microcredential/Module3/OtherRiscvCores)

