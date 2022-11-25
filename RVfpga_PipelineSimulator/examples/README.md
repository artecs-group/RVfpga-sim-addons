## **Ubuntu 20/22**

(The following steps are illustrated in this [example video](https://drive.google.com/file/d/1fX9cWZdV_GF7UTNUp-tYYD5TfJakeJai/view?usp=sharing))

Follow the next steps to run the Test program in the RVfpga_PipelineSimulator:

1. Open a terminal and go into the current folder.
2. Launch the simulation of the example program and analyse the program cycle by cycle (using Ubuntu 20.04 version):
```
<path-to-binary-file>/RVfpga_PipelineSimulator_Ubuntu +ram_init_file=Test/Test.vh
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Note that it may be necessary to give execution permisions to the simulator binary file.

___


## **Windows**

(The following steps are illustrated in this [example video](https://drive.google.com/file/d/1yGHDSitvdZiQzkdsvL0qKYCGUTGjoR33/view?usp=sharing))

Follow the next steps:

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

2. Open a cygwin terminal. Go into the current folder. Run the following command:

```
startx <path-to-binary-file>/RVfpga_PipelineSimulator_Windows.exe +ram_init_file=Test/Test.vh
```

___


## **Simulate other programs**

(The following steps are illustrated in this [example video](https://drive.google.com/file/d/1beJl3NIKAPqtg3ozgQWo37VdkAPXRUQc/view?usp=sharing))

You can simulate any other program in RVfpga-PipelineSimulator, for which you need to create the .vh file. We next explain how you can do it in the context of the RVfpga course for one of the examples provided.

1. Download [“RVfpga: Understanding Computer Architecture”](https://university.imgtec.com/rvfpga-download-page-en/).

2. Install VSCode and PlatformIO as explained in Section 2.A of the Getting Started Guide (you can skip the final part of the installation related with Nexys A7 board drivers).

3. Open in PlatformIO the ADD_Instruction example from Lab 12. Insert, before the end of the test loop, the control instruction (and t2, t4, t5) that we use in our simulator for stopping execution and continuing cycle by cycle.

4. Compile the program by clicking on "Generate Trace". Altough the process will fail, the firmware.vh file will be created inside *RVfpga/Labs/Lab12/ADD_Instruction/.pio/build/swervolf_nexys*.

5. Follow the steps indicated above using the new .vh file to simulate the new program.
