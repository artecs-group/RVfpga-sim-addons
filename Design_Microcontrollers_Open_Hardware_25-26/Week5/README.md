# Week 5

## ONLINE THEORY AND TASKS (December 8th to December 11th)

During this week, you will work on the online component of the course, focused on the RVfpga platform and the VeeR EH1 and EL2 processor cores. The material includes a set of videos and guided exercises designed to help you understand the structure of the RVfpga SoC, its input/output system, and performance evaluation techniques. Completing these activities before the in-person lab on Friday is essential, as they provide the background knowledge required for the laboratory session.

The documents include two types of tasks: Mandatory and Optional. The mandatory tasks cover the essential aspects needed to complete the compulsory exercises during the lab session. The optional tasks explore more advanced topics and can help you deepen your understanding and improve your final grade. If your time is limited, focus on the mandatory tasks first.

Take your time to watch the videos carefully, analyze the contents, and complete the proposed exercises. There are no submissions required during the week; however, you are expected to attend the in-person session familiar with the materials and ready to apply what you have learned.

We encourage you to work steadily throughout the week. The effort you invest in understanding the materials and completing the online tasks will help you make the most of the in-person session and reinforce your understanding of the course as a whole.

1. **Introduction to RVfpga**
  - Watch this video: [IntroductionRVfpgaVideo](https://www.youtube.com/watch?v=sc_Jn0XSkNw). You can obtain the slides used in the video here: [IntroSlides](https://drive.google.com/file/d/17Kid-KSDqPOPoEudiWhcuOdUChYpkcbp/view?usp=drive_link).
  - Install the environment and test tools. Follow the instructions in the document [Practice_Familiarization_fpga](https://drive.google.com/file/d/1vdLf39U89q38gmLuodo7nZkctRqeAiyO/view?usp=drive_link). Each section includes a link to a video illustrating its content.
    - Install Virtual Machine (VM)
    - Download RVfpga Sources in the VM
    - Test `RVfpga-Pipeline` and complete the task
    - Test `RVfpga-Trace` and complete the task
    - Test `RVfpga-ViDBo`
    - Test `RVfpga-Nexys` (only if you have the board)
    - Test `RVfpga-Whisper`

2. **Input/Output in RVfpga**
  - Watch this video: [InputOutputVideo](https://www.youtube.com/watch?v=8fK-CoEbo0Y). The video describes the RVfpga I/O System in detail. You can obtain the slides used in the video here: [IOSlides](https://drive.google.com/file/d/1-Kav6TLV5xBURQYfZfRP3yzWUq_Qp7eV/view?usp=drive_link))
  - Complete: [Tasks_InputOutput](https://drive.google.com/file/d/1FX5Fr63ecMRLswCPk606GWZr7z65b1Fp/view?usp=drive_link)

3. **VeeR EH1 and EL2 Cores**
  - Watch this video: [VeeReh1Video](https://youtu.be/xVnB6OM00cE?si=0HW333O-oPOXUDZG). The video describes the VeeR EH1 microarchitecture in detail. You can obtain the slides used in the video here: [EH1Slides](https://drive.google.com/file/d/1kIMQY3u5jZB7cAktFPqIHSpHAuruENAM/view?usp=drive_link))
  - Analyze hazards explained in the video (code: [Tasks_VeeR](https://drive.google.com/file/d/1NSOsgaQnFWfeKJbu6r6319T3zq0wzgf-/view?usp=sharing)).
      - The following table illustrates the forwarding paths available in the VeeR EH1 processor: [FwdPen_EH1](https://drive.google.com/file/d/1owNZUEw-2AZw2-El_mBu4-WpZ1HhYVNo/view?usp=sharing).
      - *NOTE: the RVfpga-Pipeline version that you are using in this course features a cleaner interface with improved visuals, a “-1 Cycle” button to step back one cycle, red dashed arrows showing data forwarding paths (including partial support for Secondary ALU forwardings), and highlighted pipeline stages displaying the active instruction. The problem is that it does not fully match the images and videos in the original demo materials.*

4. **Performance Evaluation in RVfpga**
  - Watch this video: [PerformanceBenchmarkingVideo](https://www.youtube.com/watch?v=GqaDEW3W4X0). You can obtain the slides used in the video here: [PerformanceSlides](https://drive.google.com/file/d/1xCmc4vFd_khLk6En14Ae_ZDF-OiP1QNm/view?usp=drive_link))
  - Complete: [Tasks_Performance](https://drive.google.com/file/d/1221ZkEwMsJuQGO-T1emmaSZvgeHH_mls/view?usp=drive_link)

---

## IN-PERSON PRACTICE (December 12th)

The in-person lab session will take place on Friday, December 12th. During the session, you will apply the concepts learned during the week to complete several hands-on exercises related to I/O systems, the VeeR EH1 and EL2 cores, and performance evaluation in the RVfpga SoC.

At the end of the session, you will be asked to submit a short report summarizing your results. This report may include screenshots from the simulator or board executions, the programs you have developed, and explanations of the obtained results. A few days later, you will submit an extended version of this report, which may include additional exercises you were unable to complete during the practice.

1. **Input/Output in RVfpga**: [Practice_IO]()

2. **VeeR EH1 and EL2 Cores**: [Practice_VeerEH1]()

3. **Performance Evaluation in RVfpga**: [Practice_Performance]()

