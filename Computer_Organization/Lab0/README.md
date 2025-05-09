# Lab 0 - Introduction and Installation
This lab aims to prepare our computer to work in the labs of the course and to introduce the RVfpga System and the Tools that we will use in the labs.

The [RISC-V FPGA](https://university.imgtec.com/rvfpga-el2-v3-0-english-downloads-page/) (RVfpga) course in computer architecture is a freely available course that provides hands-on understanding of a commercial RISC-V processor, a RISC-V system-on-chip (SoC), and the RISC-V ecosystem. These materials bridge the gap between the availability of the open RISC-V ISA and actually being able to use and experiment with a commercial RISC-V processor/SoC and the RISC-V toolchain. In addition to providing the VeeR EH1/EL2-based SoC source code in Verilog/SystemVerilog, RVfpga shows how to install and use the RISC-V toolchain to compile, debug, and run C and RISC-V assembly programs on the SoC, use and modify the I/O System, and understand and modify the SoC microarchitecture and memory hiearchy. A second package, the [RVfpga-SoC](https://university.imgtec.com/rvfpgasoc-download-page-en/) course, is a short follow-on course to RVfpga that shows how to build a RISC-V SoC from scratch using building blocks and then run the Zephyr real-time operating system (RTOS) on it. The RVfpga courses can be completed in simulation only or, optionally, also in hardware on an FPGA. All software and simulation tools are freely available. Provided simulation tools include a waveform viewer, a virtual FPGA board, and a pipeline viewer. The courses also show how to optionally target the RISC-V SoC to a range of FPGA boards, from lower-cost boards, such as the Basys 3 or Boolean board, to more expensive FPGA boards, such as the Nexys A7 FPGA board.

To understand RVfpga and start using it, you can follow the next steps:

1. View this video: [IntroductionRVfpgaVideo](https://www.youtube.com/watch?v=sc_Jn0XSkNw) (the video is in Spanish, but you can watch an AI-translated-to-English version of the video here [IntroductionRVfpgaEnglishVideo](https://www.youtube.com/watch?v=cO3UAbT09es), you can watch an AI-translated-to-Chinese version of the video here [IntroductionRVfpgaChineseVideo](https://www.youtube.com/watch?v=F-1Q-59s84s) or you can enable the subtitles in the video in Spanish). The video introduces the RVfpga materials. You can download the slides [here](https://drive.google.com/file/d/1o8df8PdNoDIV17_L0JPiURypwtAzfpfl/view?usp=sharing).

2. Install the Virtual Machine as explained [below](https://github.com/artecs-group/RVfpga-sim-addons/blob/main/Computer_Organization/Lab0/README.md#virtual-machine).

3. Download the RVfpga sources as explained [below](https://github.com/artecs-group/RVfpga-sim-addons/blob/main/Computer_Organization/Lab0/README.md#simulators-and-example-projects).

4. Finally, view the following video from time 3:12 to the end to see the different RVfpga Tools working inside the Virtual Machine: [RVfpgaToolsVideo](https://youtu.be/Z8QcQRW7F4s?si=8g_GSFpHmIsMQrzI&t=192) (the video is in Spanish, but you can watch an AI-translated-to-English version of the video here [RVfpgaToolsEnglishVideo](https://youtu.be/HuAF2XOMQmQ?si=-LpY-J7f-ng9AYAa&t=192), you can watch an AI-translated-to-Chinese version of the video here [RVfpgaToolsChineseVideo](https://youtu.be/A_c8GACrW9w?si=gst8rw2755R_JtMA&t=192), or you can enable the subtitles in the original video).



## Virtual Machine
*You can visualize the following video from time 0:0 to time 1:45 to see the steps described in this section: [RVfpgaToolsVideo](https://www.youtube.com/watch?v=Z8QcQRW7F4s) (the video is in Spanish, but you can watch an AI-translated-to-English version of the video here [RVfpgaToolsEnglishVideo](https://www.youtube.com/watch?v=HuAF2XOMQmQ), you can watch an AI-translated-to-Chinese version of the video here [RVfpgaToolsChineseVideo](https://www.youtube.com/watch?v=A_c8GACrW9w), or you can enable the subtitles in the original video).*

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
*You can visualize the following video from time 1:45 to time 3:10 to see the steps described in this section: [RVfpgaToolsVideo](https://youtu.be/Z8QcQRW7F4s?si=-LpPqGG2L8ovLKRd&t=104) (the video is in Spanish, but you can watch an AI-translated-to-English version of the video here [RVfpgaToolsEnglishVideo](https://youtu.be/HuAF2XOMQmQ?si=dS2YwrbHStoOt-ds&t=104), you can watch an AI-translated-to-Chinese version of the video here [RVfpgaToolsChineseVideo](https://youtu.be/A_c8GACrW9w?si=PZii40gCMd3WY6-B&t=104), or you can enable the subtitles in the original video).*

Once the Virtual Machine (VM) is installed in your system, all labs will be developed in it. So, from inside the VM, download the following file and unzip it in the VM home directory: [SimulatorsAndProjects](https://drive.google.com/file/d/1hbCSFmjIoGmXq4r5G12_AMUKezHXA6A-/view?usp=sharing).

To do this you can open a file explorer, move the downloaded file to the OS home, and click on the file with the right mouse button and then “Extract Here”.

<p align="center">
  <img src="Images/ExtractHere.png" width=70% height=70%>
</p>

In the following screenshot you can see how RVfpga should be located in the VM. It is important that you respect this location in order to avoid problems with the paths indicated in the labs.

<p align="center">
  <img src="Images/Path.png" width=70% height=70%>
</p>

At this point your system is ready to run, inside the Virtual Machine, all the exercises from the RVfpga package as well as the Ripes simulator.
