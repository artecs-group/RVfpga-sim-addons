# RVfpga: Links, Teaching Materials and Experiences, Papers and Tools

## Links to obtain the RVfpga materials

+ MAIN LINK: You can download the complete [RVfpga package](https://university.imgtec.com/teaching-download/) from Imagination Technologies.

+ You can take the [Computer Architecture with an Industrial RISC-V Core [RVfpga]](https://www.edx.org/learn/computer-programming/the-linux-foundation-computer-architecture-with-an-industrial-risc-v-core) edX MOOC. This course is included in the [RVFA Certification](https://riscv.org/community/training/).

+ RISC-V International recommends RVfpga in their [Learning Materials GitHub](https://github.com/riscv/learn).


## Teaching materials and experiences
This repository provides materials from a range of RVfpga-based teaching experiences, primarily conducted during the 2024-25 academic year.

We first show how we adapted and used the [RVfpga: Understanding Computer Architecture](https://university.imgtec.com/rvfpga-el2-v3-0-english-downloads-page/) and the [RVfpga-SoC](https://university.imgtec.com/rvfpgasoc-download-page-en/) packages provided by Imagination Technologies, as well as the [Ripes](https://github.com/mortbopet/Ripes) simulator, in the labs of three courses instructed at the University Complutense of Madrid (UCM).

+ **Computer Fundamentals** (second semester of year 2024-25): This is a first-year course in the Computer Science degree program at UCM. In folder **[Computer_Fundamentals](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Fundamentals)** of this repository you can find all the materials used in the course. Since this is an introductory course, we only use Ripes in the labs.

+ **Computer Organization** (first semester of year 2024-25): This is a second-year course in the Computer Science degree program at UCM. In folder **[Computer_Organization](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization)** of this repository you can find part of the materials (mainly the labs) used in the course. For the labs, we use a combination of Ripes and RVfpga-based exercises.

+ **Integrated Systems Architecture** (second semester of year 2024-25): This is a fourth-year course in the Electronics and Communication Engineering degree program at UCM. In folder **[Integrated_Systems_Architecture](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Integrated_Systems_Architecture)** of this repository you can find part of the materials (mainly the labs) used in the course. Since this is an advanced course, we mainly use RVfpga-based labs.

We also participated in the [Master de Formación Permanente en Sistemas Microelectrónicos Basados en Arquitecturas Abiertas](https://www.uclm.es/estudios/propios/master-formacion-permanente-sistemas-microelectricos-basados-arquitecturas-abiertas) (first semester of year 2024-25) at the University of Castilla-La Mancha (UCLM). Specifically, within the course Diseño de Microcontroladores en Hardware Abierto, we taught an entire two-week-long module based on RVfpga. You can find the details in the following folder: **[Design_Microcontrollers_Open_Hardware](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Design_Microcontrollers_Open_Hardware)**.

We developed an **[RVfpga-based MOOC](https://www.edx.org/learn/computer-programming/the-linux-foundation-computer-architecture-with-an-industrial-risc-v-core)** in edX. This MOOC course includes 10 chapters that cover labs 1-4, 6-9, and 11 of the RVfpga course. The chapters provide instructions, hands-on tutorials, videos with demonstrations, exercises, and multiple-choice questions.

In recent years, we have also supervised several Bachelor's and Master's theses based on RVfpga. The following are among the most significant:
+ **[Floating-point extensions for the SweRV EH1 core](https://docta.ucm.es/entities/publication/274f1b3a-c564-464d-8066-ef9aa4ae3c10)**
+ **[FPGA implementation of an AD-HOC RISC-V system-on-chip for industrial IoT](https://docta.ucm.es/entities/publication/9298fbe5-cabd-40a0-bec5-0501290c30d1)**

Finally, in the second semester of year 2024-25, we will deliver a microcredential as part of a joint effort between UCM and [OpenChip](https://openchip.com/). Here, you can find all the materials used in the course: **[RVfpga_Microcredential](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/RVfpga_Microcredential)**. This is the official webpage of the course: [RISC-V: Arquitectura y diseño basado en cores comerciales VeeR sobre FPGA](https://riscv.fdi.ucm.es/).



## Papers, Presentations and Videos
If you're interested in learning more about the details of the RVfpga course, check out our paper released in Oct-2024: 

* **[The RISC-V FPGA (RVfpga) Teaching Package](https://www.authorea.com/doi/full/10.36227/techrxiv.172978275.56140460)** 

For insights into other teaching experiences based on RVfpga, you can explore another paper released in Nov-2024: 

* **[Teaching Experiences using the RVfpga Package](http://arxiv.org/abs/2411.14954)**

We recently presented *Teaching Computer Architecture with RVfpga* at the 2024 Sino-European RISC-V Workshop. You can download the slides here:

* **[Teaching Computer Architecture with RVfpga](https://drive.google.com/file/d/1JlivSs5iZqpF1h7p_dbInBxkeEg9aDwf/view?usp=drive_link)**

We also recently gave talk *Teaching Experiences with RVfpga* at the 2025 RISC-V Education Forum (RISC-V Ecosystem Conference) at China. You can view the video here:

* **[Teaching Experiences with RVfpga](https://youtu.be/gUCAdCwOHEc)**

Finally, in the following links you can also find many videos that illustrate different topics of RVfpga.

  - Videos at YouTube Channel: **[RVfpgaVideos](https://www.youtube.com/@RVfpgaVideos)**
  - Imperial College WS 2022: **[LondonWS](https://youtube.com/playlist?list=PLnOXj03cuJjkes1OIMa8SFyn1yKQQY8aD&si=mNLqXXbtPnbuobof)**
  - IUP Video Library:
      - **[IUP1](https://youtube.com/playlist?list=PLnOXj03cuJjnip1WRJrUHNvm-80zSSfUC&si=-NR59bFEMBDF9kjs)**
      - **[IUP2](https://youtube.com/playlist?list=PLnOXj03cuJjn7ecksWZEwCe8LVR-PDgud&si=xdQEoILML6WQMnjC)**


## RVfpga Tools
We provide both simulation and hardware methods for using and analyzing the RVfpga core, SoC, and its peripherals. The next figure shows a diagram of these tools using the EL2 SoC and a Nexys A7 FPGA board. All the tools share a common back-end, the VeeRwolfX SoC code, but have different front-ends.

<div align="center">
  <img src="https://github.com/user-attachments/assets/c59fb53a-1566-4ec3-8f43-b45167d9a2f6" width="600" alt="Descripción de la imagen">
</div>

  * **Execution on the physical board:**  To use the VeeRwolfX SoC in hardware on an FPGA board, we provide the default configurations with the packages; users could generate a new bitstream using Vivado. RVfpga supports three FPGA boards: the
Nexys A7, Basys 3 and Boolean boards. All instructions for generating the bitstream and for running on the different boards can be found at [RVfpga: Understanding Computer Architecture](https://university.imgtec.com/rvfpga-el2-v3-0-english-downloads-page/).
  * **Execution in simulation:** RVfpga includes three SoC simulation tools based on Verilator: RVfpga-ViDBo (it uses a Virtual Development Board to perform a simulation of the RVfpga System and communicate with the peripherals on the simulated board), RVfpgaPipeline (it shows the instructions of a RISC-V program flowing through the VeeR EH1 or EL2 pipeline), and RVfpga-Trace (it generates a trace of the internal signals of the SoC while executing a given program and then visualizes the waveform of this trace using GTKWave). These tools, in addition to RVfpga-Whisper (a RISC-V Instruction Set Simulator), can be used to complete the course without needing a physical board; thus, the RVfpga course can be completed at no cost. The back-end of each of these SoC simulators is Verilator, which transforms the Verilog SoC into C++ code; the user then compiles and executes that code to run a RISC-V program in simulation. Each SoC simulation tool then uses those simulation results. The simulation binaries for the default configurations are provided with the RVfpga package, but users can generate new binaries using Verilator. The sources for these simulators and instructions on how to compile and use them can be found in several places:
    1. The sources provided for the courses mentioned above ([SimulatorsAndProjects](https://drive.google.com/file/d/1hbCSFmjIoGmXq4r5G12_AMUKezHXA6A-/view?usp=sharing))
    2. Version 3.0 of the RVfpga course ([RVfpga: Understanding Computer Architecture](https://university.imgtec.com/rvfpga-el2-v3-0-english-downloads-page/))
    3. The MOOC edX course ([RVfpga-based MOOC](https://www.edx.org/learn/computer-programming/the-linux-foundation-computer-architecture-with-an-industrial-risc-v-core))
    4. The papers mentioned above
    5. Old versions of RVfpga-ViDBo and RVfpga-Pipeline are also provided in this GitHub ([SimulationTools](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/SimulationTools))
