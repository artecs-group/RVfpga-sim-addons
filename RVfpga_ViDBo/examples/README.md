## **Running RVfpga-ViDBo in a Ubuntu 20/22 OS**

(The following steps are illustrated in this [example video](https://drive.google.com/file/d/1zgGUX6UYnExh1JYof4PiJ6gxi6pZvngT/view?usp=sharing))

For using this simulator in Ubuntu it is required to first install websockets library: 

```
sudo apt-get install -y libwebsockets-dev
```

Then, follow the next steps to run the *LedsSwitches* program in the **RVfpga_ViDBo** simulator:

1. Download the whole *RVfpga-sim-addons* folder as well as the *RVfpga_ViDBo_Ubuntu20* / *RVfpga_ViDBo_Ubuntu22* binary from the releases (the former is for Ubuntu 20.04 whereas the latter is for Ubuntu 22.04). Give execution permisions to the binary and move it to the *RVfpga-sim-addons/RVfpga_ViDBo/examples* folder.

2. Open a terminal and go into the *RVfpga-sim-addons/RVfpga_ViDBo/examples* folder. Run the Verilator-simulator using the following command: 

      In Ubuntu 20:04: ```./RVfpga_ViDBo_Ubuntu20 +ram_init_file=LedsSwitches/LedsSwitches.vh```

      In Ubuntu 22:04: ```./RVfpga_ViDBo_Ubuntu22 +ram_init_file=LedsSwitches/LedsSwitches.vh```

3. Open another terminal and go into the same folder (*RVfpga-sim-addons/RVfpga_ViDBo/examples*). Run the virtual board using the following command:
```
      python3 -m http.server --directory ../NexysA7board/
```
4. Open a browser and connect to `http://localhost:8000/nexys-a7.html`

5. On the browser, click on "connect to the board" and test the program. If you click on any of the 16 switches its state will invert as well as the state of the corresponding LED (you can analyze the program by opening file *LedsSwitches/LedsSwitches.vh* in an editor).


___


## **Running RVfpga-ViDBo in a Windows 10 OS**

We next provide two options for running the simulator in Windows; choose the one that better fits your needs. The first one is simpler, as it avoids installing Cygwin; the second one is a bit more tedious but allows you to prepare Cygwin in case you want to later modify and recompile the simulator as explained in *RVfpga-sim-addons/RVfpga_ViDBo/verilatorSIM_RVfpga-ViDBo*.

### **1st option - Not using CygWin**

(The following steps are illustrated in this [example video](https://drive.google.com/file/d/1eizsoL2JIYWqo36trlnzbXbkPHjk2uhE/view?usp=sharing))

Follow the next steps:

1. Download the whole *RVfpga-sim-addons* folder as well as the **RVfpga_ViDBo_Windows.zip** file from the releases. Move the **RVfpga_ViDBo_Windows.zip** file into the *RVfpga-sim-addons/RVfpga_ViDBo/examples* folder and unzip it. The zip contains one .exe file and several .dll files required by the executable.

2. Open a cmd and go into the *RVfpga-sim-addons/RVfpga_ViDBo/examples* folder. Run the following command:
```
      RVfpga_ViDBo_Windows.exe +ram_init_file=LedsSwitches/LedsSwitches.vh
```

3. Install Python 3 as explained [here](https://phoenixnap.com/kb/how-to-install-python-3-windows).

4. Open another cmd and go into the *RVfpga-sim-addons/RVfpga_ViDBo/examples* folder. Then run: 

```
      python -m http.server --directory ../NexysA7board/
```

5. Open a browser and connect to: ```http://localhost:8000/nexys-a7.html```

6. On the browser, go into nexys-a7.html, connect to the board by clicking on the corresponding button, and test the program. If you invert a switch the corresponding LED should also invert its state.



### **2nd option - Using CygWin**

(The following steps are illustrated in this [example video](https://drive.google.com/file/d/1_jsrZ2zuCW3KN73M03rk-F63tagk3Ew8/view?usp=sharing))

Follow the next steps:

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

2. Include the websockets library compiled for Windows, which is provided in Releases as a zip file called *LibWebSockets_Windows10.zip*. For that purpose, unzip the file and add to the PATH environment system variable the route to folder *LibWebSockets_Windows10/libwebsockets/build/bin*.

3. Restart your computer.

4. Download the whole *RVfpga-sim-addons* folder as well as the **RVfpga_ViDBo_Windows.exe** binary from the releases.

5. Open a cygwin terminal and go into the *RVfpga-sim-addons/RVfpga_ViDBo/examples* folder (you can go into your Windows user by running: ``` cd /cygdrive/c/Users/<your-user> ```). Run the following command:

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


## **Simulating other programs - Integration in VSCode/PlatformIO**

(The following steps are illustrated for a Ubuntu 22.04 OS in this [example video](https://drive.google.com/file/d/1acz5ryLr4lSQrhkxgkVh4TNLSd-3IfUG/view?usp=sharing))

(The following steps are illustrated for a Windows 10 OS in this [example video](https://drive.google.com/file/d/1xWhrrMHu0FtmryNyeUQSjv4m489yKYGO/view?usp=sharing))

The **RVfpga-ViDBo** can be integrated in the IDE used in RVfpga, which allows you to easily simulate any other program. This can be done both in Ubuntu and in Windows. Follow the next steps to simulate the Hello World program provided in RVfpga (you could do the same with any other program):

1. Download [“RVfpga: Understanding Computer Architecture”](https://university.imgtec.com/rvfpga-download-page-en/), the whole *RVfpga-sim-addons* folder and the **RVfpga_ViDBo** simulator binary from the releases (choose the appropriate one for your OS: *RVfpga_ViDBo_Ubuntu20*, *RVfpga_ViDBo_Ubuntu22* or *RVfpga_ViDBo_Windows.zip*). Move the simulator binary to the *RVfpga-sim-addons/RVfpga_ViDBo/examples* folder (in Windows, uncompress the file to obtain the executable and libraries used by it).

2. Install VSCode and PlatformIO as explained in Section 2.A of the Getting Started Guide (you can skip the final part of the installation related with Nexys A7 board drivers).

3. Open in PlatformIO the *HelloWorld* example (this program is provided in the *examples* folder of RVfpga and described in Section 6.F of the Getting Started Guide). Reduce the delay in the .c file, as it is prepared for running on the Nexys A7 board, but the simulator is much slower.

4. Replace file *~/.platformio/platforms/chipsalliance/builder/main.py* with the same file provided at *RVfpga-sim-addons/main.py*, which includes a new option for launching the simulator. Close VSCode and open it again for the options to refresh. (This step will not be necessary after we update the ChipsAlliance platform.)

5. Update the path to the simulator in the *board_debug.verilator.binary* option in file platformio.ini. You can find more details about this in Figure 82 of the RVfpga Getting Started Guide.

6. Launch the simulator by clicking on "RVfpga-ViDBo" from the *Project Tasks* window.

7. Follow the steps described above after the launch of the simulator: from step 3 both in Ubuntu and in Windows - 1st option.
