# RVfpga: Links, Teaching Materials and Experiences, Papers and Tools

## Links to the RVfpga materials

+ **MAIN LINK**: You can download the complete [RVfpga packages](https://university.imgtec.com/teaching-download/) from Imagination Technologies IUP.

+ You can access the [Computer Architecture with an Industrial RISC-V Core [RVfpga]](https://www.edx.org/learn/computer-programming/the-linux-foundation-computer-architecture-with-an-industrial-risc-v-core) edX MOOC, based on RVfpga.

+ RISC-V International recommends RVfpga in their [Learning Materials GitHub](https://github.com/riscv/learn) and for [Training and Certification](https://riscv.org/community/training/) in RISC-V.


## Teaching materials developed on top of RVfpga and teaching experiences
This repository provides materials from a range of RVfpga-based teaching experiences, primarily conducted during the 2024-25 and 2025-26 academic years.

We first show how we adapted and used the [RVfpga: Understanding Computer Architecture](https://university.imgtec.com/rvfpga-el2-v3-0-english-downloads-page/) and the [RVfpga-SoC](https://university.imgtec.com/rvfpgasoc-download-page-en/) packages provided by Imagination Technologies, as well as the [Ripes](https://github.com/mortbopet/Ripes) simulator, in the labs of three courses instructed at the University Complutense of Madrid (UCM).

+ **Computer Fundamentals** (second semester of year 2024-25): This is a first-year course in the Computer Science degree program at UCM. In folder **[Computer_Fundamentals_24-25](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Fundamentals)** of this repository you can find all the materials used in the course. Since this is an introductory course, we only use Ripes in the labs.

+ **Computer Organization** (first semester of years 2024-25 and 2025-26): This is a second-year course in the Computer Science degree program at UCM. In folders **[Computer_Organization_24-25](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization)** and **[Computer_Organization_25-26](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization_25-26)** of this repository you can find part of the materials (mainly the labs) used in the course. For the labs, we use a combination of Ripes and RVfpga-based exercises.

+ **Integrated Systems Architecture** (second semester of year 2024-25): This is a fourth-year course in the Electronics and Communication Engineering degree program at UCM. In folder **[Integrated_Systems_Architecture_24-25](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Integrated_Systems_Architecture)** of this repository you can find part of the materials (mainly the labs) used in the course. Since this is an advanced course, we mainly use RVfpga-based labs.

We also participated in the [Master de Formación Permanente en Sistemas Microelectrónicos Basados en Arquitecturas Abiertas](https://www.uclm.es/estudios/propios/master-formacion-permanente-sistemas-microelectricos-basados-arquitecturas-abiertas) (first semester of year 2024-25) at the University of Castilla-La Mancha (UCLM). Specifically, within the course Diseño de Microcontroladores en Hardware Abierto, we taught an entire two-week-long module based on RVfpga. You can find the details in the following folder: **[Design_Microcontrollers_Open_Hardware_24-25](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Design_Microcontrollers_Open_Hardware)**.

In the second semester of year 2024-25, we instructed a microcredential as part of a joint effort between UCM and [OpenChip](https://openchip.com/). This is the official webpage of the course: [RISC-V: Arquitectura y diseño basado en cores comerciales VeeR sobre FPGA](https://riscv.fdi.ucm.es/). Here, you can find all the materials used in the course: **[RVfpga_Microcredential_24-25](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/RVfpga_Microcredential)**.

Finally, it should be highlighted that a number of Bachelor's and Master's theses at UCM were developed using RVfpga, among which the most notable are:
+ **[Floating-point extensions for the SweRV EH1 core](https://docta.ucm.es/entities/publication/274f1b3a-c564-464d-8066-ef9aa4ae3c10)**
+ **[FPGA implementation of an AD-HOC RISC-V system-on-chip for industrial IoT](https://docta.ucm.es/entities/publication/9298fbe5-cabd-40a0-bec5-0501290c30d1)**



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

RVfpga provides both simulation and hardware-based methods for using and analyzing the RVfpga core, SoC, and its peripherals.  
The following figure shows an overview of these tools using the EL2 SoC and a Nexys A7 FPGA board.  
All tools share a common back-end —the VeeRwolfX SoC code— but use different front-ends.

<div align="center">
  <img src="https://github.com/user-attachments/assets/c59fb53a-1566-4ec3-8f43-b45167d9a2f6" width="600" alt="RVfpga tools diagram">
</div>

- **Execution on the physical board:**  
  The VeeRwolfX SoC can run in hardware on supported FPGA boards. Default configurations are provided with the packages, but users can also generate new bitstreams using Vivado. Instructions for generating the bitstream and running on these boards are available at [RVfpga: Understanding Computer Architecture](https://university.imgtec.com/rvfpga-el2-v3-0-english-downloads-page/) and in some of the above courses (such as [Integrated_Systems_Architecture_24-25](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Integrated_Systems_Architecture) or [Design_Microcontrollers_Open_Hardware_24-25](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Design_Microcontrollers_Open_Hardware)). RVfpga supports three FPGA boards: **Nexys A7, Basys 3, and Boolean**.

<p align="center">
  <img src="https://github.com/user-attachments/assets/3b1f86a4-5939-4990-830a-163abd594d05" 
       width="300" 
       alt="Nexys A7"
       style="margin-right:15px;"/>
  <img src="https://github.com/user-attachments/assets/e2932dfe-af8c-43de-beb9-626396357487" 
       width="300" 
       alt="Basys 3"
       style="margin-right:15px;"/>
  <img src="https://github.com/user-attachments/assets/ddfeb777-6d50-4da8-94b1-8f13dbfb11b7" 
       width="300" 
       alt="Boolean"/>
</p>


- **Execution in simulation:**  
  RVfpga includes several SoC simulation tools (the first three are based on Verilator). Instructions for running these simulators are available at [RVfpga: Understanding Computer Architecture](https://university.imgtec.com/rvfpga-el2-v3-0-english-downloads-page/) and in some of the above courses (such as [Computer_Organization_25-26](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization_25-26)):
  - **RVfpga-ViDBo**: simulates the RVfpga System on a Virtual Development Board, including communication with peripherals.

<p align="left">
&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;
<img src="https://github.com/user-attachments/assets/b695a296-f108-4655-871d-d535b776da96" 
     width="400" 
     alt="Descripción de la imagen">
</p>

  - **RVfpga-Pipeline**: visualizes the execution of instructions through the VeeR EH1 or EL2 pipeline.

<p align="left">
&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;
<img src="https://github.com/user-attachments/assets/629738ab-a889-4755-8b8c-2c90cb53676a" 
     width="900" 
     alt="Descripción de la imagen">
</p>

  - **RVfpga-Trace**: records internal SoC signals while running a program and visualizes them with GTKWave.

<p align="left">
&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;
<img src="https://github.com/user-attachments/assets/92800c3d-7624-48ac-8ce5-a2e74d4469fb" 
     width="600" 
     alt="Descripción de la imagen">
</p>


  - **RVfpga-Whisper**: a RISC-V Instruction Set Simulator.  

  With these tools, the complete RVfpga course can be followed without a physical board, at no cost.  
  Internally, all SoC simulators use **Verilator**, which translates the Verilog SoC into C++ code that is then compiled and executed to simulate RISC-V programs.  
  Default simulation binaries are included in the RVfpga package, but users can also generate new ones using Verilator.

  Sources and compilation instructions can be found in several places:

  1. **Course-provided packages** (two versions available):
     - [SimulatorsAndProjects_24-25](https://drive.google.com/file/d/1hbCSFmjIoGmXq4r5G12_AMUKezHXA6A-/view?usp=sharing)  
       After extracting the archive, the three simulators can be found in:
       - *RVfpga-ViDBo*: `Simuladores_EC_24-25/RVfpga/verilatorSIM_ViDBo`  
       - *RVfpga-Pipeline*: `Simuladores_EC_24-25/RVfpga/verilatorSIM_Pipeline`  
       - *RVfpga-Trace*: `Simuladores_EC_24-25/RVfpga/verilatorSIM_Trace`  
     - [SimulatorsAndProjects_25-26](https://drive.google.com/file/d/1CctkpRvmTS4PsdsKVPTHpT6g6qnUm3WH/view?usp=sharing)  
       Same as the previous version, but including an **enhanced RVfpga-Pipeline** simulator.

  2. **RVfpga course v3.0**: [RVfpga: Understanding Computer Architecture](https://university.imgtec.com/rvfpga-el2-v3-0-english-downloads-page/)  
  3. **edX MOOC**: [RVfpga-based MOOC](https://www.edx.org/learn/computer-programming/the-linux-foundation-computer-architecture-with-an-industrial-risc-v-core)  
  4. **Academic papers** associated with RVfpga  
  5. **Older versions** of RVfpga-ViDBo and RVfpga-Pipeline are also available on GitHub: [SimulationTools](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/SimulationTools)
