# RVfpga: New Simulation Tools and Teaching Experiences 
In this repository we provide two new simulation tools that can be used in conjunction with the [“RVfpga: Understanding Computer Architecture”](https://university.imgtec.com/rvfpga-el2-v3-0-english-downloads-page/) course provided by Imagination Technologies. Binary beta versions of the two simulators are provided as a release in this repository. We include both Windows and Ubuntu versions.

+ RVfpga-ViDBo: It performs a Verilator-based simulation of the RVfpga System and connects it with a Nexys A7 simulated board based on [ViDBo](https://github.com/olofk/vidbo) that allows you to communicate with some simulated peripherals on the board (at this moment the following peripherals are supported: 16 switches, 16 LEDs, UART, 5 pushbuttons, 8 7-Segment Displays). This new simulation tool is especially useful for RVfpga labs 6-10. In folder [RVfpga_ViDBo](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/RVfpga_ViDBo) you can find detailed instructions on how to run the simulator in your own OS (either Ubuntu or Windows) as well as useful examples, videos, sources, etc.

<!-- 
<p align="center">
  <img src="RVfpga_ViDBo.png" width=60% height=60%>
</p>
-->

+ RVfpga-Pipeline: It performs a Verilator-based simulation of the RVfpga System that allows you to visualize different signals of the SweRV EH1 pipeline. This new simulation tool is especially useful for RVfpga labs 11-20. In folder [RVfpga_PipelineSimulator](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/RVfpga_PipelineSimulator) you can find detailed instructions on how to run the simulator in your own OS (either Ubuntu or Windows) as well as useful examples, videos, sources, etc.

<!-- 
<p align="center">
  <img src="RVfpga_PipelineSimulator.png" width=90% height=90%>
</p>
-->


In this repository we also show two example courses, instructed at UCM, where these new tools, as well as the whole [RVfpga materials](https://university.imgtec.com/rvfpga-el2-v3-0-english-downloads-page/), are adapted and used to peform several practical labs that help the students understand the theoretical concepts explained in theory. In case you want to obtain more information about this course (slides, exercises, solutions for the labs...), you can contact ```dani02@ucm.es```.

+ Computer Organization: This is a second-year course in the Computer Science degree program offered at UCM. You can find the information about this course at: [Computer Organization UCM](http://web.fdi.ucm.es/UCMFiles/pdf/FICHAS_DOCENTES/2024/8413.pdf). In folder [Computer_Organization](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization) you can find part of the materials (mainly the labs) used in this course.

+ Integrated Systems Architecture: This is a fourth-year course in the Electronics and Communication Engineering degree that we offer at UCM. You can find the information about this course at: [Integrated Systems Architecture UCM](https://fisicas.ucm.es/data/cont/docs/18-2021-09-01-2021-22%20Gu%C3%ADa%20Docente%20GIEC%20v1.1-157-16091.pdf). In folder [Integrated Systems Architecture](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Integrated_Systems_Architecture) you can find part of the materials (mainly the labs) used in this course.
