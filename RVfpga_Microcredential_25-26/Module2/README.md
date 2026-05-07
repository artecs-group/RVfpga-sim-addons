# Module 2 - Input/Output in the RVfpga SoC

## General Contents
In this second module, students will work with the input/output (I/O) system of the RVfpga SoC and learn how the RISC-V processor interacts with external peripherals implemented in hardware. Throughout the module, students will use and modify existing peripherals such as GPIOs, LEDs, switches, counters, and 7-segment displays, combining software development in C and assembly with hardware design in SystemVerilog.

The module includes both high-level programming exercises using the existing RVfpga platform and lower-level activities focused on understanding and extending the internal hardware implementation of the SoC. Students will also explore interrupt-based I/O, as well as simulation and debugging workflows using RVfpga-Trace and Vivado tools.

## Workflow
Follow the next steps to analyze the RVfpga Input/Output System, first at a high-level and then at a low-level.

### To complete between May 18 and 21:
1. If you need to review Verilog programming or Input/Output general concepts, you can look at Chapter 4 (System Verilog) and Chapter 9 (Input/Output) of the [H&H book](https://www.amazon.es/Digital-Design-Computer-Architecture-RISC-V/dp/0128200642).

2. View this video [InputOutputVideo](https://www.youtube.com/watch?v=8fK-CoEbo0Y) (the video is in Spanish, but you can watch an AI-translated-to-English version of the video here: [InputOutputEnglishVideo](https://www.youtube.com/watch?v=oIRFxQEBNAc)). The video describes the RVfpga I/O System in detail. You can download the slides [here](https://drive.google.com/file/d/1Fv4-I8DwISdqqDpol4i_BMZNzK4QmpOe/view?usp=sharing). In case you need it, you can find more theoretical details about the RVfpga I/O System in Labs 6 to 10 of the full package.

3. Download the following zip file which contains several projects to use in this module: [Alternative Projects](https://drive.google.com/file/d/1tU7KFdhiPp8QpxczqRtw_R8V1guI3D56/view)

4. Complete the following tasks:
    - Open in VS Code the project called `LedsSwitches`. This program, which is explained in the previous video, reads the values of the switches on the board and displays them on the corresponding LEDs. First, analyze the code to understand how the GPIO peripherals are accessed and used. Then, run and test the program either on the FPGA board or using the RVfpga-ViDBo simulator.
    - Open in VS Code the project called `71_7SegDispl_C-Lang`. This program, which is explained in the previous video, shows number *71* on the 7-Segment-Displays. First, analyze the code to understand how the 7-Seg-Displays are used. Then, run and test the program either on the FPGA board or using the RVfpga-ViDBo simulator.

5. Finally, perform the following guided test, which is also explained in the previous video:
In this guided test, you will learn how to manage **interrupt-driven I/O** in RVfpga. Two example projects are provided — both implement the same functionality, but one uses **polling**, while the other uses **interrupts**. As before, analyze the two codes and then run and test the programs either on the FPGA board or using the RVfpga-ViDBo simulator.
**Programmed I/O version**
The first example (**`LED-Switch_7SegDispl_C-Lang`**) demonstrates **polling-based I/O**. It performs two independent tasks:
        1. Inverts the **right-most LED** every time a **0→1 transition** occurs on the **right-most switch**. Note that when a **1→0 transition** occurs on the **right-most switch** nothing changes.
        2. Displays an **incrementing counter** on the **8-digit 7-segment display**, increasing roughly once per second.
After initialization, the program enters an **infinite loop** that:
        - Reads the current switch state.  
        - Compares it with the previous state to detect transitions.  
        - Inverts the LED if a 0→1 transition is detected.  
        - Updates the displayed count and generates a delay through a software loop.
However, this approach has a **limitation**: if a switch transition happens during the delay loop (for instance, when the switch is toggled quickly), the program might **miss** the event. This limitation motivates the use of **interrupt-driven I/O**.
**Interrupt-driven I/O version**
The second example (**`LED-Switch_7SegDispl_Interrupts_C-Lang`**) solves this problem using **hardware interrupts**.
Here, the switch input is configured to **trigger an interrupt** whenever a **0→1 transition** occurs. When that happens:
        - The processor suspends the main program and jumps to the **`GPIO_ISR`** function.  
        - Inside the ISR, the switch state is read and the LED state is inverted.  
        - Once finished, control returns to the main loop.
In this version:
        - The `main` function performs the necessary initializations, then enters a loop that periodically updates the 7-segment display and creates a software delay.  
        - The switch is **not** read explicitly in the main loop; all event handling occurs inside the **interrupt service routine (ISR)**.  
        - As a result, **no switch transitions are missed**, even if they occur during the delay.


---
