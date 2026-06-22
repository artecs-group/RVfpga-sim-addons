# Microcredential - RISC-V - 2025-26: RISC-V: Architecture and Design based on Commercial VeeR Cores on FPGA

The course begins with an extensive introduction to RISC-V architecture and assembly programming, and continues with a series of input/output labs using a SoC based on the RISC-V VeeR EL2 and EH1 softcores.
Subsequently, a detailed study of these cores and their Verilog code is conducted. The goal of this study is for students not only to understand the design of the mentioned cores but also to be able to modify and/or integrate them into Systems-on-Chip (SoCs).
In the final module, a complete application will also be deployed, using Zephyr Project as the RTOS and TensorFlow Lite for microcontrollers. All developments will be carried out using Xilinx FPGAs.

The course will take place over six consecutive weeks, from May 11 to June 26. During each week, students will be required to complete various assignments. Then, in-person sessions will be held at the end of each week.

---

## SUMMARIZED SCHEDULE (more details going into each module):

**May 11 - Welcome Session:** 
- [Slides: Welcome Session](https://drive.google.com/file/d/187rf7Bz2vArmV7E5L5xzS7HF_8hG6gNU/view?usp=sharing)
- [Video: Welcome Session](https://www.youtube.com/watch?v=cKB7Ky25nQM)

· · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · 

**May 11-13 - Tasks to complete before 1st session:**
- Install and test the tools on the Virtual Machine: [Module 0](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/RVfpga_Microcredential_25-26/Module0)
- Review the RISC-V architecture and assembly language (Module 1):
    - [RISC-V Architecture](https://www.fdi.ucm.es/profesor/mendias/FC2/FC2module2.pdf)
    - [RISC-V Assembly](https://www.fdi.ucm.es/profesor/mendias/FC2/FC2module3.pdf)
    - [RISC-V Instruction Format](https://www.fdi.ucm.es/profesor/mendias/FC2/FC2module4.pdf)

**May 14 - 1st Session:**
- [Video: Introduction to Module 1](https://www.youtube.com/watch?v=-YGfecV1NsQ)
- You must complete complete the exercises proposed in project *ImageProcessingProject*. Look at the instructions described in [Module 1](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/RVfpga_Microcredential_25-26/Module1)

· · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · 

**May 18-21 - Tasks to complete:**
- [Video: Work to complete before 2nd Session](https://www.youtube.com/watch?v=bsVilMYW5Mc)
- Review Input/Output and Verilog concepts.
- View the RVfpga Input/Output video.
- Analyze provided programs:
    - *LEDs* and *Switches*
    - *7-Segment displays*
    - *Program-based I/O* vs *Interrup-based I/O*
- More details about these tasks can be found in [Module 2](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/RVfpga_Microcredential_25-26/Module2)

**May 22 - 2nd Session:**
- [Video: Introduction to Module 2](https://www.youtube.com/watch?v=NKhbjLduCBs)
- You must complete the 5 exercises (exercises 3 and 5 are optional) proposed in [Module 2](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/RVfpga_Microcredential_25-26/Module2#to-complete-in-the-2nd-session-friday-may-22)

· · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · 

**May 25-28 - Tasks to complete:**
- [Video: Work to complete before 3rd Session](https://www.youtube.com/watch?v=KIOg338Xp2Y)
- Understand in detail the 8-Digit 7-Segment-Displays Verilog controller.
- Install Vivado in your computer.
- More details about these tasks can be found in [Module 2-B](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/RVfpga_Microcredential_25-26/Module2_B)

**May 29 - 3rd Session:**
- [Video: Introduction to Module 2-B](https://www.youtube.com/watch?v=U5HvPjIwxSc)
- You must complete the 2 exercises proposed in [Module 2-B](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/RVfpga_Microcredential_25-26/Module2_B#to-complete-in-the-3rd-session-friday-may-29)

· · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · 

**June 1-11 - Tasks to complete:**
- [Video: Work to complete before 4th Session](https://www.youtube.com/watch?v=UwckbUKm_Ko)
- Watch the video that describes the VeeR EH1 microarchitecture in detail.
- Perform the guided exercises with RVfpga-Pipeline and RVfpga-Trace. These exercises are just provided for learning purposes, they must not be included in the report.
- More details about these tasks can be found in [Module 3](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/RVfpga_Microcredential_25-26/Module3)

**June 12 - 4th Session:**
- [Video: Introduction to Module 3](https://www.youtube.com/watch?v=aSMYbTeSdrY)
- You must complete the 2 exercises proposed in [Module 3](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/RVfpga_Microcredential_25-26/Module3#to-complete-in-the-4th-session-friday-june-12)

· · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · 

**June 15-18 - Tasks to complete:**
- [Video: Work to complete before 5th Session](https://www.youtube.com/watch?v=J0wuAjrJypw)
- Review Memory Hierarchy concepts.
- Watch the *PerformanceBenchmarkingVideo* video.
- Perform the Hw Counters example.
- More details about these tasks can be found in [Module 3-B](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/RVfpga_Microcredential_25-26/Module3_B)

**June 19 - 5th Session:**
- [Video: Introduction to Module 3-B](https://www.youtube.com/watch?v=lPXHD5m8MtE)
- Complete the exercises described in [Module 3-B](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/RVfpga_Microcredential_25-26/Module3_B#to-complete-in-the-4th-session-friday-june-12)

· · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · 

**June 26 - 6th Session:**
- Look at the instructions described in [Module 4](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/RVfpga_Microcredential_25-26/Module4)

· · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · 

**July 12 - Reports:**
- You must submit one or more documents to dani02@ucm.es containing, at a minimum, the solutions to all mandatory exercises completed throughout the course.
- Your submission should include the source code developed, explanations of the work performed, screenshots, photographs, videos (or links to videos), and any other relevant material. Make sure to clearly justify your solutions, describe the methodology followed, and explain the results obtained.
- Optional exercises may also be included and will be considered positively during the evaluation.
