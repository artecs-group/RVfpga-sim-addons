# RVfpga-sim-addons
Suplementary simulation tools for the RVfpga course developed by Imagination Technologies

We provide two new simulation tools that can be used in conjuntion with the “RVfpga: Understanding Computer Architecture” course provided by Imagination Technologies. 

RVfpga_ViDBo: It performs a Verilator-based simulation of the RVfpga System (which is based on SweRVolf SoC and SweRV EH1) running a test program and connects this simulation with a Nexys A7 simulated board called ViDBo that allows you to communicate with some of the peripherals on the board (at this moment the following peripherals are supported: 16 switches, 16 LEDs, UART, 5 pushbuttons, 8 7-Segment Displays). This new simulation tool is especially useful for RVfpga labs 6-10. 

RVfpga_PipelineSimulator: It performs a Verilator-based simulation of the RVfpga System (which is based on SweRVolf SoC and SweRV EH1) running a test program and connects this simulation with a simulation of the SweRV EH1 core that allows you to visualize different signals of the pipeline and understand the execution of the test program. This new simulation tool is especially useful for RVfpga labs 11-20. 

We highly recommend you to download the whole RVfpga course, that can be obtained through the following link: https://university.imgtec.com/rvfpga-download-page-en/