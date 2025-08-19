# Lab 1 - The RISC-V ISA
In this lab we review the RISC-V architecture and complete several exercises. We will use the [Ripes](https://github.com/mortbopet/Ripes), a visual computer architecture simulator and assembly code editor created for the RISC-V instruction set architecture. It has the following features:

- RISC-V 32-bit architecture.
- Base repertoire and M and C extensions (in this practice we will use only the M extension).
- Source code viewer, disassembled or binary code, 32 registers and memory regions.
- Possibility of executing the code in the different supported processors. In this practice we will use the Single-Cycle processor.

Follow the next steps:
1. Read the instructions provided at [Ripes_Introduction](https://github.com/mortbopet/Ripes/blob/master/docs/introduction.md).
2. Replicate the instructions provided in section *Using RIPES in the virtual machine*.
3. Then, resolve the exercises 1-4 provided below.


## Using RIPES in the virtual machine
Follow the steps below to use and finish configuring the Ripes simulator in the VM.

1. Start the simulator inside the VM:
    - Open a terminal in the VM.
    - Enter the “Ripes” directory: ```cd ~/Simuladores_EC_24-25/Ripes```
    - Before you can launch the simulator for the first time, you must install FUSE by means of the following command (it will ask for the root password, which is rvfpga): ```sudo apt-get install fuse libfuse2```
    - Run the simulator: ```./Ripes-v2.2.6-linux-x86_64.AppImage```

2. Environment:
    - On the left side you can see the different windows that can be displayed: Editor, Processor, Cache, Memory, I/O.
    - Depending on the selected window, the view will change. In the following figure we see the Editor window, in which you can enter code in Assembler or C in the left window, the compiled/assembled code will be displayed in the middle window, and it shows the registers of the simulated processor on the right.

<p align="center">
  <img src="Images/EditorFigure.png" width=80% height=80%>
</p>

3. Before simulating the program, select the Single Cycle processor, enable the M extension and disable the C extension:

<p align="center">
  <img src="Images/SingleCycle.png" width=80% height=80%>
</p>

4. The following RISC-V assembly program subtracts 1 to each element of vector ```v```.

```
  .global main
  
  .equ n ,10
  
  .data
  v: .word 12 ,1 , -2 ,15 , -8 ,4 , -31 ,8 ,8 ,25
  
  .text
  main:
    li s1 , n
    mv s2 , zero # s2 es i
    for:
      beq s2,s1,fin
      la t1 , v 		# t1= @base de v
      slli t3 ,s2 ,2 	# i*4
      add t2 ,t1 ,t3 	# t2= @efectiva de v[i]
      lw s3 ,0( t2)
      addi s3 ,s3 ,-1
      sw s3 ,0( t2)
      addi s2 ,s2 ,1 	# i=i+1
      j for
    fin:
    j fin
```

To simulate the program, type or copy it into the window on the left. For example, in the following figure you can see the previous program (which we also use in Exercise 1 below). On the right you can see the disassembled version.

<p align="center">
  <img src="Images/Ex1.png" width=80% height=80%>
</p>

5. The top menu allows us to control the simulation. By hovering the mouse over each button we are informed about its functionality.

<p align="center">
  <img src="Images/Menu.png" width=40% height=40%>
</p>

6. We can execute the code step by step:
    - The “minor” and “major” arrows in the top menu allow us to go forward or backward instruction by instruction.
    - The current instruction is shown highlighted in red.

<p align="center">
  <img src="Images/Execution.png" width=40% height=40%>
</p>

7. Disassembled/binary code window and registers window:
    - The registers will be updated as we progress through the program.
    - When a register is updated, it will be highlighted in yellow.
    - The middle window shows the disassembled code. Note that, unlike the source, it only includes instructions (not pseudo-instructions).

<p align="center">
  <img src="Images/Registers.png" width=90% height=90%>
</p>

8. The Memory window allows us to visualize the different memory sections. The figure shows the .text section, which includes the text of the code. At the bottom you must select, from the “Go to section” menu, the .text section. You can check that the hexadecimal code corresponds to the program instructions in the Editor.

<p align="center">
  <img src="Images/Memory.png" width=90% height=90%>
</p>

9. At the bottom, in the “Go to section” menu, we can switch to the .data section. You can check that the data correspond to the vector components in the Editor.

<p align="center">
  <img src="Images/DataSection.png" width=90% height=90%>
</p>

10. Set up the simulator to compile and run C programs. Follow these steps (the full instructions are available at this [link](https://github.com/mortbopet/Ripes/blob/master/docs/c_programming.md)):

  - Download the RISC-V toolchain:
      - The Ripes simulator webpage recommends to download the pre-built toolchain [here](https://github.com/sifive/freedom-tools/releases/tag/v2020.04.0-Toolchain.Only).
      - Once downloaded, copy that file to ```/home/rvfpga/Simuladores_EC_24-25/Ripes/```
      - Unzip the file ```riscv64-unknown-elf-gcc-8.3.0-2020.04.1-x86_64-linux-ubuntu14.tar.gz``` by right-clicking on the file and selecting "Extract Here."

<p align="center">
  <img src="Images/ExtractHere.png" width=90% height=90%>
</p>


  - Set the compiler path in Ripes:
      - In the top menu of Ripes, open "Edit-Settings":

      <p align="center">
        <img src="Images/EditSettings.png" width=40% height=40%>
      </p>


      - In the window that opens, go to the "Compiler" tab.

      <p align="center">
        <img src="Images/PathCompiler.png" width=90% height=90%>
      </p>


      - In the "Browse" section, select the C compiler (the file named ```riscv64-unknown-elf-gcc```), which is located in the following path (you can copy and paste the path in the "Compiler path"):

      ```
      /home/rvfpga/Simuladores_EC_24-25/Ripes/riscv64-unknown-elf-gcc-8.3.0-2020.04.1-x86_64-linux-ubuntu14/bin/riscv64-unknown-elf-gcc
      ```

      <p align="center">
        <img src="Images/PathCompiler2.png" width=90% height=90%>
      </p>

      <p align="center">
        <img src="Images/PathCompiler3.png" width=90% height=90%>
      </p>


  - Set the appropriate arguments:
      - Compiler arguments: ```-O1```
      - Linker arguments: ```-static-libgcc -lm```

      <p align="center">
        <img src="Images/Linker.png" width=90% height=90%>
      </p>


11. To simulate a C program, write or copy it into the left window, marking "Input Type" as C language. For example, try the next C program (which we use later in an exercise):

```
int main(void)
{
   int i,result,num=7;

   if (num > 1){
      result = num;
      for (i=num-1;i>1;i--)
      result = result*i;
   }
   else
      result=1;

   printf("Factorial = %d",result);

   while(1);
}
```

12. Next, compile the program by clicking on the hammer icon. If the program is correct, the disassembled version will appear in the central window:

<p align="center">
  <img src="Images/Martillo.png" width=90% height=90%>
</p>

13. Run the program by clicking the "Fast Execution" button. The result of the factorial calculation will appear in the console:

<p align="center">
  <img src="Images/Execution.png" width=70% height=70%>
</p>

14. Recompile the program with different optimization levels (see step 10 above) and compare the assembled programs generated by each of them.

15. Recompile the program with a -O0 optimization level and the following two different scenarios: M extension enabled and M extension disabled (see step 3 above). Compare the assembly code generated for the ```main``` function in each scenario.


## Exercise 1
Given the following RISC-V assembly code:

```
  .global main
  
  .equ n ,10
  
  .data
  v: .word 12 ,1 , -2 ,15 , -8 ,4 , -31 ,8 ,8 ,25
  
  .text
  main:
    li s1 , n
    mv s2 , zero # s2 es i
    for:
      beq s2,s1,fin
      la t1 , v 		# t1= @base de v
      slli t3 ,s2 ,2 	# i*4
      add t2 ,t1 ,t3 	# t2= @efectiva de v[i]
      lw s3 ,0( t2)
      addi s3 ,s3 ,-1
      sw s3 ,0( t2)
      addi s2 ,s2 ,1 	# i=i+1
      j for
    fin:
    j fin
```

This code should work both on the board (RVfpga-Nexys) and on the Whisper/Ripes simulators. At ```/home/rvfpga/Simuladores_EC_24-25/RVfpga/Projects/Lab1_Ex1``` we provide a project that can be directly used on RVfpga-Whisper. To execute on Ripes, just copy the code in the editor. To execute on RVfpga-Nexys, make sure you comment line ```debug_tool = whisper``` in file ```platformio.ini```.

Run the code and answer the following questions. Add screenshots of the execution to complement your answers.

- Briefly explain what the code does.
- Provide examples of the different addressing modes we explained in theory based on the instructions in the program (use examples of instructions, not pseudo-instructions).
- What instruction does the pseudo-instruction ```li s1, n``` translate to?
- What instruction does the pseudo-instruction ```mv s2, zero``` translate to?
- To which machine instruction in hexadecimal does the pseudo-instruction ```mv s2, zero``` translate? Considering the format of RISC-V instructions, explain which fields the machine instruction contains.
- Take a screenshot of the memory viewer clearly identifying, one by one, the instructions that make up the for loop. Are they properly aligned?
- Take a screenshot of the memory viewer at the end of each iteration, showing how the vector evolves.
- In this code, a simple modification can be made to improve its performance. Write modified code, explain why it improves efficiency, and show a screenshot in which the final vector is visible in memory.
- Modify the code so that it subtracts 1 from the components whose stored value is odd and adds 1 to the components whose stored value is even.


## Exercise 2
The Bubble Sort algorithm sorts the elements of a vector from smallest to largest using a very straightforward procedure: it repeatedly traverses the vector, swapping successive positions if V(i) > V(i+1), until no swaps are made.

The following pseudocode is provided as a guide (Note: use a constant, N, to define the length of the vector):

```
do 
  swapped=false 
  for i from 0 to N-2 do: 
    if V[i] > V[i+1] then 
      swap(V[i], V[i+1]) 
      swapped = true 
    end if 
  end for 
while swapped 
```

**PROGRAMMING IN RISC-V ASSEMBLY:**

- Implement the algorithm in RISC-V assembly. Include a ```main``` function that performs most functionality and that calls a function called ```swap```, that exchanges ```V[i]``` and ```V[i+1]```. Test the program in Ripes.
- Explain the prologue you have created for the ```swap``` function. Is it a leaf or non-leaf subroutine? What is the difference, and how does it affect the prologue?
- Copy the instructions that prepare the input parameters for the swap subroutine. Do you pass the parameters by value or by reference? Why?
- Take several screenshots during the execution of the program at relevant points, showing the instructions, registers, and memory. For example, you can show the evolution of memory as the data gets sorted.

**PROGRAMMING IN C:**

The following code is a possible C implementation of the above pseudocode (the first one for Ripes and the second one for RVfpga-Whisper). At ```/home/rvfpga/Simuladores_EC_24-25/RVfpga/Projects/Lab1_Ex2``` we provide a project that can be directly used on the RVfpga-Whisper simulator. To execute the program on RVfpga-Nexys, make sure you comment line ```debug_tool = whisper``` in file ```platformio.ini```.

- Compile the code with two different optimization levels: -O0 and -O1.
  - For each optimization level, test the execution of the program step-by-step, both in C and in RISC-V assembly.
  - Compare the obtained ```swap``` and ```main``` functions for each optimization level.
  - NOTE: this item can only be tested in Whisper or Ripes, not on the board.

**RIPES:**
```
#define N 4

int V[N]={5,2,3,1};

void main(void)
{
   int swapped=1, i;

   while(swapped){
       swapped=0;
       for (i=0; i<(N-1); i++){
           if (V[i] > V[i+1]){
               swap(&V[i], &V[i+1]);
               swapped=1;
           }
       }
   }

   while(1);

}

void swap(int *V, int *W){
   int temp;
   temp=*V;
   *V=*W;
   *W=temp;
}
```

**WHISPER:**
```
#if defined(D_NEXYS_A7)
   #include <bsp_printf.h>
   #include <bsp_mem_map.h>
   #include <bsp_version.h>
#else
   PRE_COMPILED_MSG("no platform was defined")
#endif

#include <psp_api.h>

#define N 4

int V[N]={5,2,3,1};

void main(void)
{
   int swapped=1, i;

   while(swapped){
       swapped=0;
       for (i=0; i<(N-1); i++){
           if (V[i] > V[i+1]){
               swap(&V[i], &V[i+1]);
               swapped=1;
           }
       }
   }

   while(1);

}

void swap(int *V, int *W){
   int temp;
   temp=*V;
   *V=*W;
   *W=temp;
}
```


## Exercise 3
Given the following RISC-V assembly code:

```
.global main

.equ n ,5

.data
res: .word 0

.text
main:
  li a1 , n
  la s3 , res
  call factorial
  sw a0 ,0( s3 )
  fin:
  j fin

factorial:
  # prologo
  addi sp , sp , -8
  sw s1 ,0( sp )
  sw s2 ,4( sp )
  # cuerpo
  li s1 ,1
  mv s2 , a1
  li s3 ,1
  for:
    ble s2 , s3 , fin_for
    mul s1 , s1 , s3
    addi s2 , s2 , -1
    j for
  fin_for:
  mv a0 , s1
  # epilogo
  lw s1 ,0( sp )
  lw s2 ,4( sp )
  addi sp , sp ,8
  jr ra

```

At ```/home/rvfpga/Simuladores_EC_24-25/RVfpga/Projects/Lab1_Ex3``` we provide a project that can be directly used on RVfpga-Whisper. To execute on Ripes, just copy the code in the editor. To execute on RVfpga-Nexys, make sure you comment line ```debug_tool = whisper``` in file ```platformio.ini```.

Run the code and answer the following questions. Add screenshots to complement your answers.

- The code contains three errors. Identify and correct them. Copy the modified code, explain the corrections, and include a screenshot illustrating its functionality.
- Find examples of each of the formats used in RISCV (R, I, S, B, U, J) and explain these formats in detail based on the examples shown.
- What values does the stack contain, and what is the value of sp during the execution of the subroutine? Justify your answer.
- Suppose the processor did not include the M extension (you can research this extension online). Perform the multiplication in the factorial function by calling a new subroutine that calculates the multiplication through successive additions (within a loop, add the multiplicand as many times as indicated by the multiplier). Show and explain the modifications you made and illustrate their execution. Emphasize the management involved in introducing a new nested subroutine, particularly in terms of saving registers and the evolution of the stack.


## Exercise 4
Given the following C code that computes the factorial of an integer number (the first one for Ripes and the second one for RVfpga-Whisper). At ```/home/rvfpga/Simuladores_EC_24-25/RVfpga/Projects/Lab1_Ex4``` we provide a project that can be directly used on the RVfpga-Whisper simulator. To execute on RVfpga-Nexys, make sure you comment line ```debug_tool = whisper``` in file ```platformio.ini```.

**RIPES:**
```
int main(void)
{
   int i,result,num=7;

   if (num > 1){
      result = num;
      for (i=num-1;i>1;i--)
      result = result*i;
   }
   else
      result=1;

   printf("Factorial = %d",result);

   while(1);
}
```

**WHISPER:**
```
#if defined(D_NEXYS_A7)
   #include <bsp_printf.h>
   #include <bsp_mem_map.h>
   #include <bsp_version.h>
#else
   PRE_COMPILED_MSG("no platform was defined")
#endif

#include <psp_api.h>

int main(void)
{
   int i,result,num=7;

   /* Initialize Uart */
   uartInit();

    if (num > 1){
      result = num;
      for (i=num-1;i>1;i--)
      result = result*i;
   }
   else
      result=1;

   printfNexys("Factorial = %d",result);

   while(1);
}
```

Run the code and answer the following questions. Add screenshots to complement your answers.

- Default compilation (-O0 optimization level):
    - Explain in detail the ```main``` function generated in RISC-V assembly.
    - Is the ```ra``` register preserved at any point? Why?
    - Of the other registers, which ones are preserved? Why?

- Compile with -O1 (this item can only be tested in Whisper or Ripes, not on the board):
    - The function is very simple. Explain what it does and why it is so simple.

Replace the previous code for the following one, in which the input integer number is generated randomly. Analyze the assembly functions generated with different optimization levels (-O0, -O1, -O2, -O3, -Os), and explain the differences between them and with respect to the previous code. Analyze the simulation of each scenario in Ripes.

```
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void)
{
   int i,result,num;

   srand(time(NULL));
   num = (rand() % 10) + 1;

   if (num > 1){
      result = num;
      for (i=num-1;i>1;i--)
      result = result*i;
   }
   else
      result=1;

   printf("Factorial = %d",result);

   while(1);
}
```

