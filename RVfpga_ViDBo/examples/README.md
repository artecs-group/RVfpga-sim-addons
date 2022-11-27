## **Ubuntu 20/22**

(The following steps are illustrated in this [example video](https://drive.google.com/file/d/1zgGUX6UYnExh1JYof4PiJ6gxi6pZvngT/view?usp=sharing))

For using this simulator in Ubuntu it is required to first install websockets library: 

```
sudo apt-get install -y libwebsockets-dev
```

Then, follow the next steps to run the LedsSwitches program in the RVfpga_ViDBo simulator:

1. Download the whole RVfpga-sim-addons folder as well as the Verilator-simulator binary from the releases that you are going to use, in this case RVfpga_ViDBo_Ubuntu20.

2. Open a terminal and go into the *RVfpga-sim-addons/RVfpga_ViDBo/examples* folder. Run the Verilator-simulator using the following command (this is for Ubuntu 20.04; for Ubuntu 22.04 use binary RVfpga_ViDBo_Ubuntu22): 
```
<path-to-binary-file>/RVfpga_ViDBo_Ubuntu20 +ram_init_file=LedsSwitches/LedsSwitches.vh
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Note that it may be necessary to give execution permisions to the simulator binary file.

3. Open another terminal and go into the same folder (*RVfpga-sim-addons/RVfpga_ViDBo/examples*). Run the virtual board using the following command:
```
python3 -m http.server --directory ../NexysA7board/
```
4. Open a browser and connect to `http://localhost:8000/nexys-a7.html`

5. On the browser, click on "connect to the board" and test the program. If you click on any of the 16 switches its state will invert as well as the state of the corresponding LED.

___


## **Windows**

(The following steps are illustrated in this [example video](https://drive.google.com/file/d/1_jsrZ2zuCW3KN73M03rk-F63tagk3Ew8/view?usp=sharing))

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

2. Include the libwebsockets library compiled for Windows, which is provided in Releases as a zip file. For that purpose, unzip the file and add to the PATH environment system variable the route to the unzipped folder.

3. Restart your computer.

4. Download the whole RVfpga-sim-addons folder as well as the Verilator-simulator binary from the releases that you are going to use, in this case RVfpga_ViDBo_Windows.exe.

5. Open a cygwin terminal and go into the *RVfpga-sim-addons/RVfpga_ViDBo/examples* folder. Run the following command:

```
<path-to-binary-file>/RVfpga_ViDBo_Windows.exe +ram_init_file=LedsSwitches/LedsSwitches.vh
```

6. Open another cygwin terminal and go into the same folder (*RVfpga-sim-addons/RVfpga_ViDBo/examples*). Then run: 

```
python3 -m http.server --directory ../NexysA7board/
```

7. Open a browser and connect to: ```http://localhost:8000/nexys-a7.html```

8. On the browser, go into nexys-a7.html, connect to the board by clicking on the corresponding button, and test the program. If you invert a switch the corresponding LED should also invert its state.


___


## **Simulate other programs**

(The following steps are illustrated in this [example video](https://drive.google.com/file/d/1rVUCEtV2jJZcxwa7RUylmWUISDBItj0E/view?usp=sharing))

You can simulate any other program in RVfpga-ViDBo, for which you need to create the .vh file. We next explain how you can do it in the context of the RVfpga course for one of the examples provided.

1. Download [“RVfpga: Understanding Computer Architecture”](https://university.imgtec.com/rvfpga-download-page-en/).

2. Install VSCode and PlatformIO as explained in Section 2.A of the Getting Started Guide (you can skip the final part of the installation related with Nexys A7 board drivers).

3. Open in PlatformIO the Hello World example. Reduce the delay in the .c file, as the simulator is much slower than the board.

4. Compile the program by clicking on "Generate Trace". Altough the process will fail, the firmware.vh file will be created inside *RVfpga/examples/HelloWorld_C-Lang/.pio/build/swervolf_nexys*.

5. Follow the steps indicated above using the new .vh file to simulate the Hello World program.
