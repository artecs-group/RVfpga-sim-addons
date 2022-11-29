## **Ubuntu 20/22**

(The following steps are illustrated in this [example video](https://drive.google.com/file/d/1fX9cWZdV_GF7UTNUp-tYYD5TfJakeJai/view?usp=sharing))

Follow the next steps to run the Test program in the RVfpga_PipelineSimulator:

1. Download the whole *RVfpga-sim-addons* folder as well as the **RVfpga_PipelineSimulator_Ubuntu** binary from the releases.

2. Open a terminal and go into the current folder (*RVfpga-sim-addons/RVfpga_PipelineSimulator/examples*).

3. Launch the simulation of the Test program:
```
<path-to-binary-file>/RVfpga_PipelineSimulator_Ubuntu +ram_init_file=Test/Test.vh
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(Note that it may be necessary to give execution permisions to the simulator binary file.)

4. Execution will stop at the end of the endless loop (where our program includes a control instruction- and t2, t4, t5- that makes simulation stop), and you'll be able to analyse the execution of the program cycle by cycle in the SweRV EH1 processor from that point (remember that you can view the program that you are simulating in file Test/Test.S). Specifically, we are interested in analyzing the following block of instructions (*nop* instructions are included in order to isolate the different iterations), so you can fast forward several cycles and then analyze those instructions carefully cycle-by-cycle:

```c
         add t3, t3, t3        
         add t3, t3, t3
         mul t3, t3, t4
         mul t5, t5, t5
         lw t3, 4(t0)
         lw t3, (t1)
```

___


## **Windows**

(The following steps are illustrated in this [example video](https://drive.google.com/file/d/1yGHDSitvdZiQzkdsvL0qKYCGUTGjoR33/view?usp=sharing))

Follow the next steps to run the Test program in the RVfpga_PipelineSimulator:

1. Install cygwin as explained in Appendix C of the RVfpga Getting Started Guide. Install all the packages stated in that document plus some other packages needed for the two new simulators:

    * git
    * make 
    * autoconf
    * gcc-core 
    * gcc-g++ 
    * flex
    * bison
    * perl
    * libargp-devel
    * python3
    * xorg-server
    * xinit
    * libgtk3-devel

2. Download the whole RVfpga-sim-addons folder as well as the **RVfpga_PipelineSimulator_Windows** binary from the releases

3. Open a cygwin terminal. Go into the current folder (*RVfpga-sim-addons/RVfpga_PipelineSimulator/examples*). Run the following command:

```
startx <path-to-binary-file>/RVfpga_PipelineSimulator_Windows.exe +ram_init_file=Test/Test.vh
```

4. Execution will stop at the end of the endless loop (where our program includes a control instruction- and t2, t4, t5- that makes simulation stop), and you'll be able to analyse the execution of the program cycle by cycle in the SweRV EH1 processor from that point (remember that you can view the program that you are simulating in file Test/Test.S). Specifically, we are interested in analyzing the following block of instructions (*nop* instructions are included in order to isolate the different iterations), so you can fast forward several cycles and then analyze those instructions carefully cycle-by-cycle:

```c
         add t3, t3, t3        
         add t3, t3, t3
         mul t3, t3, t4
         mul t5, t5, t5
         lw t3, 4(t0)
         lw t3, (t1)
```

___


## **Simulate other programs**

(The following steps are illustrated in this [example video](https://drive.google.com/file/d/1beJl3NIKAPqtg3ozgQWo37VdkAPXRUQc/view?usp=sharing))

You can simulate any other program in RVfpga-PipelineSimulator, for which you need to create the .vh file. We next explain how you can do it in the context of the RVfpga course for one of the examples provided.

1. Download [“RVfpga: Understanding Computer Architecture”](https://university.imgtec.com/rvfpga-download-page-en/).

2. Install VSCode and PlatformIO as explained in Section 2.A of the Getting Started Guide (you can skip the final part of the installation related with Nexys A7 board drivers).

3. Open in PlatformIO the ADD_Instruction example from Lab 12. Insert, before the end of the test loop, the control instruction (and t2, t4, t5) that we use in our simulator for stopping execution and continuing cycle by cycle.

4. Compile the program by clicking on "Generate Trace". Altough the process will fail, the firmware.vh file will be created inside *RVfpga/Labs/Lab12/ADD_Instruction/.pio/build/swervolf_nexys*. A file called firmware.dis will also be created in the same directory, which contains the dissasembly program that can be useful for the simulation analysis.

5. Follow the steps indicated above using the new .vh file to simulate the new program.
