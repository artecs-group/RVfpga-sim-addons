# Lab 0 - Introduction and Installation
This lab aims to prepare our computer to work in the labs of the course and to introduce the Tools that we will use in the labs. Follow the next steps:

1. Install the Virtual Machine as explained below at section *Virtual Machine*. If you are using one of the FdI laptops, you can skip this stage and simply launch the pre-installed VM.

2. Download the sources as explained below at section *Simulators and Example Projects*.


## Virtual Machine
*You can visualize the following video from time 0:0 to time 1:45 to see the steps described in this section: [RVfpgaToolsVideo](https://www.youtube.com/watch?v=Z8QcQRW7F4s).

In these labs we are going to work with a Virtual Machine (VM) with Ubuntu 22.04 Linux Operating System (OS). This VM can run on most native OS (Windows, Linux, macOS with Intel processors); however, if you are using an Apple Silicon MacBook (M1, M2, M3, …), you will not be able to run this VM. 

<!--In that case, follow the alternative instructions provided at the end of this section.-->

The VM belongs to the RVfpga training package, on which these practices are based. Download the VM from one of the following links. Both refer to the same VM, so use the one that works best for you: 
+ [Virtual Machine 1st link](https://drive.google.com/file/d/1KFnJYq6krB7vYt_AqTB_zTYVmxfATwJF/view)
+ [Virtual Machine 2nd link](https://pvr-sdk-live.s3.amazonaws.com/iup/ubuntu-22-RVfpga.ova)

The file is very large. You must download it with a good Internet connection and you must make sure that the file is downloaded completely, otherwise the VM will not install correctly. 
For example, the following figure shows the downloaded VM on a laptop with Windows 11 OS (note that it occupies more than 12 GB).

<img width="1421" height="510" alt="image" src="https://github.com/user-attachments/assets/3e2e5eea-0eb5-4c78-b577-e00844b8cc20" />


The VM can be installed in the usual virtualization software, such as VirtualBox or VMWare. Install one of those programs and import the VM (the screenshots in this tutorial are for VirtualBox).

Finally, run the VM, check that the boot is successful, and log into Linux using the user and password **rvfpga**. If the boot gives problems, try changing the USB version of the VM from 2.0 to 1.1, or the memory amount used by the VM.

Ignore all Ubuntu upgrade proposal windows, Guest Additions, PlatformIO, etc. that open automatically on the VM.

**Installation on a fresh Ubuntu OS:** If you want to install the simulators on a fresh Ubuntu OS, either running natively or within a Virtual Machine, follow these steps:

1. Create your own Ubuntu Virtual Machine. You can use Ubuntu 22.04 or any more recent version. If needed, you can search for a tutorial on how to create a Virtual Machine on the Internet; for example: [InstallUbuntuVM_AppleSilicon](https://youtu.be/LjL_N0OZxvY?si=9XgG6DPLE9i1Oxan).  
2. Follow these instructions to install Ripes and VSCode+PlatformIO on the Virtual Machine: [InstallSimulators](https://drive.google.com/file/d/1id4hHDzWmkNvIn-cREG98Ug8tBQSrgLR/view?usp=sharing).


## Simulators and Example Projects
*You can visualize the following video from time 1:45 to time 3:10 to see the steps described in this section: [RVfpgaToolsVideo](https://youtu.be/Z8QcQRW7F4s?si=-LpPqGG2L8ovLKRd&t=104).

Once the Virtual Machine (VM) is installed in your system, all labs will be developed in it. So, from inside the VM, download the following file and unzip it in the VM home directory: [SimulatorsAndProjects](https://drive.google.com/file/d/1hbCSFmjIoGmXq4r5G12_AMUKezHXA6A-/view?usp=sharing).

To do this you can open a file explorer, move the downloaded file to the OS home, and click on the file with the right mouse button and then “Extract Here”.

<img width="1120" height="714" alt="image" src="https://github.com/user-attachments/assets/965a2a25-f6ff-4620-a84e-754d43403a29" />

In the following screenshot you can see how RVfpga should be located in the VM. It is important that you respect this location in order to avoid problems with the paths indicated in the labs.

<img width="949" height="338" alt="image" src="https://github.com/user-attachments/assets/3afdcf73-84e1-48d7-8b62-1cfd069c4b85" />

At this point your system is ready to run, inside the Virtual Machine, all the exercises from the RVfpga package as well as the Ripes simulator.
