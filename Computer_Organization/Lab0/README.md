# Lab 0 - Installation
This lab aims to prepare our computer to work in the labs of the course.

## Virtual Machine
In these labs we are going to work with a Virtual Machine (VM) with Ubuntu 22.04 Linux Operating System (OS). 
This VM can run on any native OS (Windows, Linux, macOS). 
The VM we will use belongs to the RVfpga training package, on which these practices are based. 
It is not necessary to obtain this package for the practices; however, if you are interested in going deeper into the contents that we are going to study in this course, you can request it through the following link: [RVfpga-v3](https://university.imgtec.com/rvfpga-el2-v3-0-english-downloads-page/).

Download the VM from one of the following links. Both refer to the same VM, so use the one that works best for you: 
+ [Virtual Machine 1st link](https://drive.google.com/file/d/1KFnJYq6krB7vYt_AqTB_zTYVmxfATwJF/view)
+ [Virtual Machine 2nd link](https://pvr-sdk-live.s3.amazonaws.com/iup/ubuntu-22-RVfpga.ova)

The file is very large. You must download it with a good Internet connection and you must make sure that the file is downloaded completely, otherwise the VM will not install correctly. 
For example, the following figure shows the downloaded VM on a laptop with Windows 11 OS (note that it occupies more than 12 GB).

<p align="center">
  <img src="Images/VM_Downloaded.png" width=70% height=70%>
</p>

The VM can be installed in the usual virtualization software, such as VirtualBox or VMWare. Install one of those softwares and import the VM (you can follow a tutorial on the Internet). The screenshots in this tutorial are for VirtualBox.

Finally, run the VM, check that the boot is successful, and log into Linux using the user and password **rvfpga**. If the boot gives problems, try changing the USB version of the VM from 2.0 to 1.1, or the memory amount used by the VM.

Ignore all Ubuntu upgrade proposal windows, Guest Additions, PlatformIO, etc. that open automatically on the VM.

## Simulators and Example Projects
Download the following file from the Virtual Machine and unzip it in the VM home: [SimulatorsAndProjects](https://drive.google.com/file/d/1hbCSFmjIoGmXq4r5G12_AMUKezHXA6A-/view?usp=sharing).

To do this you can open a file explorer, move the downloaded file to the OS home, and click on the file with the right mouse button and then “Extract Here”.

<p align="center">
  <img src="Images/ExtractHere.png" width=70% height=70%>
</p>

In the following screenshot you can see how RVfpga should be located in the VM. It is important that you respect this location in order to avoid problems with the paths indicated in the labs.

<p align="center">
  <img src="Images/Path.png" width=70% height=70%>
</p>

At this point your system is ready to run, inside the Virtual Machine, all the exercises from the RVfpga package as well as the Ripes simulator.
