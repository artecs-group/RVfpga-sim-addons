# Week 5

This part of the course introduces students to the design and analysis of open-hardware microcontrollers through the RVfpga educational platform. The main objective is to understand how a modern RISC-V processor is organized internally, how it interacts with peripheral devices, and how its performance can be evaluated.

During this week, students will first complete a set of online learning activities and then attend an in-person laboratory session, combining theoretical study with guided exercises and hands-on experimentation.

- [Online theory and tasks](https://github.com/artecs-group/RVfpga-sim-addons/blob/main/Design_Microcontrollers_Open_Hardware_25-26/Week5/README.md#online-theory-and-tasks-december-8th-to-december-11th) (December 8 – 11, 2025): Work through the online materials, watch the instructional videos, and complete the guided exercises to become familiar with the RVfpga environment and the VeeR EH1/EL2 processor cores.

- [In-person practice](https://github.com/artecs-group/RVfpga-sim-addons/blob/main/Design_Microcontrollers_Open_Hardware_25-26/Week5/README.md#in-person-practice-december-12th) (December 12, 2025): Apply the knowledge acquired during the week to complete a set of practical exercises in the lab, using the RVfpga simulator and, when available, the FPGA board.

## ONLINE THEORY AND TASKS (December 8th to December 11th)

This stage focuses on the online component of the course, where you will explore the RVfpga platform and the VeeR EH1 and EL2 cores. The provided materials include short videos and guided exercises that explain the internal organization of the RVfpga SoC, its input/output subsystems, and performance-evaluation methods. Completing these activities before Friday’s lab is essential, as they provide the theoretical and practical foundation required for the in-person work.

Two types of tasks are included: Mandatory and Optional. Mandatory tasks cover the core concepts needed for the compulsory exercises in the lab, while optional ones address more advanced topics for those wishing to go deeper or improve their final grade. If your time is limited, focus on the mandatory tasks first.

Take the time to follow the videos and exercises carefully. There are no submissions during the week, but you are expected to attend the lab session well prepared and ready to apply what you have learned. Working steadily throughout the week will help you make the most of the lab and strengthen your understanding of the course as a whole.

### 1. **Introduction to RVfpga**
  - Watch this video: [IntroductionRVfpgaVideo](https://www.youtube.com/watch?v=sc_Jn0XSkNw). You can obtain the slides used in the video here: [IntroSlides](https://drive.google.com/file/d/17Kid-KSDqPOPoEudiWhcuOdUChYpkcbp/view?usp=drive_link.
  - Install the environment and test tools. Follow the instructions in the document [Practice_Familiarization_fpga](https://drive.google.com/file/d/1vdLf39U89q38gmLuodo7nZkctRqeAiyO/view?usp=drive_link). Each section includes a link to a video illustrating its content.
    - Install Virtual Machine (VM)
    - Download RVfpga Sources in the VM
    - Test `RVfpga-Pipeline` and complete the task
    - Test `RVfpga-Trace` and complete the task
    - Test `RVfpga-ViDBo`
    - Test `RVfpga-Nexys` (only if you have the board)
    - Test `RVfpga-Whisper`

### 2. **Input/Output in RVfpga**
  - Watch this video: [InputOutputVideo](https://www.youtube.com/watch?v=8fK-CoEbo0Y). The video describes the RVfpga I/O System in detail. You can obtain the slides used in the video here: [IOSlides](https://drive.google.com/file/d/1-Kav6TLV5xBURQYfZfRP3yzWUq_Qp7eV/view?usp=drive_link)
  - Complete: [Tasks_InputOutput](https://drive.google.com/file/d/1-rVKByx-tePY05oWAjKyeDu75Ch20iKc/view?usp=sharing)

### 3. **VeeR EH1 and EL2 Cores**
  - Watch this video: [VeeReh1Video](https://youtu.be/xVnB6OM00cE?si=0HW333O-oPOXUDZG). The video describes the VeeR EH1 microarchitecture in detail. You can obtain the slides used in the video here: [EH1Slides](https://drive.google.com/file/d/1kIMQY3u5jZB7cAktFPqIHSpHAuruENAM/view?usp=drive_link)
  - Analyze the hazards explained in the video using the code provided here: [Tasks_VeeR](https://drive.google.com/file/d/1NSOsgaQnFWfeKJbu6r6319T3zq0wzgf-/view?usp=sharing)). You can also use the following table, which illustrates the forwarding paths available in the VeeR EH1 processor: [FwdPen_EH1](https://drive.google.com/file/d/1owNZUEw-2AZw2-El_mBu4-WpZ1HhYVNo/view?usp=sharing).

### 4. **Performance Evaluation in RVfpga**
  - Watch this video: [PerformanceBenchmarkingVideo](https://www.youtube.com/watch?v=GqaDEW3W4X0). You can obtain the slides used in the video here: [PerformanceSlides](https://drive.google.com/file/d/1xCmc4vFd_khLk6En14Ae_ZDF-OiP1QNm/view?usp=drive_link)
  - Complete: [Tasks_Performance](https://drive.google.com/file/d/1J8XczS0iMb5ttKyKPtDbZiwAkewIovVT/view?usp=sharing)

---

## IN-PERSON PRACTICE (December 12th)

The in-person session will be held on Friday, December 12th. You will put into practice the concepts studied during the week through several hands-on exercises on I/O systems, the VeeR EH1/EL2 cores, and performance evaluation within the RVfpga SoC.

At the end of the session, you will submit a brief report summarizing your results. This report may include screenshots from the simulator or FPGA executions, your developed code, and explanations of the obtained results. A few days later, you will deliver an extended version including any exercises not completed during the lab.

This session consolidates the knowledge gained during the online phase and provides direct experience in analyzing and experimenting with open-hardware microcontroller designs.

### 1. **Input/Output in RVfpga**: 
Complete the exercises from the following document: [Practice_IO]()

### 2. **VeeR EH1 and EL2 Cores**: 
Complete the exercises from the following document: [Practice_VeerEH1]()

### 3. **Performance Evaluation in RVfpga**: 
Complete the exercises from the following document: [Practice_Performance]()

