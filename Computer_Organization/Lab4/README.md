# Lab 4 - The RVfpga I/O System
This practice aims to help students gain a thorough understanding of an Input/Output System. You can follow the next steps:

1. If you are new to Computer Organization, you should start by reading Chapter 9 of the H&H book.
2. Then, you should look at the detailed presentation of the RVfpga I/O System provided here: [Presentation_RVfpga_IO](https://drive.google.com/file/d/1Fv4-I8DwISdqqDpol4i_BMZNzK4QmpOe/view?usp=sharing) (if necessary, you can obtain more information in the [RVfpga: Understanding Computer Architecture](https://university.imgtec.com/rvfpga-el2-v3-0-english-downloads-page/) course).
3. Then, you can perform the guided example provided [next](https://github.com/artecs-group/RVfpga-sim-addons/blob/main/Computer_Organization/Lab4/README.md#introduction---simulation-of-the-rvfpga-soc) in this repository.
4. Finally, you can resolve the exercises included [below](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab4#exercise-1) in this repository.

## Introduction - Simulation of the RVfpga SoC
In this lab, we will use the RVfpga-ViDBo simulator. This tool simulates the VeeRwolfX SoC based on the VeeR EH1 core running on the Nexys A7 FPGA board. The simulator allows us to simulate the execution of RISC-V codes on this processor and interact with some of the board’s peripherals. The programs work exactly the same in the simulator as on the actual board.

<p align="center">
  <img src="Images/Nexys.png" width=80% height=80%>
</p>

In this lab, we will only use the following peripherals among all the available ones:
- 16 LEDs
- 16 Switches
- 8 digits with 7-segment displays

Follow the steps below to launch an example simulation on RVfpga-ViDBo, where the state of the switches is continuously read and displayed on the LEDs.
1. Open Visual Studio Code (VSCode).
2. Click on ```File - Open Folder``` and open the folder containing the project for the example we will work on in this introduction: ```/home/rvfpga/Simuladores_EC_24-25/RVfpga/Projects/LedsSwitches_C-Lang```

<p align="center">
  <img src="Images/OpenFolder.png" width=80% height=80%>
</p>

3. Set the path for the simulator in the ```platformio.ini``` file. In this lab, we will use the RVfpga-ViDBo simulator. In this project, the path is already correctly set in the following line, so you do not need to change anything:

```board_debug.verilator.binary = /home/rvfpga/Simuladores_EC_24-25/RVfpga/verilatorSIM_ViDBo/OriginalBinaries/RVfpga-ViDBo_Ubuntu22```

4. Run the simulator:

    a. In the ```PROJECT TASKS``` window of PlatformIO, click on ```RVfpgaEL2-ViDBo/Pipeline```

   <p align="center">
      <img src="Images/RVfpgaVidbo.png" width=30% height=30%>
   </p>
   
    b. Open a terminal and launch the ViDBo server by running the following commands:

      ```
      cd /home/rvfpga/Simuladores_EC_24-25/RVfpga/verilatorSIM_ViDBo
      python3 -m http.server --directory NexysA7board/
      ```

     <p align="center">
        <img src="Images/Python.png" width=100% height=100%>
     </p>

    c. Finally, open a browser and go to http://localhost:8000/nexys-a7.html, connect to the board, and check the simulation by modifying the switches and viewing the LEDs. This code would behave exactly the same if run on the actual board.

     <p align="center">
        <img src="Images/NexysExample.png" width=80% height=80%>
     </p>

## Exercise 1

