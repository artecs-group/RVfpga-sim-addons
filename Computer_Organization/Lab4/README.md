# Lab 7 (Lab 4 of CO) - The RVfpga I/O System - High Level
This lab aims to help students gain a solid understanding of an **Input/Output (I/O) System** and how it operates within the RVfpga platform. Follow the steps below:

1. **Background reading**  
   If you are new to *Computer Organization*, start by reading **Chapter 9** of the *Hennessy & Harris* textbook.

2. **Watch the introductory video**  
   Watch the video [InputOutputVideo](https://www.youtube.com/watch?v=8fK-CoEbo0Y), which provides a detailed explanation of the **RVfpga I/O System**. You can also download the slides [here](https://drive.google.com/file/d/1Fv4-I8DwISdqqDpol4i_BMZNzK4QmpOe/view?usp=sharing).

3. **Run the guided simulation example**  
   Perform the guided example for RVfpga-ViDBo, provided in the section *Simulation of the RVfpga SoC in RVfpga-ViDBo*. *(You do **not** need to include this example in your report.)*

4. **Solve the polling-based exercises**  
   Then, complete the following exercises:  
   - [Exercise 1]()  
   - [Exercise 2]()  
   - [Exercise 3]()

5. **Run the interrupt-based guided test**  
   Perform the guided test provided in the section *Interrupts – Guided Test* to learn how interrupts are managed in RVfpga. *(You do **not** need to include this example in your report.)*

6. **Solve the interrupt-based exercises**  
   Finally, complete the following exercises:  
   - [Exercise 4]()  
   - [Exercise 5]()  
   - [Exercise 6]()


## Simulation of the RVfpga SoC in RVfpga-ViDBo
From **minute 16:36 to 19:16** of the following video, you can watch an example of the **RVfpga-ViDBo simulator** running a program: [RVfpgaToolsVideo](https://youtu.be/Z8QcQRW7F4s?si=99ybjtqrBAa5-r8K&t=996).

This tool simulates the **VeeRwolfX SoC**, which is based on the **VeeR EH1** core running on the **Nexys A7 FPGA** board. It allows you to execute RISC-V programs and interact with several board peripherals directly from your computer. Programs executed in the simulator behave **exactly the same** as on the actual FPGA board.

<p align="center">
  <img src="Images/Nexys.png" width=60% height=60%>
</p>

In this lab, we will use only the following peripherals:
- **16 LEDs**
- **16 Switches**
- **8 digits with 7-segment displays**

Follow the steps below to launch an example simulation on RVfpga-ViDBo, where the state of the switches is continuously read and displayed on the LEDs.

1. **Open Visual Studio Code (VS Code).**

2. **Open the project folder**  
   Go to `File → Open Folder` and open the folder containing the example project for this introduction:  
   ```/home/rvfpga/Simuladores_EC_24-25/RVfpga/Projects/LedsSwitches_C-Lang```

<p align="center">
  <img src="Images/OpenFolder.png" width=80% height=80%>
</p>

3. **Check the simulator path**  
   Open the `platformio.ini` file. In this lab, we will use the **RVfpga-ViDBo** simulator, so set the path as follows: 
```board_debug.verilator.binary = /home/rvfpga/Simuladores_EC_24-25/RVfpga/verilatorSIM_ViDBo/OriginalBinaries/RVfpga-ViDBo_Ubuntu22```

4. **Run the simulator**

a. In the **PROJECT TASKS** panel of PlatformIO, click on ```RVfpgaEL2-ViDBo / Pipeline```

<p align="center">
   <img src="Images/RVfpgaVidbo.png" width=30% height=30%>
</p>

b. **Launch the ViDBo server**  
   Open a terminal and run the following commands:
   ```
   cd /home/rvfpga/Simuladores_EC_24-25/RVfpga/verilatorSIM_ViDBo
   python3 -m http.server --directory NexysA7board/
   ```

  <p align="center">
     <img src="Images/Python.png" width=100% height=100%>
  </p>

c. **Open the web interface**  
   In your browser, go to **http://localhost:8000/nexys-a7.html**, and click the **“Connect to board”** button.

  <p align="center">
     <img src="Images/ViDBo1.png" width=80% height=80%>
  </p>

5. **Test the simulation**  
Move the switches and observe how the LEDs change accordingly. This behavior is identical to how the program would run on the actual FPGA board. For example:

<p align="center">
   <img src="Images/NexysExample.png" width=60% height=60%>
</p>


## Exercise 1

Write a C program that displays the **inverse** of the switches on the LEDs.

For example:  
- If the switches are (in binary): `0101010101010101`, then the LEDs should display: `1010101010101010`  
- If the switches are: `1111000011110000`, then the LEDs should display: `0000111100001111`

You can use the project **`LedsSwitches_C-Lang`** as a base. Make sure you understand how the program reads the switch states, writes to the LEDs, and how the GPIO registers are accessed.


## Exercise 2

Write a C program that displays the **value of the switches** on the **four right-most digits** of the 7-segment displays. You can use the project **`71_7SegDispl_C-Lang.c`** as a base.

When running the program in **RVfpga-ViDBo**, you should see the switch value appear on the 7-segment display. Note that this peripheral is shown **outside** the FPGA board in the simulator.

<p align="center">
  <img src="Images/ViDBo.png" width=70% height=70%>
</p>


## Exercise 3

Write a C program that shows the string **“0-1-2-3-4-5-6-7-8”** moving from right to left across the 8-digit 7-segment display.

- The character `0` should first appear on the **right-most digit**.  
- Then it should move one position to the left, while the next character (`1`) appears on the right-most digit, and so on.  

You can base your code on the same **`71_7SegDispl_C-Lang`** project, modifying it to implement the scrolling behavior.


## Interrupts – Guided Test

In this guided test, you will learn how to manage **interrupt-driven I/O** in RVfpga. Two example projects are provided — both implement the same functionality, but one uses **polling**, while the other uses **interrupts**:

- `/home/rvfpga/Simuladores_EC_24-25/RVfpga/Projects/LED-Switch_7SegDispl_C-Lang`  
- `/home/rvfpga/Simuladores_EC_24-25/RVfpga/Projects/LED-Switch_7SegDispl_Interrupts_C-Lang`

Open both projects, analyze their structure, and run them in **RVfpga-ViDBo**. Focus especially on the following functions in the interrupt-based version: `main`, `GPIO_Initialization`, and `GPIO_ISR`.

#### Programmed I/O version

The first example (**`LED-Switch_7SegDispl_C-Lang`**) demonstrates **polling-based I/O**. It performs two tasks:

1. Inverts the **right-most LED** every time a **0→1 transition** occurs on the **right-most switch**.  
2. Displays an **incrementing counter** on the **8-digit 7-segment display**, increasing roughly once per second.

After initialization, the program enters an **infinite loop** that:
- Reads the current switch state.  
- Compares it with the previous state to detect transitions.  
- Inverts the LED if a 0→1 transition is detected.  
- Updates the displayed count and generates a delay through a software loop.

However, this approach has a **limitation**: if a switch transition happens during the delay loop (for instance, when the switch is toggled quickly), the program might **miss** the event.

> **Observation:** Try toggling the switch quickly in the simulator — you will notice that some transitions are not detected.  
> This limitation motivates the use of **interrupt-driven I/O**.

#### Interrupt-driven I/O version

The second example (**`LED-Switch_7SegDispl_Interrupts_C-Lang`**) solves this problem using **hardware interrupts**.

Here, the switch input is configured to **trigger an interrupt** whenever a **0→1 transition** occurs. When that happens:
- The processor suspends the main program and jumps to the **`GPIO_ISR`** function.  
- Inside the ISR, the switch state is read and the LED state is inverted.  
- Once finished, control returns to the main loop.

In this version:
- The `main` function performs the necessary initializations, then enters a loop that periodically updates the 7-segment display and creates a software delay.  
- The switch is **not** read explicitly in the main loop; all event handling occurs inside the **interrupt service routine (ISR)**.  
- As a result, **no switch transitions are missed**, even if they occur during the delay.

> **Key takeaway:**  
> Using interrupt-driven I/O ensures that the processor can react to external events immediately, without wasting time polling the device.


## Exercise 4

Modify the interrupt-based code  
`/home/rvfpga/Simuladores_EC_24-25/RVfpga/Projects/LED-Switch_7SegDispl_Interrupts_C-Lang`  
so that each time a 0→1 transition is detected on the first switch, the state of all 16 LEDs is inverted — not just the least significant one as in the original program.

Hint: In the interrupt service routine (ISR), replace the line that toggles only one LED with a bitwise inversion of the entire 16-bit LED output register. Remember that in C:
- ! is logical NOT (returns 0 or 1)
- is bitwise NOT (inverts all bits).


## Exercise 5

Modify the functions `main`, `GPIO_Initialization`, and `GPIO_ISR` in the interrupt-based project `/home/rvfpga/Simuladores_EC_24-25/RVfpga/Projects/LED-Switch_7SegDispl_Interrupts_C-Lang` so that the program uses **two switches** (the two least significant ones) instead of just one.

The new functionality must be:

- **SW0**: retains the same behavior as in the original code — toggles the LED state on each 0→1 transition.  
- **SW1**: toggles the **7-segment display on/off** state.  
  - If the display is off, turning it on resumes counting where it left off.  
  - If the display is on, turning it off stops updating it.

Hint: Use the register `RGPIO_INTS` to identify which switch triggered the interrupt. Inside the ISR, check both switch bits and handle each event accordingly.


## Exercise 6

Modify the `main`, `GPIO_Initialization`, and `GPIO_ISR` functions in the interrupt-based project `/home/rvfpga/Simuladores_EC_24-25/RVfpga/Projects/LED-Switch_7SegDispl_Interrupts_C-Lang` to implement the following behavior:

- Use the two least significant switches (SW0 and SW1).
- SW0 toggles between two counting speeds (fast / slow).
- SW1 toggles the counting direction (increment / decrement).
- The LEDs must remain off at all times (do not update the LED output).

Guidance:
- Enable interrupts for both SW0 and SW1 and use `RGPIO_INTS` to determine which switch triggered the interrupt.
- Maintain global state variables for:
  - current speed (fast/slow),
  - current direction (up/down),
  - the 32-bit counter value,
  - display on/off state if your template requires it.
- In the main loop, update the 7-segment display using:
  - a delay that depends on the selected speed,
  - a counter update that depends on the selected direction.
- In the ISR, only update the speed/direction state and clear the served interrupt source(s).
- Do not write to the LED register anywhere in the program.
