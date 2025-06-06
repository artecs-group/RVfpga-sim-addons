# Module 0 - Introduction and Installation
This lab aims to prepare our computer to work in the labs of the course and to introduce the RVfpga System and the Tools that we will use in the labs.

The [RISC-V FPGA](https://university.imgtec.com/rvfpga-el2-v3-0-english-downloads-page/) (RVfpga) course in computer architecture is a freely available course that provides hands-on understanding of a commercial RISC-V processor, a RISC-V system-on-chip (SoC), and the RISC-V ecosystem. These materials bridge the gap between the availability of the open RISC-V ISA and actually being able to use and experiment with a commercial RISC-V processor/SoC and the RISC-V toolchain. In addition to providing the VeeR EH1/EL2-based SoC source code in Verilog/SystemVerilog, RVfpga shows how to install and use the RISC-V toolchain to compile, debug, and run C and RISC-V assembly programs on the SoC, use and modify the I/O System, and understand and modify the SoC microarchitecture and memory hiearchy. A second package, the [RVfpga-SoC](https://university.imgtec.com/rvfpgasoc-download-page-en/) course, is a short follow-on course to RVfpga that shows how to build a RISC-V SoC from scratch using building blocks and then run the Zephyr real-time operating system (RTOS) on it. The RVfpga courses can be completed in simulation only or, optionally, also in hardware on an FPGA. All software and simulation tools are freely available. Provided simulation tools include a waveform viewer, a virtual FPGA board, and a pipeline viewer. The courses also show how to optionally target the RISC-V SoC to a range of FPGA boards, from lower-cost boards, such as the Basys 3 or Boolean board, to more expensive FPGA boards, such as the Nexys A7 FPGA board.

To understand RVfpga and start using it, you can follow the next steps:

- Watch this video: [IntroductionRVfpgaVideo](https://www.youtube.com/watch?v=sc_Jn0XSkNw) (the video is in Spanish, but you can watch an AI-translated-to-English version of the video here [IntroductionRVfpgaEnglishVideo](https://www.youtube.com/watch?v=cO3UAbT09es), you can watch an AI-translated-to-Chinese version of the video here [IntroductionRVfpgaChineseVideo](https://www.youtube.com/watch?v=F-1Q-59s84s)). You can obtain the slides used in the video here: [IntroSlides](https://drive.google.com/file/d/17Kid-KSDqPOPoEudiWhcuOdUChYpkcbp/view?usp=drive_link).

- Install the environment and test the RVfpga tools. Follow the instructions in the document [Practice_Familiarization_fpga](https://drive.google.com/file/d/1IyeinlVZMmjAOQFoq8BYQIQapDQ6AWra/view?usp=drive_link). Each section includes a link to a video illustrating its content. It is not necessary to complete the tasks proposed in the document.
  - Install Virtual Machine (VM)
  - Download RVfpga Sources in the VM
  - Test `RVfpga-Pipeline`
  - Test `RVfpga-ViDBo`
  - Test `RVfpga-Nexys` (do this section only if you have the board)
  - Test `RVfpga-Trace`
  - Test `RVfpga-Whisper`

**IMPORTANT NOTE**: The videos in the course reference a different directory for the RVfpga sources than the one used in this course; specifically, whenever directory `RVfpga_MasterUCLM/` is mentioned, you should instead refer to directory `Simuladores_EC_24-25/RVfpga/`.

- Download a second set of sources that we will also use in the course. Specifically, from inside the VM, download the following file and unzip it in the VM home directory: [RVfpgaSources_v2](https://drive.google.com/file/d/1hbCSFmjIoGmXq4r5G12_AMUKezHXA6A-/view?usp=sharing).

- Download the two RVfpga packages from these links: [RISC-V FPGA](https://university.imgtec.com/rvfpga-el2-v3-0-english-downloads-page/) and [RVfpga-SoC](https://university.imgtec.com/rvfpgasoc-download-page-en/). While most of the required source files will be provided during the exercises, these packages are useful as reference material and may contain additional documentation and resources that you might find helpful.
