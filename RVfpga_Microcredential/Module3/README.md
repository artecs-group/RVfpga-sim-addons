# Module 3 - VeeR EH1 and EL2 microarchitecture

## Module General Contents
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

## Module Workflow
Follow the next steps to analyze the VeeR EH1 processor, first at a high-level and then at a low-level.

**To complete between June 16 and 19:**

1. Review of the simple 5-stages pipelined processor:

   * Look at Chapter 7 (Microarchitecture) of the H&H book.
   * Look at the following slides, which describe the processor from the previous textbook: [Module7_FC2-Spanish](https://www.fdi.ucm.es/profesor/mendias/FC2/FC2tema7-imprimible.pdf) or [Module7_FC2-English](https://www.fdi.ucm.es/profesor/mendias/FC2/FC2module7.pdf).
   * You can also practice on the exercises proposed in the following link, using the Ripes simulator: [ExamplesAndExercises_RipesProcessors](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Fundamentals/RiscvProcessors).

3. Watch this video, which describes the VeeR EH1 microarchitecture in detail: [VeeReh1Video](https://youtu.be/xVnB6OM00cE?si=0HW333O-oPOXUDZG) (the video is in Spanish, but you can watch an AI-translated-to-English version of the video here [VeeReh1EnglishVideo](https://www.youtube.com/watch?v=Ow_0l47xqV4), you can watch an AI-translated-to-Chinese version of the video here [VeeReh1ChineseVideo](https://www.youtube.com/watch?v=2c4Iaswnz8w), or you can enable the subtitles in the original video). You can download the slides used in the video [here](https://drive.google.com/file/d/1rSlwCzcHD4F_S4YFLCFn3L0VNXH_sv7L/view?usp=drive_link).

4. Perform the following example and do the guided exercise:
   * [Use of RVfpga-Pipeline](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab2/VeeR#rvfpga-pipeline).
   * [Guided exercise VeeR EH1 microarchitecture](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab2/VeeR#exercise-1).

5. Then view, from time 0:0 to time 6:25, this video, which shows a description of the VeeR Performance Counters and an example using RVfpga-ViDBo: [PerformanceBenchmarkingVideo](https://youtu.be/GqaDEW3W4X0?si=yf1rObPveS-RB-We&t=10) (the video is in Spanish, but you can watch an AI-translated-to-English version of the video here: [PerformanceBenchmarkingEnglishVideo](https://youtu.be/DXB7jl1iGq8?si=GODI7vlY9WCXIMny&t=10), you can watch an AI-translated-to-Chinese version of the video here: [PerformanceBenchmarkingChineseVideo](https://youtu.be/d5-0sNLW7wg?si=6P5wM8ruumOQuSnD&t=10) or you can enable the subtitles in the video in Spanish) (you can download the [slides](https://drive.google.com/file/d/146nEyUkGkXn85cS15EiUM7R0Bv1nKyoT/view?usp=sharing)).

6. Perform the following guided exercise:
   * [Guided exercise HW Counters](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Integrated_Systems_Architecture/Lab3#exercise-1).


**JUNE 20 SESSION:**

7. Complete the following exercises:
   * To be provided.

<!--
   * Evaluate the performance of the VeeR EH1 core using RVfpga-Pipeline and the Nexys A7 board:
       - [Exercise-2](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab2/VeeR#exercise-3).
       - [Exercise-3](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Integrated_Systems_Architecture/Lab3#exercise-2).

   * Analyze the execution of basic instructions using RVfpga-Trace:
       - Analyze an add instruction: [Exercise-1](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Integrated_Systems_Architecture/Lab4#exercise-1).
       - Analyze a lw instruction and a beq instruction (Lab 13 and Lab 16 of RVfpga).
-->

**To complete between June 23 and 26:**

2. Review of the memory hierarchy:

   * Look at Chapter 8 (Memory Systems) of the H&H book.
   * You can also practice on the exercises proposed in the following link, using the Ripes simulator: [ExamplesAndExercises_RipesCache](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab3).

9. Then view the same video, from time 24:18 to the end, this video [PerformanceBenchmarkingVideo](https://youtu.be/GqaDEW3W4X0?si=yf1rObPveS-RB-We&t=1458) (the video is in Spanish, but you can watch an AI-translated-to-English version of the video here: [PerformanceBenchmarkingEnglishVideo](https://youtu.be/DXB7jl1iGq8?si=GODI7vlY9WCXIMny&t=1458), you can watch an AI-translated-to-Chinese version of the video here: [PerformanceBenchmarkingChineseVideo](https://youtu.be/d5-0sNLW7wg?si=6P5wM8ruumOQuSnD&t=1458) or you can enable the subtitles in the video in Spanish) (you can download the [slides](https://drive.google.com/file/d/146nEyUkGkXn85cS15EiUM7R0Bv1nKyoT/view?usp=sharing)). The video describes how to run the CoreMark benchmark on the RVfpga SoC.

8. View, from time 6:29 to time 24:18, this video [PerformanceBenchmarkingVideo](https://youtu.be/GqaDEW3W4X0?si=yf1rObPveS-RB-We&t=388) (the video is in Spanish, but you can watch an AI-translated-to-English version of the video here: [PerformanceBenchmarkingEnglishVideo](https://youtu.be/DXB7jl1iGq8?si=GODI7vlY9WCXIMny&t=388), you can watch an AI-translated-to-Chinese version of the video here: [PerformanceBenchmarkingChineseVideo](https://youtu.be/d5-0sNLW7wg?si=6P5wM8ruumOQuSnD&t=388) or you can enable the subtitles in the video in Spanish) (you can download the [slides](https://drive.google.com/file/d/146nEyUkGkXn85cS15EiUM7R0Bv1nKyoT/view?usp=sharing)). The video describes how to extend the VeeR EH1 processor with new instructions and how we can improve its peformance using them.

10. Update the C compiler using the following instructions: [CompilerUpdate](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Integrated_Systems_Architecture/Lab4#exercise-4).

11. Add simple test instruction: bitmanip.

**JUNE 27 SESSION:**

12. Complete the following exercises:
   * To be provided.

<!--
   * [Benchmarking and Memory System](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Integrated_Systems_Architecture/Lab6).

   * Final project (Lab 18 of RVfpga):
       - Add FPU.
       - Test with a real algorithm: Bisection.
       - Compare using Performance Counters.
-->
