# RVfpga: Teaching Experiences and Simulation Tools 

## Teaching experiences at UCM:
In this repository, we show how we adapted and used the [RVfpga materials](https://university.imgtec.com/rvfpga-el2-v3-0-english-downloads-page/) in the labs of two courses instructed at UCM.

+ Computer Organization: This is a second-year course in the Computer Science degree program offered at UCM. In folder [Computer_Organization](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization) of this repository you can find part of the materials (mainly the labs) used in the course. 

+ Integrated Systems Architecture: This is a fourth-year course in the Electronics and Communication Engineering degree that we offer at UCM. In folder [Integrated Systems Architecture](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Integrated_Systems_Architecture) of this repository you can find part of the materials (mainly the labs) used in the course.

**NOTE: In case you want to obtain more information about these courses (such as the slides, the exercises sheets, the solutions for the labs, etc.), you can contact ```dani02@ucm.es```**

## New simulation tools - RVfpga-ViDBo and RVfpga-Pipeline:
In this repository, we also provide two simulation tools that can be used in conjunction with the [“RVfpga: Understanding Computer Architecture”](https://university.imgtec.com/rvfpga-el2-v3-0-english-downloads-page/) course provided by Imagination Technologies. Binary beta versions of the two simulators are provided as a release in this repository. We include both Windows and Ubuntu versions.

**NOTE: The courses mentioned above include modified versions of these simulation tools. Moreover, v3 of the [RVfpga materials](https://university.imgtec.com/rvfpga-el2-v3-0-english-downloads-page/) also includes newer versions of these tools.**

+ RVfpga-ViDBo: It performs a Verilator-based simulation of the RVfpga System and connects it with a Nexys A7 simulated board based on [ViDBo](https://github.com/olofk/vidbo) that allows you to communicate with some simulated peripherals on the board (at this moment the following peripherals are supported: 16 switches, 16 LEDs, UART, 5 pushbuttons, 8 7-Segment Displays). This new simulation tool is especially useful for RVfpga labs 6-10. In folder [RVfpga_ViDBo](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/RVfpga_ViDBo) of this repository you can find detailed instructions on how to run the simulator in your own OS (either Ubuntu or Windows) as well as useful examples, videos, sources, etc.

<!-- 
<p align="center">
  <img src="RVfpga_ViDBo.png" width=60% height=60%>
</p>
-->

+ RVfpga-Pipeline: It performs a Verilator-based simulation of the RVfpga System that allows you to visualize different signals of the SweRV EH1 pipeline. This new simulation tool is especially useful for RVfpga labs 11-20. In folder [RVfpga_PipelineSimulator](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/RVfpga_PipelineSimulator) of this repository you can find detailed instructions on how to run the simulator in your own OS (either Ubuntu or Windows) as well as useful examples, videos, sources, etc.

<!-- 
<p align="center">
  <img src="RVfpga_PipelineSimulator.png" width=90% height=90%>
</p>
-->
