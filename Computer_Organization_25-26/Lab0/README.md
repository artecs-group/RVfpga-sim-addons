# Lab 0 - Introduction and Installation
This lab aims to prepare our computer to work in the labs of the course and to introduce the tools that we will use in the labs. Follow the next steps:

1. Install the Virtual Machine as explained below at section *Virtual Machine*.

2. Download the sources as explained below at section *RVfpga Sources*.


## Virtual Machine
You can visualize the following video from time 0:0 to time 1:45 to see the steps described in this section: [RVfpgaToolsVideo](https://www.youtube.com/watch?v=Z8QcQRW7F4s).

In these labs we are going to work with a Virtual Machine (VM) with Ubuntu 22.04 Linux Operating System (OS). This VM can run on most native OS (Windows, Linux, macOS with Intel processors); however, if you are using an Apple Silicon MacBook (M1, M2, M3, …), you will not be able to run this VM. 

>If you prefer to work natively on Ubuntu without a virtual machine, follow the installation procedure described in the next document: [Installing the RVfpga Tools in a Clean Ubuntu Environment](https://drive.google.com/file/d/1WKjvM18EdGsICj_fqLM_Gq4MjyDzGp1T/view). After following the instructions in the document, continue directly with section *RVfpga Sources*.

The VM belongs to the RVfpga training package, on which these practices are based. Download the VM from one of the following links. Both refer to the same VM, so use the one that works best for you: 
+ [Virtual Machine 1st link](https://drive.google.com/file/d/1KFnJYq6krB7vYt_AqTB_zTYVmxfATwJF/view)
+ [Virtual Machine 2nd link](https://pvr-sdk-live.s3.amazonaws.com/iup/ubuntu-22-RVfpga.ova)

The file is very large. You must download it with a good Internet connection and you must make sure that the file is downloaded completely, otherwise the VM will not install correctly. 
For example, the following figure shows the downloaded VM on a laptop with Windows 11 OS (note that it occupies more than 12 GB).

<img width="1421" height="510" alt="image" src="https://github.com/user-attachments/assets/3e2e5eea-0eb5-4c78-b577-e00844b8cc20" />


The VM can be installed in the usual virtualization software, such as VirtualBox or VMWare. Install one of those programs and import the VM (the screenshots in this tutorial are for VirtualBox).

Finally, run the VM, check that the boot is successful, and log into Linux using the user and password **rvfpga**. If the boot gives problems, try changing the USB version of the VM from 2.0 to 1.1, the memory amount used by the VM, or reinstalling the Guest Additions.

Ignore all Ubuntu upgrade proposal windows, Guest Additions, PlatformIO, etc. that open automatically on the VM.



## RVfpga Sources
You can visualize the following video from time 1:45 to time 3:10 to see the steps described in this section: [RVfpgaToolsVideo](https://youtu.be/Z8QcQRW7F4s?si=-LpPqGG2L8ovLKRd&t=104).

Once the Virtual Machine (VM) is installed in your system, all labs will be developed in it. So, from inside the VM, download the following file and unzip it in the VM home directory: [SimulatorsAndProjects_25-26](https://drive.google.com/file/d/1CctkpRvmTS4PsdsKVPTHpT6g6qnUm3WH/view?usp=sharing).

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

Once you have downloaded the file, you can open a file explorer, move the downloaded file to the OS home, and click on the file with the right mouse button and then “Extract Here”.

<img 
  src="https://github.com/user-attachments/assets/8af3f3d2-7d9f-404a-9a09-14bb0178b9ac"
  style="width: 70%;"
/>

At this point your system is ready to run, inside the Virtual Machine, all the exercises from the RVfpga package as well as the Ripes simulator.
