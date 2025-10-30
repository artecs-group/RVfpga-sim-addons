# Design of Microcontrollers in Open Hardware

In Weeks 5 and 6 of DISEÑO DE MICROCONTROLADORES EN HARDWARE ABIERTO, students dive into the world of open hardware microcontrollers using the RVfpga platform. Through videos, guided exercises, and hands-on labs, they learn how to analyze the VeeR EH1/EL2 cores, explore input/output systems, evaluate processor performance, and use the Zephyr Operating System.

---

## Week 5 (December 8th to 12th, 2025)

### ONLINE THEORY AND TASKS (To complete between December 8th and December 11th)
- **Introduction to RVfpga**
  - Watch this video: [IntroductionRVfpgaVideo](https://www.youtube.com/watch?v=sc_Jn0XSkNw). You can obtain the slides used in the video here: [IntroSlides](https://drive.google.com/file/d/17Kid-KSDqPOPoEudiWhcuOdUChYpkcbp/view?usp=drive_link).
  - Install the environment and test tools. Follow the instructions in the document [Practice_Familiarization_fpga](https://drive.google.com/file/d/1vdLf39U89q38gmLuodo7nZkctRqeAiyO/view?usp=drive_link). Each section includes a link to a video illustrating its content.
    - Install Virtual Machine (VM)
    - Download RVfpga Sources in the VM
    - Test `RVfpga-Pipeline` and complete the task
    - Test `RVfpga-Trace` and complete the task
    - Test `RVfpga-ViDBo`
    - Test `RVfpga-Nexys` (only if you have the board)
    - Test `RVfpga-Whisper`

- **Input/Output in RVfpga**
  - Watch this video: [InputOutputVideo](https://www.youtube.com/watch?v=8fK-CoEbo0Y). The video describes the RVfpga I/O System in detail. You can obtain the slides used in the video here: [IOSlides](https://drive.google.com/file/d/1-Kav6TLV5xBURQYfZfRP3yzWUq_Qp7eV/view?usp=drive_link))
  - Complete: [Tasks_InputOutput](https://drive.google.com/file/d/1FX5Fr63ecMRLswCPk606GWZr7z65b1Fp/view?usp=drive_link)

- **VeeR EH1 and EL2 Cores**
  - Watch this video: [VeeReh1Video](https://youtu.be/xVnB6OM00cE?si=0HW333O-oPOXUDZG). The video describes the VeeR EH1 microarchitecture in detail. You can obtain the slides used in the video here: [EH1Slides](https://drive.google.com/file/d/1kIMQY3u5jZB7cAktFPqIHSpHAuruENAM/view?usp=drive_link))
  - Analyze hazards explained in the video (code: [Tasks_VeeR](https://drive.google.com/file/d/1NSOsgaQnFWfeKJbu6r6319T3zq0wzgf-/view?usp=sharing)).
      - The following table illustrates the forwarding paths available in the VeeR EH1 processor: [FwdPen_EH1](https://drive.google.com/file/d/1owNZUEw-2AZw2-El_mBu4-WpZ1HhYVNo/view?usp=sharing).
      - *NOTE: the RVfpga-Pipeline version that you are using in this course features a cleaner interface with improved visuals, a “-1 Cycle” button to step back one cycle, red dashed arrows showing data forwarding paths (including partial support for Secondary ALU forwardings), and highlighted pipeline stages displaying the active instruction. The problem is that it does not fully match the images and videos in the original demo materials.*

- **Performance Evaluation in RVfpga**
  - Watch this video: [PerformanceBenchmarkingVideo](https://www.youtube.com/watch?v=GqaDEW3W4X0). You can obtain the slides used in the video here: [PerformanceSlides](https://drive.google.com/file/d/1xCmc4vFd_khLk6En14Ae_ZDF-OiP1QNm/view?usp=drive_link))
  - Complete: [Tasks_Performance](https://drive.google.com/file/d/1221ZkEwMsJuQGO-T1emmaSZvgeHH_mls/view?usp=drive_link)


### IN-PERSON PRACTICE (December 12th)
- **Input/Output in RVfpga**: [Practice_IO]()
- **VeeR EH1 and EL2 Cores**: [Practice_VeerEH1]()
- **Performance Evaluation in RVfpga**: [Practice_Performance]()

---

## Week 6 (December 15th to 19th, 2025)

