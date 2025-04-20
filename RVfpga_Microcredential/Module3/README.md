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

**To complete between June 16 and 19:**

1. Review of the simple 5-stages pipelined processor:

   * Look at Chapter 7 (Microarchitecture) of the H&H book.
   * Look at the following slides, which describe the processor from the previous textbook: [Module7_FC2-Spanish](https://www.fdi.ucm.es/profesor/mendias/FC2/FC2tema7-imprimible.pdf) or [Module7_FC2-English](https://www.fdi.ucm.es/profesor/mendias/FC2/FC2module7.pdf).
   * You can also practice on the exercises proposed in the following link, using the Ripes simulator: [ExamplesAndExercises_RipesProcessors](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Fundamentals/RiscvProcessors).

2. Watch this video, which describes the VeeR EH1 microarchitecture in detail: [VeeReh1Video](https://youtu.be/xVnB6OM00cE?si=0HW333O-oPOXUDZG) (the video is in Spanish, but you can watch an AI-translated-to-English version of the video here [VeeReh1EnglishVideo](https://www.youtube.com/watch?v=Ow_0l47xqV4), you can watch an AI-translated-to-Chinese version of the video here [VeeReh1ChineseVideo](https://www.youtube.com/watch?v=2c4Iaswnz8w), or you can enable the subtitles in the original video). You can download the slides used in the video [here](https://drive.google.com/file/d/1rSlwCzcHD4F_S4YFLCFn3L0VNXH_sv7L/view?usp=drive_link).

3. Perform the following guided example and solved exercise, which analyze the VeeR EH1 microarchitecture analyzed in the previous item:
   * [Use of RVfpga-Pipeline](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab2/VeeR#rvfpga-pipeline) (steps 1 to 10).
   * [Exercise VeeR EH1 microarchitecture](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab2/VeeR#exercise-1) (first exercise).

4. Then view, from time 0:0 to time 6:25, this video, which shows a description of the VeeR Performance Counters and an example using RVfpga-ViDBo: [PerformanceBenchmarkingVideo](https://youtu.be/GqaDEW3W4X0?si=yf1rObPveS-RB-We&t=10) (the video is in Spanish, but you can watch an AI-translated-to-English version of the video here: [PerformanceBenchmarkingEnglishVideo](https://youtu.be/DXB7jl1iGq8?si=GODI7vlY9WCXIMny&t=10), you can watch an AI-translated-to-Chinese version of the video here: [PerformanceBenchmarkingChineseVideo](https://youtu.be/d5-0sNLW7wg?si=6P5wM8ruumOQuSnD&t=10) or you can enable the subtitles in the video in Spanish) (you can download the [slides](https://drive.google.com/file/d/146nEyUkGkXn85cS15EiUM7R0Bv1nKyoT/view?usp=sharing)).

5. Finally, test on the board the exercise shown in the video from the previous item: [Guided exercise HW Counters](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Integrated_Systems_Architecture/Lab3#exercise-1) (first exercise).


**JUNE 20 SESSION:**

6. Complete the following exercises:
   * To be provided.

<!--
   * Evaluate the performance of the VeeR EH1 core and the VeeR EL2 core for the following program, first using RVfpga-Pipeline and then running on the Nexys A7 board. Compare the results and explain the differences:
       - [Exercise-RVfpgaPipeline_EH1](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab2/VeeR#exercise-3) (third exercise).
       - [Exercise-HwCounters_EH1](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Integrated_Systems_Architecture/Lab3#exercise-2) (second exercise).
       - [Exercise-HwCounters-EL2](https://github.com/artecs-group/RVfpga-sim-addons/blob/main/Integrated_Systems_Architecture/Lab3/README.md#exercise-2---extension-for-veer-el2) (extension of the second exercise).

   * Analyze the execution of basic instructions using RVfpga-Trace:
       - Analyze an add instruction: [Exercise-1](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Integrated_Systems_Architecture/Lab4#exercise-1) (first exercise) in the VeeR EH1 core.
       - Analyze a lw instruction (Section 2 of Lab 13 of RVfpga) and a beq instruction (Section 2 of Lab 16 of RVfpga) in the VeeR EH1 core.
-->

**To complete between June 23 and 26:**

7. Review of the memory hierarchy:

   * Look at Chapter 8 (Memory Systems) of the H&H book.
   * You can also practice with the exercises proposed in the following link, using the Ripes simulator: [ExamplesAndExercises_RipesCache](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab3).

8. View, from time 24:18 to the end, this video: [PerformanceBenchmarkingVideo](https://youtu.be/GqaDEW3W4X0?si=yf1rObPveS-RB-We&t=1458) (the video is in Spanish, but you can watch an AI-translated-to-English version of the video here: [PerformanceBenchmarkingEnglishVideo](https://youtu.be/DXB7jl1iGq8?si=GODI7vlY9WCXIMny&t=1458), you can watch an AI-translated-to-Chinese version of the video here: [PerformanceBenchmarkingChineseVideo](https://youtu.be/d5-0sNLW7wg?si=6P5wM8ruumOQuSnD&t=1458) or you can enable the subtitles in the video in Spanish) (you can download the [slides](https://drive.google.com/file/d/146nEyUkGkXn85cS15EiUM7R0Bv1nKyoT/view?usp=sharing)). The video describes how to run the CoreMark benchmark on the RVfpga SoC.

9. Then view the same video from the previous item, but now from time 6:29 to time 24:18: [PerformanceBenchmarkingVideo](https://youtu.be/GqaDEW3W4X0?si=yf1rObPveS-RB-We&t=388) (the video is in Spanish, but you can watch an AI-translated-to-English version of the video here: [PerformanceBenchmarkingEnglishVideo](https://youtu.be/DXB7jl1iGq8?si=GODI7vlY9WCXIMny&t=388), you can watch an AI-translated-to-Chinese version of the video here: [PerformanceBenchmarkingChineseVideo](https://youtu.be/d5-0sNLW7wg?si=6P5wM8ruumOQuSnD&t=388) or you can enable the subtitles in the video in Spanish) (you can download the [slides](https://drive.google.com/file/d/146nEyUkGkXn85cS15EiUM7R0Bv1nKyoT/view?usp=sharing)). The video describes how to extend the VeeR EH1 processor with new instructions and how we can improve its peformance using them.

**JUNE 27 SESSION:**

10. Complete the following exercises:
   * To be provided.

<!--
   * [Benchmarking and Memory System](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Integrated_Systems_Architecture/Lab6).

   * Add a new instruction from the bitmanip extension ([BitManip1](https://github.com/riscv/riscv-bitmanip), [BitManip2](https://five-embeddev.com/riscv-bitmanip/1.0.0/bitmanip.html)) to the VeeR EH1 core. You can follow the instructions explained in Lab 18 of RVfpga (you should add the instruction to the EH1 core, but some of the instructions for the EL2 core are more up-to-date).

   * Final project:
       - Integrate an FPU (Floating Point Unit) into the VeeR EH1 core, with support for addition, multiplication, and division.
       - Test the implementation using a real algorithm; for example, the Bisection method for finding the roots of a function.
       - Use Performance Counters to compare the emulation of floating-point operations versus their hardware implementation.

   * Other RISC-V cores: In the following directory you can find some examples of other open RISC-V cores: [OtherRiscvCores]()

-->
