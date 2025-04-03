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
   * You can also practice on the exercises proposed in the following link, using the Ripes simulator: [ExamplesAndExercises_Ripes](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Fundamentals/RiscvProcessors).


**JUNE 20 SESSION:**

**To complete between June 23 and 26:**

**JUNE 27 SESSION:**
