## **Compilation of RVfpga-PipelineSimulator in Ubuntu**

(The following steps are illustrated in this [example video](https://drive.google.com/file/d/18HBC6PZoAHl9H2Vwr7f_d41loH18VwgV/view?usp=share_link))

Follow the next steps to compile the simulator in your Ubuntu 22.04 OS:

1. Download the whole *RVfpga-sim-addons* folder as well as [RVfpga: Understanding Computer Architecture](https://university.imgtec.com/rvfpga-download-page-en/).

2. Copy the *src* folder containing the RVfpga System into the *RVfpga-sim-addons* folder.

3. In a terminal, go into the *RVfpga-sim-addons* folder and apply the provided patch to the src folder by running the following command:

```
patch -p0 < Patch_src
```

4. Install the following packages: 

```
sudo apt-get install make verilator g++ libcairo2-dev libgtk-3-dev libsdl-pango-dev
```

5. In the terminal, go into folder *RVfpga-sim-addons-main/RVfpga_PipelineSimulator/verilatorSIM_RVfpga-PipelineSimulator* and compile the simulator by running:

```
make
```

You should obtain a binary file called ***Vrvfpgasim*** which is the **RVfpga-PipelineSimulator** and that you can use as explained in the examples folder.

___

## **Compilation of RVfpga-PipelineSimulator in Windows**

(The following steps are illustrated in this [example video](https://drive.google.com/file/d/1wMNF6T07eCiFiJzH4IhsWFmg4LTTfJ68/view?usp=sharing))

Follow the next steps to compile the simulator in your Windows OS:

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
    * libcairo-devel
    * libcairo2
    * patch

2. Download the whole *RVfpga-sim-addons* folder as well as [RVfpga: Understanding Computer Architecture](https://university.imgtec.com/rvfpga-download-page-en/).

3. Copy the *src* folder containing the RVfpga System into the *RVfpga-sim-addons* folder.

4. In a cygwin terminal, go into the *RVfpga-sim-addons* folder (you can go into your Windows user by running: ``` cd /cygdrive/c/Users/<your-user> ```) and apply the provided patch to the *src* folder by running the following command:

```
patch.exe -p0 < Patch_src
```

5. Install Verilator as explained in Appendix C of the RVfpga Getting Started Guide.

6. In the cygwin terminal, go into folder *RVfpga-sim-addons-main/RVfpga_PipelineSimulator/verilatorSIM_RVfpga-PipelineSimulator*, and copy file *glibconfig.h* (provided in this folder) to */usr/include/glib-2.0/*:

```
cp glibconfig.h /usr/include/glib-2.0/
```

7. In the cygwin terminal, in the same folder (*RVfpga-sim-addons-main/RVfpga_PipelineSimulator/verilatorSIM_RVfpga-PipelineSimulator*), compile the simulator by running:

```
make
```

You should obtain a binary file called ***Vrvfpgasim.exe*** which is the **RVfpga-PipelineSimulator** and that you can use as explained in the examples folder.
