# RVfpga-sim-addons
We provide two new simulation tools that can be used in conjuntion with the [“RVfpga: Understanding Computer Architecture”](https://university.imgtec.com/rvfpga-download-page-en/) course provided by Imagination Technologies.

+ RVfpga_ViDBo: It performs a Verilator-based simulation of the RVfpga System and connects it with a Nexys A7 simulated board based on [ViDBo](https://github.com/olofk/vidbo) that allows you to communicate with some simulated peripherals on the board (at this moment the following peripherals are supported: 16 switches, 16 LEDs, UART, 5 pushbuttons, 8 7-Segment Displays). This new simulation tool is especially useful for RVfpga labs 6-10.

<kbd>
<p align="center" kbd>
  <img src="RVfpga_ViDBo.png" width=60% height=60%>
</p>
</kbd>

+ RVfpga_PipelineSimulator: It performs a Verilator-based simulation of the RVfpga System that allows you to visualize different signals of the pipeline. This new simulation tool is especially useful for RVfpga labs 11-20.

Binary beta version (Ubuntu) of the two simulators are provided as a release in this repository.
