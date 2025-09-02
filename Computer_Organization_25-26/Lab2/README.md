# Lab 2 - The Ripes core and the VeeR EH1 core
This practice aims to help students gain a thorough understanding of the commercial VeeR EH1 core, an advanced 2-way superscalar processor with 9 pipeline stages. The processor is explained both theoretically, through a detailed presentation, and practically, using the RVfpga-Pipeline simulator. As a preparatory step, we first focus on the typical academic 5-stage pipelined processor, exploring it theoretically (using the pipelined processor from the Harris and Harris book, H&H) and practically (through the Ripes simulator). 

Follow the next steps:

1. **Ripes core:** You can start using Ripes to simulate and analyze a 5-stage processor that is almost identical to the one described in the H&H textbook.

    * Read again the instructions provided at [Ripes_Introduction](https://github.com/mortbopet/Ripes/blob/master/docs/introduction.md).
    * Replicate the instructions provided below in section [Basic use of the Ripes Pipelined Processor](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization_25-26/Lab2#basic-use-of-the-ripes-pipelined-processor).
    * Analyze the example exercise provided below in section [Exercise 1 - Guided Exercise in Ripes](https://github.com/artecs-group/RVfpga-sim-addons/blob/main/Computer_Organization_25-26/Lab2/README.md#exercise-1---guided-exercise-in-ripes).
    * Analyze the example exercise provided below in section [Exercise 2 - Guided Exercise in Ripes](https://github.com/artecs-group/RVfpga-sim-addons/blob/main/Computer_Organization_25-26/Lab2/README.md#exercise-2---guided-exercise-in-ripes).
    * Finally, complete the exercise provided below in section [Exercise 3 in Ripes](https://github.com/artecs-group/RVfpga-sim-addons/blob/main/Computer_Organization_25-26/Lab2/README.md#exercise-3-in-ripes). This is the first exercise you will include in the report, so make sure to write everything down as you work through it.

2. **VeeR EH1 core:** Once you have a clear understanding of the 5-stage processor used in the textbook and the one used in Ripes, you will start your analysis of a more complex processor, the VeeR EH1 core.

    * Start by watching this video: [VeeReh1Video](https://youtu.be/xVnB6OM00cE?si=0HW333O-oPOXUDZG). The video describes the VeeR EH1 microarchitecture in detail. You can download the slides used in the video [here](https://drive.google.com/file/d/1rSlwCzcHD4F_S4YFLCFn3L0VNXH_sv7L/view?usp=drive_link).
    * Replicate the instructions provided below in section [RVfpga-Pipeline](https://github.com/artecs-group/RVfpga-sim-addons/blob/main/Computer_Organization_25-26/Lab2/README.md#rvfpga-pipeline).
    * Analyze the example exercise provided below in section [Exercise 4 - Guided Exercise in RVfpga-Pipeline](https://github.com/artecs-group/RVfpga-sim-addons/blob/main/Computer_Organization_25-26/Lab2/README.md#exercise-4---guided-exercise-in-rvfpga-pipeline).
    * Finally, complete the exercise provided below in section [Exercise 5 in RVfpga-Pipeline](https://github.com/artecs-group/RVfpga-sim-addons/blob/main/Computer_Organization_25-26/Lab2/README.md#exercise-5-in-rvfpga-pipeline). This is the second exercise you will include in the report, so make sure to write everything down as you work through it.


## Basic use of the *Ripes Pipelined Processor*
Follow the next steps to test a program in the Ripes Pipelined Processor:

1. Start the Ripes simulator.

2. Open the Processor tab and in the ```Select Processor``` icon, choose the processor with the following characteristics:
   - 5-stage processor.
   - RISC-V base instruction set plus M extension.
   - Extended layout.

<p align="center">
  <img src="../../Computer_Organization/Lab2/Images/SelectProc.png" width=60% height=60%>
</p>

3. Add the signal values view in the ```View``` tab.

<p align="center">
  <img src="../../Computer_Organization/Lab2/Images/View.png" width=40% height=40%>
</p>

4. Copy the following program into the Editor tab.

```
.data
   xa: .word 10
   xb: .word 0
   xc: .word 0

.text
   la x9, xa
   la x8, xc
  L1:
   addi x5, x0, 2
   addi x4, x0, 3
   addi x3, x0, -1
   lw x6, 0(x9)
   beq x0, x5, L1
   add x1, x5, x5
   or x2, x4, x4
   sw x6, 8(x9)
```

5. Advance step-by-step until the final cycle. This is the processor state in that cycle. As you can see, five instructions are being executed simultaneously in the processor (in-flight), each at a different stage. 

![image](https://github.com/user-attachments/assets/e08335a0-2b4c-4e79-a031-07274116b849)

6. In the same window, look at the bottom right corner (shown next), where you can see the *Instruction Memory* window, which helps us follow the program's execution step by step, and the *Execution info* window, which displays performance metrics such as cycles, instructions, and CPI/IPC.

![image](https://github.com/user-attachments/assets/d8c137b5-47f4-420d-b62c-4ae4d6bef39d)



### Exercise 1 - Guided Exercise in Ripes
The following code is executed in Ripes:

```
.text
main:
li x3, 0x4
li x4, 0x6
add x2, x3, x4
sub x5, x2, x3
or  x6, x2, x5
```

Answer the following questions for the Pipelined Processor:

a. Simulate the code in Ripes, obtain the pipeline diagram and explain it.

b. Identify each of the data dependencies that exist in the code and explain how they are resolved in the processor. 

c. Show a screenshot from Ripes that illustrates how the data hazard between the ```add``` and the ```sub``` are handled.


**SOLUTION:**

*a. Simulate the code in Ripes, obtain the pipeline diagram and explain it.*

This is the timing diagram obtained with Ripes:

<p align="center">
  <img src="../../Computer_Organization/Lab2/Images/TimingDiagramRipes.png" width=40% height=40%>
</p>

We observe that there are no stalls in the pipeline, meaning that once it is filled, the CPI (Cycles Per Instruction) is 1.

*b. Identify each of the data dependencies that exist in the code and explain how they are resolved in the processor.*

- ```x3``` is written by the first ```li``` instruction (which the assembler transforms into an ```addi``` instruction) and used by the ```add``` instruction. It is obtained with a forwarding from WB to EX.
- ```x4``` is written by the second ```li``` instruction (which the assembler transforms into an ```addi``` instruction) and used by the ```add``` instruction. It is obtained with a forwarding from MEM to EX.
- ```x2``` is written by the ```add``` instruction and used by the ```sub``` instruction. It is obtained with a forwarding from MEM to EX.
- ```x2``` is written by the ```add``` instruction and used by the ```or``` instruction. It is obtained with a forwarding from WB to EX.
- ```x5``` is written by the ```sub``` instruction and used by the ```or``` instruction. It is obtained with a forwarding from MEM to EX.

<div align="center">

<img src="https://github.com/user-attachments/assets/49d653df-5cd3-4443-ba48-ca53d7b0e208" width="450" />

</div>

*c. Show a screenshot from Ripes that illustrates how the data hazard between the ```add``` and the ```sub``` are handled.*

<div align="center">

<img src="https://github.com/user-attachments/assets/7b2bc8b7-9295-46ef-99b7-f5373bcb05c5" width="450" />

</div>

As shown, the multiplexer within the red square selects the value that comes from the Memory stage (the result of the ```add``` instruction, provided through the yellow wire) as the ALU's first operand (*0x0000000a*), instead of using the value from the Register File.


### Exercise 2 - Guided Exercise in Ripes
Given the following program:

```
.globl main

.data
D: .word 1, 3, 5, 7, 9

.text
main:

la   t1 , D
addi s1 ,x0 ,4
addi s2 ,x0 ,0

for:
	lw   s3, 0(t1)
	lw   s4, 4(t1)
	add  s3, s3, s4
	addi s2 ,s2 ,1
	sub  s3, s3, s2
	sw   s3, 4(t1)
	addi t1, t1, 4
	bne  s2, s1, for

or s2, zero, zero
or s1, zero, zero

fin:
j fin
```

a. Simulate the code in Ripes, obtain the pipeline diagram and explain the hazards and how they are resolved.

b. How many cycles does it take to execute one iteration of the loop? Calculate the CPI.

c. Is it possible to improve the loop's performance by reordering the code? Justify your answer and, if it can be improved, explain how you would modify the code and recalculate the CPI.


**SOLUTION:**
In the following document you can find the complete solution for this exercise: [SolutionExercise8](https://drive.google.com/file/d/15VYkzeFB2zKBXFk5xNL5ffFj5DtK2j1V/view?usp=sharing)



### Exercise 3 in Ripes
The following C code is intended to run on the Ripes Pipelined processor (this code is provided for reference only and should not be used in the exercise below):

```
for ( n = 0; n < 8; n ++ ) {
    for ( k = 0; k < 3; k ++ ) {
    Salida[n] += Filtro[k] * Entrada[n + k];
    }
}
```

To achieve the highest performance in executing this program, the following RISC-V assembly implementation is used (this is the code you will use in the lab):

```
.globl main

.data
Entrada: .word 1, 2, 6, 3, 8, 2, 12, 3, 7, 6
Filtro: .word 3, 7, 8
Salida: .word 0, 0, 0, 0, 0, 0, 0, 0

.text
main:
la   a3 , Entrada
la   a4 , Filtro
la   a5 , Salida
li   a2, 0
li   t1, 3
li   a1, 0
li   t0, 8
loop_n:
 addi a2 , x0 , 0
	loop_k:
   	  lw t3 , 0( a3)
   	  lw t4 , 0( a4)
   	  mul t6 , t3 , t4
   	  lw t5 , 0( a5)
   	  add t5 , t6 , t5
   	  sw t5 , 0( a5)
   	  addi a3 , a3 , 4
   	  addi a4 , a4 , 4
   	  addi a2 , a2 , 1
   	  blt a2 , t1 , loop_k
 addi a5 , a5 , 4
 addi a3 , a3 , -8
 addi a4 , a4 , -12
 addi a1 , a1 , 1
blt a1 , t0 , loop_n
fin:
j fin
```

The RISC-V assembly program is executed in the Ripes Pipelined processor. Answer the following questions:

1. Draw in Ripes the execution diagram at the end of the first iteration of the inner loop (loop_k) and explain the execution of the instructions within the loop, highlighting the data and control hazards that occur and how they are handled.

2. Calculate the CPI of the loop_k loop.

3. Reorder the program, confirm if the result is the same, and recalculate the CPI.


---


## RVfpga-Pipeline
RVfpga-Pipeline is a simulator of the VeeR EH1 pipeline. The simulator can be used from VSCode - PlatformIO. Follow the next steps to simulate an example running on the RVfpga-Pipeline simulator:

1. Start by watching the following video from time 3:12 to time 11:13, to see the RVfpga-Pipeline simulating the same program that we use in the subsequent steps: [RVfpgaToolsVideo](https://youtu.be/Z8QcQRW7F4s?si=8g_GSFpHmIsMQrzI&t=192). ***NOTE:** The video uses a different directory name than the one we are using in the examples and exercises below; however, the contents of the diretories are the identical. Specifically, the ```RVfpga_MasterUCLM/``` directory name used in the video and the ```Simuladores_EC_24-25/RVfpga/``` directory name used below include the same contents.*

2. Open VSCode. Open the project (File - Open Folder) located at the following path: ```/home/rvfpga/Simuladores_EC_24-25/RVfpga/Projects/ProyectoP2```

    To open the project, simply navigate to the directory ```/home/rvfpga/Simuladores_EC_24-25/RVfpga/Projects```, select the ```ProyectoP2``` directory, and click “Open,” as shown in the following screenshot.

<p align="center">
  <img src="../../Computer_Organization/Lab2/Images/OpenFolder.png" width=80% height=80%>
</p>

3. Open the editor in VSCode to view the assembly code of the project called ```Programa.S```

<p align="center">
  <img src="../../Computer_Organization/Lab2/Images/ProgramS.png" width=80% height=80%>
</p>

4. Open the ```platformio.ini``` file and update the path to the RVfpga-Pipeline simulator. To do this, replace the following line:

```
board_debug.verilator.binary = /home/dani/Simuladores_EC_24-25/RVfpga/verilatorSIM_Pipeline/Vrvfpgasim
```

For this one:

```
board_debug.verilator.binary = /home/rvfpga/Simuladores_EC_24-25/RVfpga/verilatorSIM_Pipeline/OriginalBinaries/RVfpga-Pipeline_Ubuntu
```

5. Open the PlatformIO tab and click on the task ```RVfpga-ViDBo/Pipeline```. The simulator will start executing the code (you can see it in the Explorer, inside the ```src``` directory).

<p align="center">
  <img src="../../Computer_Organization/Lab2/Images/RVfpgaVidboPipeline.png" width=40% height=40%>
</p>

6. The simulator starts executing the program, and it only stops when instruction ```and zero, t4, t5``` reaches the Decode stage of the pipeline (note that this instruction has no effect at all in the architectural state of the processor and is simply used as a breakpoint). In the program provided in this project (```ProyectoP2```) this instruction is already included before the ```REPEAT``` loop (see the program above). (If the target program does not have the ```and zero, t4, t5``` instruction, you must add it at the point where you want execution to stop; typically, we place this instruction before entering the loop where the fragment we want to analyze is located.) For example, the following figure shows the simulator at the point where it has stopped execution (you can see that instruction ```and zero, t4, t5``` is at the Decode Stage). Note that the second figure shows a simplified version of the VeeR EH1 microarchitecture, which helps understanding the signals included in the simulator.

<p align="center">
  <img src="../../Computer_Organization/Lab2/Images/RVfpgaPipeline1.png" width=90% height=90%>
</p>

<p align="center">
  <img src="../../Computer_Organization/Lab2/Images/VeeReh1.png" width=90% height=90%>
</p>

7. Continue execution cycle by cycle, by clicking the ```+ 1 Cycle``` button on the right bottom corner of the simulator window, and observe how the program's instructions flow through the VeeR EH1 pipeline.

8. Usually, the programs that we simulate will consist of a loop where the instructions we want to analyze are located (specifically, in the program used in this example, which you can see above, we want to analyze two consecutive ```mul``` instructions, which are placed within a ```REPEAT-OUT``` loop). It is important to analyze an iteration that is not the first or the second one, as some processor structures (branch predictor, instruction cache, etc.) have not yet been “trained” and might obscure the situations we want to analyze. For example, the following figure shows the simulator at the point where instructions from the third, fourth and fifth iterations are executing (at this point the cycles count is Cycles=26).

<p align="center">
  <img src="../../Computer_Organization/Lab2/Images/RVfpgaPipeline2.png" width=90% height=90%>
</p>

9. Let's analyze what the simulator shows in the previous figure:

- **WRITE-BACK stage**
	- *Way-0*: Instruction ```mul t0, t3, t4``` (3rd iteration) is writting its result to the Register File (```waddr0=5``` as register ```t0``` corresponds to x5, ```wen0=1``` as writting is enabled, and ```wd0=6``` which is the result of the first multiplication, 3*2).
 	- *Way-1*: Due to the structural hazard between the two subsequent ```mul``` instructions, the second one was delayed one cycle and a bubble was inserted in this way.
- **COMMIT stage**
	- *Way-0*: Instruction ```mul t1, t5, t6``` (3rd iteration) propagates the result in signal ```i0_result_e4_final=4```, which is the result of the second multiplication (2*2).
 	- *Way-1*: Instruction ```addi t2, t2, -1``` (3rd iteration) propagates the result in signal ```i1_result_e4_final=0xFFFC```, which is the result of this instruction in the third iteration of the loop (0xFFFF - 1 - 1 - 1).
- **EX3/DC3/M3 stage**
	- *Way-0*: Instruction ```bne t2, zero, REPEAT``` (3rd iteration).
 	- *Way-1*: Instruction ```mul t0, t3, t4``` (4th iteration) has just obtained the result of the multiplication (```exu_mul_result_e3=6```).
- **EX2/DC2/M2 stage**
	- *Way-0*: Instruction ```mul t1, t5, t6``` (4th iteration).
 	- *Way-1*: Instruction ```addi t2, t2, -1``` (4th iteration).
- **EX1/DC1/M1 stage**
	- *Way-0*: Instruction ```bne t2, zero, REPEAT``` (4th iteration).
 	- *Way-1*: Instruction ```mul t0, t3, t4``` (5th iteration).
- **DECODE stage** (in the Decode stage information about the origin of the operands is provided: RF/Im means that the operand comes from the Register File or the Immediate, whereas Byp menas that the operand comes through a forwarding path)
	- *Way-0*: Instruction ```mul t1, t5, t6``` (5th iteration). Both operands come from the Register File.
 	- *Way-1*: Instruction ```addi t2, t2, -1``` (5th iteration). The first operand comes through forwarding, whereas the second comes from the Immediate.

10. To stop the simulator, we must close the simulation window and then, in VSCode, click on the Terminal window located at the bottom of the application and press Ctrl+c three times.



## Exercise 4 - Guided Exercise in RVfpga-Pipeline
Consider the RISC-V VeeR EH1 processor. The processor has all configurable features enabled (pipelined execution, superscalar execution, Gshare branch predictor, etc.), except for the Secondary ALU. The following program is executed on this processor:

```
.globl main

.section .midccm
D: .space 16

.text
main:

li t2, 0x080                  # Disable Secondary ALUs
csrrs t1, 0x7F9, t2

la t0, D

li t1, 0x2					
sw t1, (t0)				# D[0] = 2
li t1, 0x4					
sw t1, 4(t0)				# D[1] = 4
li t1, 0x3					
sw t1, 8(t0)				# D[2] = 3
li t1, 0x5					
sw t1, 12(t0)				# D[3] = 5

li s1, 4
mv s2, zero

and zero,t4,t5

for:
   slli t3 ,s2 ,2
   add t2 ,t0 ,t3
   lw s3 , 0(t2)
   lw s4 , 4(t2)
   add s3 ,s3 ,s4
   sw s3 , 0(t2)
   addi s2 ,s2 ,1
   bne s2,s1,for
end:

REPEAT:
   beq  zero, zero, REPEAT  # Repeat the loop
```

Answer the following questions about the ```for``` loop both theoretically and using the RVfpga-Pipeline simulator. Remember to analyze an iteration from the third one onward, avoiding the first/second iterations where there are instruction cache misses and the branch predictor is not yet properly trained. You can use the project located at ```/home/rvfpga/Simuladores_EC_24-25/RVfpga/Projects/ProyectoP2``` and simply replace the program in file ```src/Programa.S``` for the new one.

a. Identify the hazards that occur and explain how this processor handles them.

b. Draw the pipeline diagram for the second iteration of the loop. Unlike Ripes, the RVfpga-Pipeline simulator does not generate this diagram automatically. Therefore, you must create it manually, either on paper or with a tool such as Excel or PowerPoint. Nevertheless, you can still rely on the RVfpga-Pipeline simulation to analyze the program’s behavior cycle by cycle within the loop.

c. Calculate the CPI (Cycles Per Instruction) of the loop.


**SOLUTION:**
We next show partial solutions for this exercise as an example. Complete the solutions not provided.

*a. Identify the hazards that occur and explain how this processor handles them.*

<img width="259" height="271" alt="image" src="https://github.com/user-attachments/assets/77b0ad9d-11c3-4234-a2b2-71582294b623" />

Existing dependencies:

- Data hazards highlighted with colors.

  - They are resolved through forwarding, mostly from a stage after E1 to Decode, and the second way cannot be used in all those cases.
  - Forwarding of the add with the sw is done in E2.
  - In the hazard between the second lw and the add, since the lw is a multicycle operation, it is resolved with 2 stalls and then with forwarding.

- Structural hazard between the two lw. The second one stalls in Decode and executes in the next cycle.
- Control hazard in the bne. When the gshare predictor is enabled, there is no stall on predictor hits, which occurs in almost all iterations (miss in the first and the last).

For example, this figure illustrates the data hazard between the ```slli``` and the ```add``` in the RVfpga-Pipeline simulator.

<img width="311" height="168" alt="image" src="https://github.com/user-attachments/assets/22737ef1-c51e-49a9-bdf9-a4318f5ca6aa" />

The hazard is resolved by:
- Inserting a bubble by the ```slli``` instruction (way-1). We can see that Way 1 in the EX1 Stage is empty (```-----```).
- Performing a forwarding from EX1 to Decode. We can see that: ```out=4 → b=4 (Byp)```.

*b. Draw the pipeline diagram for the second iteration of the loop.*

<p align="center">
  <img src="../../Computer_Organization/Lab2/Images/Ex5-b.png" width=90% height=90%> 
</p>

*c. Calculate the CPI (Cycles Per Instruction) of the loop.*

To calculate the CPI of the loop, simulate until a given instruction of the loop reaches the Decode stage in two consecutive iterations (e.g., the third and fourth iterations). Then, subtract the cycle numbers of these two iterations and divide this result by the number of instructions in the loop.

For example:

<p align="center">
  <img src="../../Computer_Organization/Lab2/Images/Cycle25.png" width=90% height=90%>
</p>

<p align="center">
  <img src="../../Computer_Organization/Lab2/Images/Cycle33.png" width=90% height=90%>
</p>

In this case, ```CPI = (33-25)/8 = 1```




## Exercise 5 in RVfpga-Pipeline
In the VeeR EH1 processor, the following code is to be executed:

```
for ( n = 0; n < 8; n ++ ) {
    for ( k = 0; k < 3; k ++ ) {
    Salida[n] += Filtro[k] * Entrada[n + k];
    }
}
```

To achieve the highest performance in executing this program on the VeeR EH1 processor, the following assembly implementation is decided:

```
.globl main

.section .midccm
Entrada: .space 40
Filtro: .space 12
Salida: .space 32

.text
main:

li t2, 0x488 # Disable Superscalar Exec, Sec. ALUs and Branch Pred.
csrrs t1, 0x7F9, t2

la t0, Entrada
li t1, 0x1   				 
sw t1, (t0)   			 
li t1, 0x3   				 
sw t1, 4(t0)   			 
li t1, 0x5   				 
sw t1, 8(t0)   			 
li t1, 0x7   				 
sw t1, 12(t0)   			 
li t1, 0x9   				 
sw t1, 16(t0)   			 
li t1, 0x1   				 
sw t1, 20(t0)   			 
li t1, 0x3   				 
sw t1, 24(t0)   			 
li t1, 0x5   				 
sw t1, 28(t0)   			 
li t1, 0x7   				 
sw t1, 32(t0)   			 
li t1, 0x9   				 
sw t1, 36(t0)   			 

la t0, Filtro
li t1, 0x2   				 
sw t1, (t0)   			 
li t1, 0x3   				 
sw t1, 4(t0)   			 
li t1, 0x4   				 
sw t1, 8(t0)   			 

la t0, Salida
li t1, 0   				 
sw t1, (t0)   			 
li t1, 0   				 
sw t1, 4(t0)   			 
li t1, 0   				 
sw t1, 8(t0)   			 
li t1, 0   				 
sw t1, 12(t0)   			 
li t1, 0   				 
sw t1, 16(t0)   			 
li t1, 0   				 
sw t1, 20(t0)   			 
li t1, 0   				 
sw t1, 24(t0)   			 
li t1, 0   				 
sw t1, 28(t0)   			 

la   a3 , Entrada
la   a4 , Filtro
la   a5 , Salida

li   a2, 0
li   t1, 3
li   a1, 0
li   t0, 8

nop
nop
nop
nop

and zero, t4, t5

loop_n :
addi a2 , x0 , 0
	loop_k :
    	lw t3 , 0( a3)
    	lw t4 , 0( a4)
    	mul t6 , t3 , t4
    	lw t5 , 0( a5)
    	add t5 , t6 , t5
    	sw t5 , 0( a5)
    	addi a3 , a3 , 4
    	addi a4 , a4 , 4
    	addi a2 , a2 , 1
    	blt a2 , t1 , loop_k
addi a5 , a5 , 4
addi a3 , a3 , -8
addi a4 , a4 , -12
addi a1 , a1 , 1
blt a1 , t0 , loop_n

fin:
j fin
```

Analyze the code in RISC-V assembly. Note that in the assembly program we are initializing the arrays before entering the loops, element-by-element, so this needs quite a few instructions.

**NOTE**: Remember that we can configure the core in order to enable/disable different features, as explained in the corresponding video and reminded next.

<img src="https://github.com/user-attachments/assets/a3fef95e-5b2c-4b7b-a2d7-0021136024b0" alt="image" width="800" />


<img src="https://github.com/user-attachments/assets/9e5c1f7a-4516-44a1-89a5-96748a7a934c" alt="image" width="800" />


You can use the project located at ```/home/rvfpga/Simuladores_EC_24-25/RVfpga/Projects/ProyectoP2``` and simply replace the program in file ```src/Programa.S``` for the new one:

a. Run the assembly program in RVfpga-Pipeline with superscalar execution, the Secondary ALU, and the Gshare branch predictor disabled (this is the default configuration provided in the program above), and stop right at the beginning of iteration n=0, k=1. To get to that iteration, you must skip some cycles after the breakpoint (instruction: and zero, t4, t5). Specifically, you must advance until the point when Cycles=21. At this point, the first instruction of the loop is at the Decode stage. See the following screenshot:

<p align="center">
  <img src="../../Computer_Organization/Lab2/Images/Ex7.png" width=80% height=80%>
</p>

* Draw the execution diagram manually. Explain how data/control/structural hazards are handled by the VeeR EH1 core. 
* Calculate the CPI for iteration n=0, k=1, of the loop_k loop. For that purpose, you must stop the simulation at the point shown above, and count the number of cycles until the same point (first load instruction at Decode stage) of the next iteration. Then, you must divide that number by the number of instructions executed in the loop.

b. Repeat the analysis from *item a* but now enable superscalar execution with respect to the configuration used at *item a*.

c. Repeat the analysis from *item a* but now enable the Gshare branch predictor with respect to the configuration used at *item b*.

d. Repeat the analysis from *item a* but now enable the Secondary ALU with respect to the configuration used at *item c*.

e. Finally, with the configuration of *item d*, reorder the code of the loop_k loop to improve performance as much as possible, and repeat the analysis from *item a*.

