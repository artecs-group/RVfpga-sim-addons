# Integrated Systems Architecture

This is a fourth-year course in the Electronics and Communication Engineering degree program offered at UCM. You can see the contents of this course at [Integrated Systems Architecture UCM](https://fisicas.ucm.es/data/cont/docs/18-2021-09-01-2021-22%20Gu%C3%ADa%20Docente%20GIEC%20v1.1-157-16091.pdf). 

***NOTE: This course will be conducted during the second semester of the 2024-2025 academic year (February 2025 to May 2025). During this time, the course materials will continue to be refined and enhanced.***

The course starts with an introduction to the most recent trends in computer architecture, and then it explores exhaustively advanced processor design (deep pipelining, multi-cycle operations, speculative execution and branch prediction), the memory system (memory hierarchy, scratchpad memories), the I/O system, benchmarking and SoC design.

The course includes ten labs (some of them are identical to the labs used in the [Computer Organization](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization) course):

+ [Lab 0](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab0): Installation and Introduction.
+ [Lab 1](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab1): The RISC-V ISA.
+ [Lab 2](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab2): Introduction to the VeeR EH1 core.
+ [Lab 3](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Integrated_Systems_Architecture/Lab3): Performance counters, new instructions and benchmark execution on the VeeR EH1 core.
+ Lab 4: Execution of basic instructions on the VeeR EH1 core. (*COMING SOON*)
+ [Lab 5](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab3): The Memory Hierarchy in Ripes.
+ Lab 6: The Memory Hierarchy in VeeR EH1. (*COMING SOON*)
+ [Lab 7](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab4): High-level Input/Output on the RVfpga SoC.
+ [Lab 8](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Integrated_Systems_Architecture/Lab8): Low-level Input/Output on the RVfpga SoC.
+ Lab 9: The [RVfpga-SoC package](https://university.imgtec.com/rvfpgasoc-download-page-en/). (*COMING SOON*)

Students in this course are provided with a Nexys A7 board per person that they can keep until the end of the semester. The VeeR EH1 core fits in this board and it is a more advanced processor than EL2, that allows us to explore concepts such as deep pipelining or multi-cycle operations, thus it is the core that we use in the course. Anyway, most exercises can also be completed in the two other boards supported (Boolean and Basys 3), in this case using the samaller EL2 VeeR core. All instructions not provided in this repository can be found in the complete [RVfpga](https://university.imgtec.com/rvfpga-el2-v3-0-english-downloads-page/) course.

In case you do not have an FPGA board, all exercises can also be completed using the different simulation tools available in RVfpga: Whisper, RVfpga-ViDBo, RVfpga-Pipeline and RVfpga-Trace.

*NOTE: In case you want to obtain more information about this course (such as the slides, the exercises sheets, the solutions for the labs, etc.), you can contact ```dani02@ucm.es```*
