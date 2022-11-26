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
