# Design of Microcontrollers in Open Hardware

From December 9 to December 20, 2024, we taught a module based on RVfpga in the course Diseño de Microcontroladores en Hardware Abierto, part of the [Master de Formación Permanente en Sistemas Microelectrónicos Basados en Arquitecturas Abiertas](https://www.uclm.es/estudios/propios/master-formacion-permanente-sistemas-microelectricos-basados-arquitecturas-abiertas) at the University of Castilla-La Mancha (UCLM). This master's program combines both online and in-person activities. 

Specifically, in the seventh module of the course (*RISC-Vfpga: cores VeeR EH1 y EL2, E/S y evaluacion*), we delivered 12 online hours featuring video lectures and tasks for students to complete using simulators. Additionally, we conducted six in-person hours focused on hands-on exercises with the Nexys A7 board. Below is the schedule, where you can access the course materials.

### ONLINE INTRODUCTION (2 hours)
- Watch this video: [IntroductionRVfpgaVideo](https://www.youtube.com/watch?v=sc_Jn0XSkNw) (the video is in Spanish, but you can watch an AI-translated-to-English version of the video here [IntroductionRVfpgaEnglishVideo](https://www.youtube.com/watch?v=cO3UAbT09es), you can watch an AI-translated-to-Chinese version of the video here [IntroductionRVfpgaChineseVideo](https://www.youtube.com/watch?v=F-1Q-59s84s)). You can obtain the slides used in the video here: [IntroSlides](https://drive.google.com/file/d/17Kid-KSDqPOPoEudiWhcuOdUChYpkcbp/view?usp=drive_link).
- Install the environment and test tools. Follow the instructions in the document [Practice_Familiarization_fpga](https://drive.google.com/file/d/1IyeinlVZMmjAOQFoq8BYQIQapDQ6AWra/view?usp=drive_link). Each section includes a link to a video illustrating its content.
  - Install Virtual Machine (VM)
  - Download RVfpga Sources in the VM
  - Test `RVfpga-Pipeline` and complete the task
  - Test `RVfpga-Trace` and complete the task
  - Test `RVfpga-ViDBo`
  - Test `RVfpga-Nexys` (only if you have the board)
  - Test `RVfpga-Whisper`

### ONLINE THEORY AND TASKS (10 hours)
- **Input/Output in RVfpga**
  - Watch this video: [InputOutputVideo](https://www.youtube.com/watch?v=8fK-CoEbo0Y) (the video is in Spanish, but you can watch an AI-translated-to-English version of the video here: [InputOutputEnglishVideo](https://www.youtube.com/watch?v=oIRFxQEBNAc) or you can watch an AI-translated-to-Chinese version of the video here: [InputOutputChineseVideo](https://www.youtube.com/watch?v=gG0HSeJ9ew8)). The video describes the RVfpga I/O System in detail. You can obtain the slides used in the video here: [IOSlides](https://drive.google.com/file/d/1-Kav6TLV5xBURQYfZfRP3yzWUq_Qp7eV/view?usp=drive_link))
  - Complete: [Tasks_InputOutput](https://drive.google.com/file/d/1FX5Fr63ecMRLswCPk606GWZr7z65b1Fp/view?usp=drive_link)
- **VeeR EH1 and EL2 Cores**
  - Watch this video: [VeeReh1Video](https://youtu.be/xVnB6OM00cE?si=0HW333O-oPOXUDZG) (the video is in Spanish, but you can watch an AI-translated-to-English version of the video here [VeeReh1EnglishVideo](https://www.youtube.com/watch?v=Ow_0l47xqV4) or you can watch an AI-translated-to-Chinese version of the video here [VeeReh1ChineseVideo](https://www.youtube.com/watch?v=2c4Iaswnz8w)). The video describes the VeeR EH1 microarchitecture in detail. You can obtain the slides used in the video here: [EH1Slides](https://drive.google.com/file/d/1kIMQY3u5jZB7cAktFPqIHSpHAuruENAM/view?usp=drive_link))
  - Analyze hazards explained in the video (code: [Tasks_VeeR](https://drive.google.com/file/d/16OagcWaDP7zbUy_SP-rzmAF3PSu5-2OD/view?usp=drive_link))
- **Performance Evaluation in RVfpga**
  - Watch this video: [PerformanceBenchmarkingVideo](https://www.youtube.com/watch?v=GqaDEW3W4X0) (the video is in Spanish, but you can watch an AI-translated-to-English version of the video here: [PerformanceBenchmarkingEnglishVideo](https://www.youtube.com/watch?v=DXB7jl1iGq8) or you can watch an AI-translated-to-Chinese version of the video here: [PerformanceBenchmarkingChineseVideo](https://www.youtube.com/watch?v=d5-0sNLW7wg)). You can obtain the slides used in the video here: [PerformanceSlides](https://drive.google.com/file/d/1xCmc4vFd_khLk6En14Ae_ZDF-OiP1QNm/view?usp=drive_link))
  - Complete: [Tasks_Performance](https://drive.google.com/file/d/1221ZkEwMsJuQGO-T1emmaSZvgeHH_mls/view?usp=drive_link)
- **Zephyr on VeeRwolf**
  - These resources provide detailed explanations on how to use Zephyr within the RVfpga/VeeRwolf environment, both in simulation and on the Nexys A7 board (highly recommended to fully leverage its capabilities). Additionally, you will find instructions for running a TensorFlow Lite model on Zephyr using the SoC we have studied in this module. Finally, we include some exercises, most of which can be performed in simulation and on the FPGA board.
    - [Running Zephyr on VeeRwolf](https://drive.google.com/file/d/1NhHENjrs6Qh67sln-8aBcfsszHKc3daD/view?usp=sharing) (IMPORTANT NOTE: In Section 2, step 4, replace line ```pip install fusesoc``` for ```pip install fusesoc==2.4.2```, to install a specific version of fusesoc that has been verified in this lab)
    - [VeeRWolf Zephyr Module](https://drive.google.com/file/d/1Nh-293681Sug0TC7LCY-1HGcuFA8uI-P/view?usp=drive_link)
    - [Zephyr Blinky Sample](https://drive.google.com/file/d/1NrapTS3pD1edNsC9jZgFUBlClN6UceAI/view?usp=drive_link)

### IN-PERSON PRACTICE (6 hours)
- **Input/Output in RVfpga**: [Practice_IO](https://drive.google.com/file/d/17nXdxS4ShI1Z-I5VhSzSehGR-g449GJZ/view?usp=drive_link)
- **VeeR EH1 and EL2 Cores**: [Practice_VeerEH1](https://drive.google.com/file/d/1pe7l4ddl4cMUhzx5Cn4oQ1fqV5IL0yM4/view?usp=drive_link)
- **Performance Evaluation in RVfpga**: [Practice_Performance](https://drive.google.com/file/d/11ftnn8QoSrMI0wn0X8Ez_ko8bibeW82-/view?usp=drive_link)
- In the following links, you can view the videos of the in-person session:
    - [Introduction](https://youtu.be/jclmekOv2oc)
    - [Input/Output](https://youtu.be/Cka9Hl5JXOY)
    - [Performance](https://youtu.be/jWfORj1ELS8)
    - [VeeR_EH1](https://youtu.be/C3sWmIMy5I0)
