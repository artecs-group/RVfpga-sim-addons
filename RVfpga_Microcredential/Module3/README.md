# Module 3 - VeeR EH1 and EL2 microarchitecture

## General Contents
In this module, we will move down to the microarchitectural level to analyze how the VeeR EL2 and VeeR EH1 processors operate internally.

We will begin by examining basic microarchitectural techniques: pipelining, execution of basic instructions (add, lw, etc.), hazards, and so on. In Topic 1, we start with a general analysis of the VeeR EL2 processor. First, we will explore the organization of the Verilog files that make up this core and examine the details of its pipeline stages. Then, we will learn how to use the performance counters available in this processor, which will be very useful for performance measurement later on. Finally, we will review how to configure the VeeR EL2 core.

In Topics 2 and 3, we will analyze the execution of Arithmetic-Logic instructions (add, sub, and, ...) and memory transfer instructions (load and store), respectively. The structure will be similar in both topics: a detailed explanation of one instruction of that type (add, lw) will be provided, followed by tasks in which students are asked to analyze other instructions of the same category.

Finally, in Topic 4, we will introduce the concept of hazards and explore an initial approach to dealing with them.

We will then shift our focus to the VeeR EH1 processor to explore advanced microarchitectural techniques: deep pipelining, superscalar execution, branch prediction, cache and scratchpad memories, extending the processor with new instructions, and more.

In Topic 5, we begin a general analysis of the VeeR EH1 processor and examine the main differences compared to the processor studied in the previous module, the VeeR EL2. Specifically, we will study the performance benefits and key design challenges (such as handling data hazards) that arise when moving from a 4-stage to a 9-stage pipeline. Additionally, we will explore the configuration options available for this processor.

In Topic 6, we will analyze superscalar execution in the VeeR EH1 processor and compare performance differences as the superscalar width increases. We will also examine how different types of structural hazards are handled.

Topic 7 will focus on conditional and unconditional branch instructions (beq, j, ...) and branch predictors. We will study how instructions are fetched predictively and how mispredictions are resolved. Performance measurements will be carried out for different processor configurations.

In Topic 8, we will explore how to add new instructions to the VeeR processors. This will enable us to incorporate a Floating-Point Unit into the processor, which we will use to compare the performance of floating-point algorithms executed via hardware versus software emulation.

Finally, in Topic 9, we will study the memory hierarchy, focusing on two key components: the instruction cache and the data scratchpad.

## Workflow
Follow the next steps to analyze the VeeR processors, first at a high-level and then at a low-level.

### To complete between June 23 and 26:

1. Review of the simple 5-stages pipelined processor:

   * Look at Chapter 7 (Microarchitecture) of the [H&H book](https://www.amazon.es/Digital-Design-Computer-Architecture-RISC-V/dp/0128200642).
   * Look at the following slides, which describe the processor from the previous textbook: [Module7_FC2-Spanish](https://www.fdi.ucm.es/profesor/mendias/FC2/FC2tema7-imprimible.pdf) or [Module7_FC2-English](https://www.fdi.ucm.es/profesor/mendias/FC2/FC2module7.pdf).
   * You can also practice on the exercises proposed in the following link, using the Ripes simulator: [ExamplesAndExercises_RipesProcessors](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Fundamentals/RiscvProcessors).

2. Watch this video, which describes the VeeR EH1 microarchitecture in detail: [VeeReh1Video](https://youtu.be/xVnB6OM00cE?si=0HW333O-oPOXUDZG) (the video is in Spanish, but you can watch an AI-translated-to-English version of the video here [VeeReh1EnglishVideo](https://www.youtube.com/watch?v=Ow_0l47xqV4), you can watch an AI-translated-to-Chinese version of the video here [VeeReh1ChineseVideo](https://www.youtube.com/watch?v=2c4Iaswnz8w), or you can enable the subtitles in the original video). You can download the slides used in the video [here](https://drive.google.com/file/d/1rSlwCzcHD4F_S4YFLCFn3L0VNXH_sv7L/view?usp=drive_link).

3. Perform the following guided example and solved exercise, which analyze the VeeR EH1 microarchitecture analyzed in the previous item:
   * [Use of RVfpga-Pipeline](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab2/VeeR#rvfpga-pipeline) (steps 1 to 10).
   * [Exercise VeeR EH1 microarchitecture](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab2/VeeR#exercise-1) (First exercise - note that the solution is shown after the exercise statement).

4. Then view, from time 0:0 to time 6:25, this video, which shows a description of the VeeR Performance Counters and an example using RVfpga-ViDBo: [PerformanceBenchmarkingVideo](https://youtu.be/GqaDEW3W4X0?si=yf1rObPveS-RB-We&t=10) (the video is in Spanish, but you can watch an AI-translated-to-English version of the video here: [PerformanceBenchmarkingEnglishVideo](https://youtu.be/DXB7jl1iGq8?si=GODI7vlY9WCXIMny&t=10), you can watch an AI-translated-to-Chinese version of the video here: [PerformanceBenchmarkingChineseVideo](https://youtu.be/d5-0sNLW7wg?si=6P5wM8ruumOQuSnD&t=10) or you can enable the subtitles in the video in Spanish) (you can download the [slides](https://drive.google.com/file/d/146nEyUkGkXn85cS15EiUM7R0Bv1nKyoT/view?usp=sharing)).

5. Finally, test on the board the exercise shown in the video from the previous item: [Guided exercise HW Counters](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Integrated_Systems_Architecture/Lab3#exercise-1) (first exercise).

6. In case you need it, you can find more details about the VeeR EH1/EL2 microarchitecture in Labs 11 to 17 of the full RVfpga package.


### JUNE 27 SESSION:

7. Complete the following exercises:
<!--
-->
   * Evaluate the performance of the VeeR EH1 core and the VeeR EL2 core for the following program, first using RVfpga-Pipeline and then running on the Nexys A7 board. Compare the results and explain the differences:
       - [Exercise-RVfpgaPipeline_EH1](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab2/VeeR#exercise-3) (third exercise). You must resolve the exercise in a similar way as [Exercise VeeR EH1 microarchitecture](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab2/VeeR#exercise-1) (first exercise).
       - [Exercise-HwCounters_EH1](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Integrated_Systems_Architecture/Lab3#exercise-2) (second exercise).
       - (OPTIONAL) [Exercise-HwCounters-EL2](https://github.com/artecs-group/RVfpga-sim-addons/blob/main/Integrated_Systems_Architecture/Lab3/README.md#exercise-2---extension-for-veer-el2) (extension of the second exercise).

   * Analyze the execution of basic instructions using RVfpga-Trace:
       - Analyze an add instruction: [Exercise-1](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Integrated_Systems_Architecture/Lab4#exercise-1) (first exercise) in the VeeR EH1 core.
       - (OPTIONAL) Analyze a lw instruction (Section 2 of Lab 13 of RVfpga) and a beq instruction (Section 2 of Lab 16 of RVfpga) in the VeeR EH1 core.

### To complete between June 30 and July 3:

8. Review of the memory hierarchy:

   * Look at Chapter 8 (Memory Systems) of the H&H book.
   * You can also practice with the exercises proposed in the following link, using the Ripes simulator: [ExamplesAndExercises_RipesCache](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab3).

9. View, from time 24:18 to the end, this video: [PerformanceBenchmarkingVideo](https://youtu.be/GqaDEW3W4X0?si=yf1rObPveS-RB-We&t=1458) (the video is in Spanish, but you can watch an AI-translated-to-English version of the video here: [PerformanceBenchmarkingEnglishVideo](https://youtu.be/DXB7jl1iGq8?si=GODI7vlY9WCXIMny&t=1458), you can watch an AI-translated-to-Chinese version of the video here: [PerformanceBenchmarkingChineseVideo](https://youtu.be/d5-0sNLW7wg?si=6P5wM8ruumOQuSnD&t=1458) or you can enable the subtitles in the video in Spanish) (you can download the [slides](https://drive.google.com/file/d/146nEyUkGkXn85cS15EiUM7R0Bv1nKyoT/view?usp=sharing)). The video describes how to run the CoreMark benchmark on the RVfpga SoC.

10. Then view the same video from the previous item, but now from time 6:29 to time 24:18: [PerformanceBenchmarkingVideo](https://youtu.be/GqaDEW3W4X0?si=yf1rObPveS-RB-We&t=388) (the video is in Spanish, but you can watch an AI-translated-to-English version of the video here: [PerformanceBenchmarkingEnglishVideo](https://youtu.be/DXB7jl1iGq8?si=GODI7vlY9WCXIMny&t=388), you can watch an AI-translated-to-Chinese version of the video here: [PerformanceBenchmarkingChineseVideo](https://youtu.be/d5-0sNLW7wg?si=6P5wM8ruumOQuSnD&t=388) or you can enable the subtitles in the video in Spanish) (you can download the [slides](https://drive.google.com/file/d/146nEyUkGkXn85cS15EiUM7R0Bv1nKyoT/view?usp=sharing)). The video describes how to extend the VeeR EH1 processor with new instructions and how we can improve its peformance using them.

11. You can find more details about the VeeR EH1/EL2 memory system and how to add new instructions in Labs 18 to 20 of the full RVfpga package. You can also find the solutions to most of these exercises at ```RVfpgaEH1/RVfpga/Labs/RVfpgaLabsSolutions/Modified_RVfpgaSystem```.


### JULY 4 SESSION:

12. Complete the exercises proposed in the following link (Exercise 4 is optional): [Benchmarking and Memory System](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Integrated_Systems_Architecture/Lab6). Most of the exercises are already solved, so your task is to follow the steps, explain what you do, and justify the results you obtain.

<!--
   * Add a new instruction from the bitmanip extension ([BitManip1](https://github.com/riscv/riscv-bitmanip), [BitManip2](https://five-embeddev.com/riscv-bitmanip/1.0.0/bitmanip.html)) to the VeeR EH1 core. You can follow the instructions explained in Lab 18 of RVfpga.
-->

13. Adding new instructions in the VeeR EH1 core: Use primarily the instructions provided in the video mentioned above and also, if you need more information, the document for Lab 18 of RVfpga (we recommend you to use the document provided both for the EH1 core and for the EL2 core, as some instructions are more up-to-date in the latter document). Do the tests both in RVfpga-ViDBo and on the board:
       * Integrate an FPU (Floating Point Unit) into the VeeR EH1 core, with support for addition, multiplication, and division. You can use the sources provided in the following link, which already provide the modified files: [SoC_Sources](https://drive.google.com/file/d/1199soZSgC8ZiqvnQjMRLNSkZAyRviOb5/view?usp=drive_link). Explain the differences versus the original SoC. Obtain the bitstream (in this case you can generate your own bitstream or use the one provided here: [SoC_FPU](https://drive.google.com/file/d/1DwSW22Nk8Ef6UOMWIHgC7AB96AzB-yJI/view?usp=drive_link)), as well as the simulator binary (in this case follow the instructions explained in the video to compile the simulator).
       * Test the implementation using a real algorithm. Use the Dot Product program provided in the following link: [DotProduct](https://drive.google.com/file/d/1FxCZzNDfhHamieTfrMSGTSZLJr-9cMYl/view?usp=drive_link)). First, understand the program, both the C and the assembly file. Then, execute the program both in simulation and on the board, and confirm that the results obtained for the dot product are correct. Finally, compare the performance obtained when executing the FP instructions using software emulation vs. hardware implementation.
       * (OPTIONAL) Upgrade the compiler to support the Zfinx extension following the instructions from this [Exercise 4](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Integrated_Systems_Architecture/Lab4#exercise-4).

14. (OPTIONAL) Other RISC-V cores: In the following directory you can find some examples of other open RISC-V cores: [OtherRiscvCores](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/RVfpga_Microcredential/Module3/OtherRiscvCores)
