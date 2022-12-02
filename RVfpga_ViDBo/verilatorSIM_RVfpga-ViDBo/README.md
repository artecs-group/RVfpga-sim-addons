## **Compilation of RVfpga-ViDBo in Ubuntu**

(The following steps are illustrated in this [example video](https://drive.google.com/file/d/1k2nV0DwbfJ-FskXy-967qKRxBtgQzVX2/view?usp=sharing))

Follow the next steps to compile the simulator in your Ubuntu 22.04 OS:

1. Download the whole *RVfpga-sim-addons* folder as well as [RVfpga: Understanding Computer Architecture](https://university.imgtec.com/rvfpga-download-page-en/).

2. Copy the *src* folder containing the *RVfpga System* into the *RVfpga-sim-addons* folder.

3. In a terminal, go into the *RVfpga-sim-addons* folder and apply the provided patch to the *src* folder by running the following command:

```
patch -p0 < Patch_src
```

4. Install the following packages: 

```
sudo apt-get install make libwebsockets-dev verilator g++
```

5. In the terminal, go into folder *RVfpga-sim-addons-main/RVfpga_ViDBo/verilatorSIM_RVfpga-ViDBo* and compile the simulator by running:

```
make
```

You should obtain a binary file called ***Vrvfpgasim*** which is the **RVfpga-ViDBo** simulator and that you can use as explained in the examples folder.

___

## **Compilation of RVfpga-ViDBo in Windows**

(The following steps are illustrated in this [example video](https://drive.google.com/file/d/1nVsdJnBaPgrEnqjsRWPUYbjo1tNXbUu_/view?usp=sharing))

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
    * libssl-devel
    * cmake

2. Download the whole *RVfpga-sim-addons* folder as well as [RVfpga: Understanding Computer Architecture](https://university.imgtec.com/rvfpga-download-page-en/).

3. Download the websockets library compiled for Windows, which is provided in Releases as a zip file called *LibWebSockets_Windows10.zip*. (At the end of this section we include as an Appendix the steps that we've followed for compiling this library for Windows.)
   - Unzip the file, go into folder *LibWebSockets_Windows10* and copy the whole *libwebsockets* folder into the current folder (*RVfpga-sim-addons-main/RVfpga_ViDBo/verilatorSIM_RVfpga-ViDBo*).
   - Then, add to the PATH environment system variable the route to folder *RVfpga-sim-addons-main/RVfpga_ViDBo/verilatorSIM_RVfpga-ViDBo/libwebsockets/build/bin*.
   - Finally, in a Cygwin terminal (you can go into your Windows user by running: ``` cd /cygdrive/c/Users/<your-user> ```), go into the current folder and copy the library to the Cygwin System:

```
      cp libwebsockets/build/lib/libwebsockets.dll.a /usr/lib/gcc/x86_64-pc-cygwin/10/
      cp libwebsockets/build/lib/libwebsockets.a /usr/lib/gcc/x86_64-pc-cygwin/10/
```


4. Restart your computer.

5. Copy the *src* folder containing the RVfpga System into the *RVfpga-sim-addons* folder.

6. In a cygwin terminal, go into the *RVfpga-sim-addons* folder (you can go into your Windows user by running: ``` cd /cygdrive/c/Users/<your-user> ```) and apply the provided patch to the *src* folder by running the following command:

```
patch.exe -p0 < Patch_src
```

7. Install Verilator as explained in Appendix C of the RVfpga Getting Started Guide.


8. In the cygwin terminal, go into folder *RVfpga-sim-addons-main/RVfpga_ViDBo/verilatorSIM_RVfpga-ViDBo* and compile the simulator by running:

```
make
```

You should obtain a binary file called ***Vrvfpgasim.exe*** which is the **RVfpga-ViDBo** simulator and that you can use as explained in the examples folder.


# **Appendix: Compilation of LibWebSockets in Windows**

Follow the next steps to compile the LibWebSockets for a Windows OS. We assume that Cygwin is already installed as explained in step 1 above:

1. Go into the folder where you want to place the sources and download them with the following command:

```
git clone https://libwebsockets.org/repo/libwebsockets
```

2. Open file *libwebsockets/CMakeLists.txt* in an editor and remove the *-Werror* option.

Change ```set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Werror")``` to ```set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS}")```

3. Two header files are missing in the current version of Cygwin. To resolve this problem, download [cygwin-alternative](https://github.com/rinrin-/cygwin-alternative.git) and, in a Cygwin terminal, copy files *route.h* and *radix.h* from *cygwin-alternative-master/newlib/libc/sys/linux/include/net/* to */usr/include/net*.

4. Compile libwebsockets:
   - ```cd libwebsockets```
   - ```mkdir build```
   - ```cd build```
   - ```cmake ..```
   - ```cmake --build . --config DEBUG```
