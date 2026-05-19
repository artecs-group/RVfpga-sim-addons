## General Contents

In this module, students will explore the internal microarchitecture of the VeeR EH1 (and EL2 in less detail) RISC-V processor. The activities focus on understanding pipelined execution, superscalar architectures, performance evaluation, and memory hierarchy concepts.

Students will analyze instruction execution using RVfpga visualization and tracing tools, evaluate processor performance through hardware counters and benchmarks, and study how architectural features such as branch prediction, caches, and custom instructions affect performance. The module also includes practical exercises extending the processor with floating-point hardware support and comparing hardware versus software execution of floating-point algorithms.

---

## Previous work to complete between June 1 and 11:

1. Review of the simple 5-stages pipelined processor:

   * You can look at Chapter 7 (Microarchitecture) of the [H&H book](https://www.amazon.es/Digital-Design-Computer-Architecture-RISC-V/dp/0128200642), which explains the basic concepts of different RISCV-based processor implementations.
   * Look at the following slides, which describe the processor from the previous textbook: [Module7_FC2-Spanish](https://www.fdi.ucm.es/profesor/mendias/FC2/FC2tema7-imprimible.pdf) or [Module7_FC2-English](https://www.fdi.ucm.es/profesor/mendias/FC2/FC2module7.pdf).

2. Watch this video, which describes the VeeR EH1 microarchitecture in detail: [VeeReh1Video](https://youtu.be/xVnB6OM00cE?si=0HW333O-oPOXUDZG) (the video is in Spanish, but you can watch an AI-translated-to-English version of the video here [VeeReh1EnglishVideo](https://www.youtube.com/watch?v=Ow_0l47xqV4), you can watch an AI-translated-to-Chinese version of the video here [VeeReh1ChineseVideo](https://www.youtube.com/watch?v=2c4Iaswnz8w), or you can enable the subtitles in the original video). You can download the slides used in the video [here](https://drive.google.com/file/d/1rSlwCzcHD4F_S4YFLCFn3L0VNXH_sv7L/view?usp=drive_link).

3. Perform the following guided example and solved exercise, which analyze the VeeR EH1 microarchitecture analyzed in the previous item:
   * [Use of RVfpga-Pipeline](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab2/VeeR#rvfpga-pipeline) (steps 1 to 10).
   * [Exercise VeeR EH1 microarchitecture](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab2/VeeR#exercise-1) (First exercise - note that the solution is shown after the exercise statement).

4. Then view, from time 0:0 to time 6:25, this video, which shows a description of the VeeR Performance Counters and an example using RVfpga-ViDBo: [PerformanceBenchmarkingVideo](https://youtu.be/GqaDEW3W4X0?si=yf1rObPveS-RB-We&t=10) (the video is in Spanish, but you can watch an AI-translated-to-English version of the video here: [PerformanceBenchmarkingEnglishVideo](https://youtu.be/DXB7jl1iGq8?si=GODI7vlY9WCXIMny&t=10), you can watch an AI-translated-to-Chinese version of the video here: [PerformanceBenchmarkingChineseVideo](https://youtu.be/d5-0sNLW7wg?si=6P5wM8ruumOQuSnD&t=10) or you can enable the subtitles in the video in Spanish) (you can download the [slides](https://drive.google.com/file/d/146nEyUkGkXn85cS15EiUM7R0Bv1nKyoT/view?usp=sharing)).

5. Finally, test on the board the exercise shown in the video from the previous item: [Guided exercise HW Counters](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Integrated_Systems_Architecture/Lab3#exercise-1) (first exercise).

6. In case you need it, you can find more details about the VeeR EH1/EL2 microarchitecture in Labs 11 to 17 of the full RVfpga package.

