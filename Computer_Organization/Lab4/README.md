# Lab 7 (Lab 4 of CO) - The RVfpga I/O System - High Level
This practice aims to help students gain a thorough understanding of an Input/Output System. You can follow the next steps:

1. If you are new to Computer Organization, you should start by reading Chapter 9 of the H&H book.
2. Then, view this video [InputOutputVideo](https://www.youtube.com/watch?v=8fK-CoEbo0Y). The video describes the RVfpga I/O System in detail. You can download the slides [here](https://drive.google.com/file/d/1Fv4-I8DwISdqqDpol4i_BMZNzK4QmpOe/view?usp=sharing).
3. Then, you can perform the guided example for RVfpga-ViDBo, provided next in section *Simulation of the RVfpga SoC in RVfpga-ViDBo*. You do not need to include this example in the report.
4. Then, you can resolve the polling-based exercises included below:
    - [Exercise 1]()
    - [Exercise 2]()
    - [Exercise 3]()
5. Then, you can perform the Interrupt-bsaed guided test, provided next in section *Interrupts - Guided test*. You do not need to include this example in the report.
6. Finally, you can resolve the interrupt-based exercises included below:
    - [Exercise 4]()
    - [Exercise 5]()
    - [Exercise 6]()


## Simulation of the RVfpga SoC in RVfpga-ViDBo
From time 16:36 to time 19:16 of the following video, you can visualize an example of the RVfpga-ViDBo simulator running a program: [RVfpgaToolsVideo](https://youtu.be/Z8QcQRW7F4s?si=99ybjtqrBAa5-r8K&t=996).

This tool simulates the VeeRwolfX SoC based on the VeeR EH1 core running on the Nexys A7 FPGA board. The simulator allows us to simulate the execution of RISC-V codes on this processor and interact with some of the board’s peripherals. The programs work exactly the same in the simulator as on the actual board.

<p align="center">
  <img src="Images/Nexys.png" width=60% height=60%>
</p>

In this lab, we will only use the following peripherals among all the available ones:
- 16 LEDs
- 16 Switches
- 8 digits with 7-segment displays

Follow the steps below to launch an example simulation on RVfpga-ViDBo, where the state of the switches is continuously read and displayed on the LEDs.
1. Open Visual Studio Code (VSCode).
2. Click on ```File - Open Folder``` and open the folder containing the project for the example we will work on in this introduction: ```/home/rvfpga/Simuladores_EC_24-25/RVfpga/Projects/LedsSwitches_C-Lang```

<p align="center">
  <img src="Images/OpenFolder.png" width=80% height=80%>
</p>

3. Set the path for the simulator in the ```platformio.ini``` file. In this lab, we will use the RVfpga-ViDBo simulator. In this project, the path is already correctly set in the following line, so you do not need to change anything:

```board_debug.verilator.binary = /home/rvfpga/Simuladores_EC_24-25/RVfpga/verilatorSIM_ViDBo/OriginalBinaries/RVfpga-ViDBo_Ubuntu22```

4. Run the simulator:

    a. In the ```PROJECT TASKS``` window of PlatformIO, click on ```RVfpgaEL2-ViDBo/Pipeline```

   <p align="center">
      <img src="Images/RVfpgaVidbo.png" width=30% height=30%>
   </p>
   
    b. Open a terminal and launch the ViDBo server by running the following commands:

      ```
      cd /home/rvfpga/Simuladores_EC_24-25/RVfpga/verilatorSIM_ViDBo
      python3 -m http.server --directory NexysA7board/
      ```

     <p align="center">
        <img src="Images/Python.png" width=100% height=100%>
     </p>

    c. Finally, open a browser and go to http://localhost:8000/nexys-a7.html, and click on the "Connect to board" button.

     <p align="center">
        <img src="Images/ViDBo1.png" width=80% height=80%>
     </p>


5. Finally, check the simulation by modifying the switches and viewing the LEDs. This code would behave exactly the same if run on the actual board. For example:

     <p align="center">
        <img src="Images/NexysExample.png" width=60% height=60%>
     </p>


## Exercise 1
Write a C program that displays the inverse of the switches on the LEDs. For example: 
- If the switches are (in binary): 0101010101010101, then the LEDs should display: 1010101010101010
- If the switches are: 1111000011110000, then the LEDs should display: 0000111100001111 

You can use the ```LedsSwitches_C-Lang``` project as a base. Make sure you understand 


## Exercise 2
Write a C program that displays the value of the switches on the four right-most digits of the 7-segment displays.

You can use the ```71_7SegDispl_C-Lang.c``` project as a base.

We next show the result that you should obtain when running this program on RVfpga-ViDBo. You can see how the switches value is shown in the 7-segment displays. Note that this device is shown in the simulator outside the board.

<p align="center">
  <img src="Images/ViDBo.png" width=70% height=70%>
</p>


## Exercise 3
Write a C program that shows the string “0-1-2-3-4-5-6-7-8” moving from the right to the left of the 8-digit 7-segment displays. That is, 0 should show up on the right-most digit first. Then it should move to the left and 1 should show up on the right-most digit, and so on.


## Interrupts - Guided test
In this test, we will work with interrupts. Two codes are provided with the same functionality, but the first uses polling while the second uses interrupts.

- ```/home/rvfpga/Simuladores_EC_24-25/RVfpga/Projects/LED-Switch_7SegDispl_C-Lang```
- ```/home/rvfpga/Simuladores_EC_24-25/RVfpga/Projects/LED-Switch_7SegDispl_Interrupts_C-Lang```

Analyze both provided codes and simulate them. In the interrupt-based code, you must focus on the ```main```, ```GPIO_Initialization```, and ```GPIO_ISR``` functions. We next provide some guidance about these two examples:

In the first example (LED-Switch_7SegDispl_C-Lang), we show how to use Programmed I/O to perform the following two tasks:
Invert the rightmost LED every time a 0 to 1 transition on the rightmost switch occurs.
Show an ascending count in the 8-digit 7-segment displays, that increments around once per second.

Open the program in the editor. You can see that, after some initializations, the program enters an infinite loop that compares the current switch state with the previous one and, in case a 0 to 1 transition is detected, it inverts the LED state. Then, the value shown on the 8-digit 7-segment displays is incremented and a software delay is generated.

Note that this program does not work correctly in some situations. For example, a 0 to 1 to 0 switch transition that occurs within the delay loop will never be detected (you can test it by changing the switch quickly). How could we improve the program? The answer is interrupt-driven I/O.

In the second example (LED-Switch_7SegDispl_Interrupts_C-Lang), we show a new version of the program where interrupt-driven I/O is used to read the state of the rightmost switch. This strategy fixes the problem of the program missing switch transitions that occur during the delay loop.

In this program, the main function performs some initializations and then enters an infinite loop where the 7-segment displays are written and a software delay is established. Note that the switch is not explicitly read in this case. Instead, whenever a 0 to 1 transition occurs in the switch, an interrupt is triggered that makes the processor execute the GPIO_ISR function, where the switch state is read and the LED state is inverted.


## Exercise 4

Modify the interrupt-based code (```/home/rvfpga/Simuladores_EC_24-25/RVfpga/Projects/LED-Switch_7SegDispl_Interrupts_C-Lang```) so that each time a 0 to 1 transition is detected on the first switch, the state of all 16 LEDs is inverted, not just the least significant one as in the provided code.

Note: In C, the following two operators work as explained:
  - ! → Performs boolean inversion; i.e., !0 is 1 and !1 is 0.
  - ~ → Performs logical inversion; i.e., ~0 is 0xffffffff.


## Exercise 5

Modify the ```main```, ```GPIO_Initialization``` and ```GPIO_ISR``` functions of the interrupt-based code (```/home/rvfpga/Simuladores_EC_24-25/RVfpga/Projects/LED-Switch_7SegDispl_Interrupts_C-Lang```) so that it implements the following functionality:

- Both of the two least significant switches must be used, not just one. The register ```RGPIO_INTS``` indicates which pin generated the interrupt.  
- The **first switch** retains the same functionality as in the original code.  
- The **second switch** toggles the 7-segment displays on/off state (i.e., if they are off, they turn on and continue displaying the count, and if they are on, they turn off).


## Exercise 6

Modify the ```main```, ```GPIO_Initialization``` and ```GPIO_ISR``` functions of the interrupt-based code (```/home/rvfpga/Simuladores_EC_24-25/RVfpga/Projects/LED-Switch_7SegDispl_Interrupts_C-Lang```) so that it implements the following functionality:

- Both of the two least significant switches must be used, not just one. The register ```RGPIO_INTS``` indicates which pin generated the interrupt.  
- The **first switch** toggles between two counting speeds.  
- The **second switch** toggles the counting direction:  
  * Increment the counter.  
  * Decrement the counter.  

Unlike the original code, it is not necessary for the LEDs to invert their value on each 0-to-1 transition; instead, they must remain turned off.

