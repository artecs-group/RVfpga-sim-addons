## **Compilation of RVfpga-ViDBo in Ubuntu**

(The following steps are illustrated in this [example video](https://drive.google.com/file/d/1k2nV0DwbfJ-FskXy-967qKRxBtgQzVX2/view?usp=sharing))

Follow the next steps to compile the simulator in your Ubuntu 22.04 OS:

1. Download the whole RVfpga-sim-addons folder as well as [RVfpga: Understanding Computer Architecture](https://university.imgtec.com/rvfpga-download-page-en/).

2. Copy the src folder containing the RVfpga System into the RVfpga-sim-addons folder.

3. In a terminal, go into the RVfpga-sim-addons folder and apply the provided patch to the src folder by running the following command:

```
patch -p0 < Patch_src
```

4. Install the following packages: 

```
sudo apt-get install make
sudo apt-get install -y libwebsockets-dev
sudo apt-get install verilator
sudo apt-get install g++
```

5. In the terminal, go into folder RVfpga-sim-addons-main/RVfpga_ViDBo/verilatorSIM_RVfpga-ViDBo and compile the simulator by running:

```
make
```

You should obtain a binary file called Vrvfpgasim which is the RVfpga-ViDBo simulator and that you can use as explained in the examples folder.

___

## **Compilation of RVfpga-ViDBo in Windows**

Follow the next steps to compile the simulator in your Windows OS:

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
    * libcairo-devel
    * libcairo2
    * patch
    * libssl-devel

2. Download the whole RVfpga-sim-addons folder as well as [RVfpga: Understanding Computer Architecture](https://university.imgtec.com/rvfpga-download-page-en/).

3. Download the libwebsockets library compiled for Windows, which is provided in Releases as a zip file called LibWebSockets_Windows10.zip. Unzip the file and move the whole folder (*LibWebSockets_Windows10*) into the current folder (*<path-to-folder>/RVfpga-sim-addons-main/RVfpga_ViDBo/verilatorSIM_RVfpga-ViDBo*). Then, add to the PATH environment system variable the route to folder *<path-to-folder>/RVfpga-sim-addons-main/RVfpga_ViDBo/verilatorSIM_RVfpga-ViDBo/LibWebSockets_Windows10/libwebsockets/build/bin*.

4. Restart your computer.

5. Copy the src folder containing the RVfpga System into the RVfpga-sim-addons folder.

6. In a cygwin terminal, go into the RVfpga-sim-addons folder and apply the provided patch to the src folder by running the following command:

```
patch.exe -p0 < Patch_src
```

7. Install Verilator as explained in Appendix C of the RVfpga Getting Started Guide.


8. In the cygwin terminal, go into folder RVfpga-sim-addons-main/RVfpga_ViDBo/verilatorSIM_RVfpga-ViDBo and compile the simulator by running:

```
make
```

You should obtain a binary file called Vrvfpgasim.exe which is the RVfpga-ViDBo simulator and that you can use as explained in the examples folder.
