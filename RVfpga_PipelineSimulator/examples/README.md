## **Ubuntu 20/22**

(The following steps are illustrated in this [example video](https://drive.google.com/file/d/1fX9cWZdV_GF7UTNUp-tYYD5TfJakeJai/view?usp=sharing))

Follow the next steps to run the Test program in the RVfpga_PipelineSimulator:

1. Download the whole *RVfpga-sim-addons* folder as well as the **RVfpga_PipelineSimulator_Ubuntu** binary from the releases. Give execution permisions to the binary and move it to the *RVfpga-sim-addons/RVfpga_ViDBo/examples* folder.

2. Open a terminal and go into the current folder (*RVfpga-sim-addons/RVfpga_PipelineSimulator/examples*).

3. Launch the simulation of the Test program:
```
         ./RVfpga_PipelineSimulator_Ubuntu +ram_init_file=Test/Test.vh
```
4. Execution will stop at the end of the endless loop (where our program includes a control instruction- and t2, t4, t5- that makes simulation stop), and you'll be able to analyse the execution of the program cycle by cycle in the SweRV EH1 processor from that point (remember that you can view the program that you are simulating in file Test/Test.S). Specifically, we are interested in analyzing the following block of instructions (*nop* instructions are included in order to isolate the different iterations), so you can fast forward several cycles and then analyze those instructions carefully cycle-by-cycle:

```c
         add t3, t3, t3        
         add t3, t3, t3
         mul t3, t3, t4
         mul t5, t5, t5
         lw t3, 4(t0)      # load from the DCCM (low-latency)
         lw t3, (t1)       # load from the External Memory (high-latency that makes the processor stall for some cycles)
```

___


## **Windows**

(The following steps are illustrated in this [example video](https://drive.google.com/file/d/1yGHDSitvdZiQzkdsvL0qKYCGUTGjoR33/view?usp=sharing))

Follow the next steps to run the Test program in the RVfpga_PipelineSimulator:

1. Install cygwin as explained in Appendix C of the RVfpga Getting Started Guide. Install all the packages stated in that document plus some other packages needed for the two new simulators (install the latest available version unless for gcc-core and gcc-g++, as stated below):

    * git
    * make 
    * autoconf
    * gcc-core (IMPORTANT: install version 10.2.0)
    * gcc-g++ (IMPORTANT: install version 10.2.0)
    * flex
    * bison
    * perl
    * libargp-devel
    * python3
    * xorg-server
    * xinit
    * libgtk3-devel

2. Download the whole RVfpga-sim-addons folder as well as the **RVfpga_PipelineSimulator_Windows.exe** binary from the releases

3. Open a cygwin terminal (you can go into your Windows user by running: ``` cd /cygdrive/c/Users/<your-user> ```). Go into the current folder (*RVfpga-sim-addons/RVfpga_PipelineSimulator/examples*). Run the following command:

```
startx <absolute-path-to-binary-file>/RVfpga_PipelineSimulator_Windows.exe +ram_init_file=Test/Test.vh
```

4. Execution will stop at the end of the endless loop (where our program includes a control instruction- and t2, t4, t5- that makes simulation stop), and you'll be able to analyse the execution of the program cycle by cycle in the SweRV EH1 processor from that point (remember that you can view the program that you are simulating in file Test/Test.S). Specifically, we are interested in analyzing the following block of instructions (*nop* instructions are included in order to isolate the different iterations), so you can fast forward several cycles and then analyze those instructions carefully cycle-by-cycle:

```c
         add t3, t3, t3        
         add t3, t3, t3
         mul t3, t3, t4
         mul t5, t5, t5
         lw t3, 4(t0)      # load from the DCCM (low-latency)
         lw t3, (t1)       # load from the External Memory (high-latency that makes the processor stall for some cycles)
```

___


## **Simulate other programs**

### **1st Option (both Ubuntu and Windows)**

(The following steps are illustrated in this [example video](https://drive.google.com/file/d/1beJl3NIKAPqtg3ozgQWo37VdkAPXRUQc/view?usp=sharing))

You can simulate any other program in RVfpga-PipelineSimulator, for which you need to create the .vh file. We next explain how you can do it in the context of the RVfpga course for one of the examples provided in those materials.

1. Download [“RVfpga: Understanding Computer Architecture”](https://university.imgtec.com/rvfpga-download-page-en/), the whole *RVfpga-sim-addons* folder and the **RVfpga_PipelineSimulator_Ubuntu** or **RVfpga_PipelineSimulator_Windows** binary from the releases. Give execution permisions to the binary and move it to the *RVfpga-sim-addons/RVfpga_PipelineSimulator/examples* folder..

2. Install VSCode and PlatformIO as explained in Section 2.A of the Getting Started Guide (you can skip the final part of the installation related with Nexys A7 board drivers).

3. Open in PlatformIO the ADD_Instruction example from Lab 12. Insert, before the end of the test loop, the control instruction (and t2, t4, t5) that we use in our simulator for stopping execution and continuing cycle by cycle.

4. Compile the program by clicking on "Generate Trace". Altough the process will fail, the firmware.vh file will be created inside *RVfpga/Labs/Lab12/ADD_Instruction/.pio/build/swervolf_nexys*. A file called firmware.dis will also be created in the same directory, which contains the dissasembly program that can be useful for the simulation analysis.

5. Follow the steps indicated above using the new .vh file to simulate the new program.  


### **2nd Option (only available for Ubuntu)**

(The following steps are illustrated in this [example video](https://drive.google.com/file/d/1e2myDKTp95RUeqxO9j_w_qbDGcPwPdXR/view?usp=sharing))

The **RVfpga-PipelineSimulator** can be integrated in the IDE used in RVfpga, which allows you to easily simulate any other program. However, currently this option only works in a Ubuntu OS (we plan to extend it to Windows). Follow the next steps to simulate the ADD_Instruction example from Lab 12 (you could do the same with any other program):

1. Download [“RVfpga: Understanding Computer Architecture”](https://university.imgtec.com/rvfpga-download-page-en/), the whole *RVfpga-sim-addons* folder and the **RVfpga_PipelineSimulator_Ubuntu** binary from the releases. Give execution permisions to the binary and move it to the *RVfpga-sim-addons/RVfpga_PipelineSimulator/examples* folder.

2. Install VSCode and PlatformIO as explained in Section 2.A of the Getting Started Guide (you can skip the final part of the installation related with Nexys A7 board drivers).

3. Open in PlatformIO the ADD_Instruction example from Lab 12. Insert, before the end of the test loop, the control instruction (and t2, t4, t5) that we use in our simulator for stopping execution and continuing cycle by cycle.

4. Replace file *~/.platformio/platforms/chipsalliance/builder/main.py* with the same file provided at *RVfpga-sim-addons/main.py*, which includes a new option for launching the simulator. Close VSCode and open it again for the options to refresh. (This step will not be necessary after we update the ChipsAlliance platform.)

5. Update the path to the simulator in the *board_debug.verilator.binary* option in file platformio.ini. You can find more details about this in Figure 82 of the RVfpga Getting Started Guide.

6. Launch the simulator by clicking on "RVfpga-ViDBo/Pipeline" from the *Project Tasks* window. The simulator will open in an independent window and you'll be able to simulate the program as described above.


