# Lab 0 - Introduction and Installation
This lab aims to prepare our computer to work in the labs of the course and to introduce the tools that we will use in the labs. Follow the next steps:

1. Install the Virtual Machine as explained below at section [Virtual Machine](https://github.com/artecs-group/RVfpga-sim-addons/blob/main/Computer_Organization_25-26/Lab0/README.md#virtual-machine), or alternatively install a fresh Ubuntu machine as explained below at section [Alternative Installation for Windows Users: Native Ubuntu 22.04 (Dual Boot)](https://github.com/artecs-group/RVfpga-sim-addons/blob/main/Computer_Organization_25-26/Lab0/README.md#alternative-installation-for-windows-users-native-ubuntu-2204-dual-boot).

2. Download the sources as explained below at section [RVfpga Sources](https://github.com/artecs-group/RVfpga-sim-addons/blob/main/Computer_Organization_25-26/Lab0/README.md#rvfpga-sources).


## Virtual Machine
> You can visualize the following video from time 0:0 to time 1:45 to see the steps described in this section: [RVfpgaToolsVideo](https://www.youtube.com/watch?v=Z8QcQRW7F4s).

In these labs we are going to work with a Virtual Machine (VM) with Ubuntu 22.04 Linux Operating System (OS). The VM belongs to the RVfpga training package, on which these practices are based. Download the VM from one of the following links. Both refer to the same VM, so use the one that works best for you: 
+ [Virtual Machine 1st link](https://drive.google.com/file/d/1KFnJYq6krB7vYt_AqTB_zTYVmxfATwJF/view)
+ [Virtual Machine 2nd link](https://pvr-sdk-live.s3.amazonaws.com/iup/ubuntu-22-RVfpga.ova)

The file is very large. You must download it with a good Internet connection and you must make sure that the file is downloaded completely, otherwise the VM will not install correctly. 
For example, the following figure shows the downloaded VM on a laptop with Windows 11 OS (note that it occupies more than 12 GB).

<p align="center">
  <img src="https://github.com/user-attachments/assets/3e2e5eea-0eb5-4c78-b577-e00844b8cc20" width="70%">
</p>

The VM can be installed in the usual virtualization software, such as VMWare or VirtualBox. Install one of those programs and import the VM.

Finally, run the VM, check that the boot is successful, and log into Linux using the user and password **rvfpga**. If the boot gives problems, try changing the USB version of the VM from 2.0 to 1.1, the memory amount used by the VM, or reinstalling the Guest Additions.

Ignore all Ubuntu upgrade proposal windows, Guest Additions, PlatformIO, etc. that open automatically on the VM.

Once you have completed these steps, skip the following section and continue with the [RVfpga Sources](https://github.com/artecs-group/RVfpga-sim-addons/blob/main/Computer_Organization_25-26/Lab0/README.md#rvfpga-sources) section below.


## Alternative Installation for Windows Users: Native Ubuntu 22.04 (Dual Boot)

> **⚠️ Warning:** These installation instructions are new for the 2026–27 course and have not yet been fully tested, so they may contain mistakes or omissions. Students trying them out are encouraged to contact the instructor for assistance and to report any issues or errata they encounter.

If you are using Windows and prefer to work natively on Ubuntu instead of using a virtual machine, you can install **Ubuntu 22.04** alongside Windows using a **dual‑boot** configuration. This allows you to keep your existing Windows installation while booting into Ubuntu whenever you want to work with RVfpga.

> **⚠️ Important:** Before installing a dual-boot system, **back up all important files** stored on your Windows installation. Although the installation process is generally safe when performed correctly, mistakes during disk partitioning or bootloader installation may result in data loss or make Windows temporarily unbootable. Having a recent backup ensures that your data can be recovered if something goes wrong.

Follow the next steps:

1. Download the Ubuntu 22.04 Desktop image: [Ubuntu 22.04.5 LTS (64-bit)](https://releases.ubuntu.com/22.04/ubuntu-22.04.5-desktop-amd64.iso)

2. Create a bootable USB drive using a tool such as Rufus or Balena Etcher.

3. Install Ubuntu by following a dual-boot tutorial. For example: [How to Dual Boot Ubuntu 22.04 LTS and Windows 10](https://www.youtube.com/watch?v=GXxTxBPKecQ)

4. Launch Ubuntu and follow the RVfpga installation procedure described in: [Installing the RVfpga Tools in a Clean Ubuntu Environment](https://drive.google.com/file/d/1WKjvM18EdGsICj_fqLM_Gq4MjyDzGp1T/view)

Once you have completed these steps, continue with the [RVfpga Sources](https://github.com/artecs-group/RVfpga-sim-addons/blob/main/Computer_Organization_25-26/Lab0/README.md#rvfpga-sources) section below.

> **⚠️ Note:** Throughout the rest of the labs, any reference to the **virtual machine (VM)** should be interpreted as referring to your **native Ubuntu installation**.



## RVfpga Sources
> You can visualize the following video from time 1:45 to time 3:10 to see the steps described in this section: [RVfpgaToolsVideo](https://youtu.be/Z8QcQRW7F4s?si=-LpPqGG2L8ovLKRd&t=104).

Once the Virtual Machine (VM) is installed in your system, all labs will be developed in it. So, from inside the VM, download the following file and unzip it in the VM home directory: [SimulatorsAndProjects_26-27](https://drive.google.com/file/d/1PztrAxSVNpHJT0SWqHd8M0k2ITHElTLd/view?usp=sharing).

<!--
>The sources used last year are almost the same and are available here: [SimulatorsAndProjects_25-26](https://drive.google.com/file/d/1CctkpRvmTS4PsdsKVPTHpT6g6qnUm3WH/view?usp=sharing).
-->


<!--
> OPTIONAL: This is an enhanced version of the 24-25 sources ([SimulatorsAndProjects_24-25](https://drive.google.com/file/d/1hbCSFmjIoGmXq4r5G12_AMUKezHXA6A-/view?usp=sharing)). Keep in mind that, although the 25-26 version that you will use in this course provides a more complete and polished interface, it is not fully aligned with the images and videos used in the demo materials. Main improvements of the 25-26 version:  
>  
> - Improved aesthetics: cleaner layout, refined colors and fonts.  
> - “-1 Cycle” button: allows going back one cycle.  
> - Forwarding arrows: red dashed arrows show data forwarding paths. Supported forwardings:  
>   - From EX2/EX3/Commit/WB to Decode.  
>   - From DC3 (LSU) to M1 (Multiplier).  
>   - From EX2 (ALU) to DC2 (Store).  
>   - From DC3 (Load) to DC2 (Store).  
>   - Secondary-ALU forwardings: partially supported. Forwarding paths involving the Secondary ALU (e.g., Commit/WB to EX2/EX3 for ALU and branch instructions) are now displayed.
Some cases (such as Secondary ALU to sw (rs2) in DC3) are still work in progress.
> - Highlighted datapaths: occupied pipeline stages are emphasized with colored rectangles.  
> - Instruction display: the current instruction is shown inside each highlighted rectangle.  
-->

Once you have downloaded the file, you can open a file explorer, move the downloaded file to the OS home, and click on the file with the right mouse button and then “Extract Here”.

<p align="center">
  <img 
    src="https://github.com/user-attachments/assets/69387930-92de-4f9b-8902-0ed68f427bcb"
    width="70%">
</p>

At this point your system is ready to run, inside the Virtual Machine, all the exercises from the RVfpga package as well as the Ripes simulator.

<p align="center">
  <img 
    src="https://github.com/user-attachments/assets/757c306e-841d-4715-9b63-d8ad67d0880d"
    width="40%">
</p>
