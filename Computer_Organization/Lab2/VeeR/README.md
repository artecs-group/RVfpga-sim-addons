# The VeeR EH1 processor

## RVfpga-Pipeline
RVfpga-Pipeline is a simulator of the VeeR EH1 pipeline. The simulator can be used from VSCode - PlatformIO. Follow the next steps to simulate an example running on the RVfpga-Pipeline simulator:

*NOTE: The RVfpga-Pipeline simulator provided may differ a bit from the one used in the documents/slides/videos. For example, the latest version specifies, at the Decode Stage, if the operands come from the Register File or the Immediate (text **(RF/Im)** and red color), or from a Bypass Path (text **(Byp)** and green color).*

1. Start by watching the following video from time 3:12 to time 11:13, to see the RVfpga-Pipeline simulating the same program that we use in the subsequent steps: [RVfpgaToolsVideo](https://youtu.be/Z8QcQRW7F4s?si=8g_GSFpHmIsMQrzI&t=192) (the video is in Spanish, but you can watch an AI-translated-to-English version of the video here [RVfpgaToolsEnglishVideo](https://youtu.be/HuAF2XOMQmQ?si=-LpY-J7f-ng9AYAa&t=192), you can watch an AI-translated-to-Chinese version of the video here [RVfpgaToolsChineseVideo](https://youtu.be/A_c8GACrW9w?si=gst8rw2755R_JtMA&t=192), or you can enable the subtitles in the original video). ***NOTE:** The video uses a different directory name than the one we are using in the examples and exercises below; however, the contents of the diretories are the identical. Specifically, the ```RVfpga_MasterUCLM/``` directory name used in the video and the ```Simuladores_EC_24-25/RVfpga/``` directory name used below include the same contents.*

2. Open VSCode. Open the project (File - Open Folder) located at the following path: ```/home/rvfpga/Simuladores_EC_24-25/RVfpga/Projects/ProyectoP2```

    To open the project, simply navigate to the directory ```/home/rvfpga/Simuladores_EC_24-25/RVfpga/Projects```, select the ```ProyectoP2``` directory, and click “Open,” as shown in the following screenshot.

<p align="center">
  <img src="../Images/OpenFolder.png" width=80% height=80%>
</p>

3. Open the editor in VSCode to view the assembly code of the project called ```Programa.S```

<p align="center">
  <img src="../Images/ProgramS.png" width=80% height=80%>
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
  <img src="../Images/RVfpgaVidboPipeline.png" width=40% height=40%>
</p>

6. The simulator starts executing the program, and it only stops when instruction ```and zero, t4, t5``` reaches the Decode stage of the pipeline (note that this instruction has no effect at all in the architectural state of the processor and is simply used as a breakpoint). In the program provided in this project (```ProyectoP2```) this instruction is already included before the ```REPEAT``` loop (see the program above). (If the target program does not have the ```and zero, t4, t5``` instruction, you must add it at the point where you want execution to stop; typically, we place this instruction before entering the loop where the fragment we want to analyze is located.) For example, the following figure shows the simulator at the point where it has stopped execution (you can see that instruction ```and zero, t4, t5``` is at the Decode Stage). Note that the second figure shows a simplified version of the VeeR EH1 microarchitecture, which helps understanding the signals included in the simulator.

<p align="center">
  <img src="../Images/RVfpgaPipeline1.png" width=90% height=90%>
</p>

<p align="center">
  <img src="../Images/VeeReh1.png" width=90% height=90%>
</p>

7. Continue execution cycle by cycle, by clicking the ```+ 1 Cycle``` button on the right bottom corner of the simulator window, and observe how the program's instructions flow through the VeeR EH1 pipeline.

8. Usually, the programs that we simulate will consist of a loop where the instructions we want to analyze are located (specifically, in the program used in this example, which you can see above, we want to analyze two consecutive ```mul``` instructions, which are placed within a ```REPEAT-OUT``` loop). It is important to analyze an iteration that is not the first or the second one, as some processor structures (branch predictor, instruction cache, etc.) have not yet been “trained” and might obscure the situations we want to analyze. For example, the following figure shows the simulator at the point where instructions from the third, fourth and fifth iterations are executing (at this point the cycles count is Cycles=26).

<p align="center">
  <img src="../Images/RVfpgaPipeline2.png" width=90% height=90%>
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

Then, visualize the following presentation: ([PresentationRVfpgaPipeline](https://drive.google.com/file/d/1fAJMpsBv3IGf3DBGVOAmqnDocVmarly0/view?usp=drive_link)), and reproduce and analyze all the examples provided in it. To simulate the programs in RVfpga-Pipeline, you only must copy the codes from the presentation into the file ```src/Programa.S```. Verify that the diagrams and CPIs indicated in the presentation match what you get in the simulations. Specifically, you must simulate the following examples:

- RVfpga-Pipeline:

    * Program without dependencies
    * Structural hazard: consecutive mul-mul instructions
    * Data hazard: consecutive add-add instructions
    * Data hazard - Multi-cycle instructions: mul-add
    * Control hazard
    * Example program analyzed in the video shown above and provided in this [document](https://drive.google.com/file/d/1ltE_sOyaw090Sk49o8gLpa4MJNTl3yZz/view?usp=sharing).

---

## Exercise 1
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

b. Draw the pipeline diagram for the second iteration of the loop.

c. Calculate the CPI (Cycles Per Instruction) of the loop.

d. Indicate on the following figure where each instruction is and the values of the various signals of the VeeR EH1 processor in the cycle when the first ```load``` instruction is in the Write-Back stage. Show also a screenshot of the RVfpga-Pipeline simulator in that same cycle.

<p align="center">
  <img src="../Images/VeeReh1.png" width=90% height=90%>
</p>

e. Show a screenshot of the RVfpga-Pipeline simulator in the cycle when the two ```load``` instructions perform a forwarding to the subsequent ```add``` instruction.

f. Reorder the code to try to improve performance. Calculate the new CPI.

g. Recalculate the CPI of the loop assuming that the Secondary ALU available in the Commit stage is activated and that the code is reordered as per the previous step.

**NOTE**: Remember that we can configure the core in order to enable/disable different features, as explained in the corresponding video and reminded next.

---

<img src="https://github.com/user-attachments/assets/a3fef95e-5b2c-4b7b-a2d7-0021136024b0" alt="image" width="800" />

---

<img src="https://github.com/user-attachments/assets/9e5c1f7a-4516-44a1-89a5-96748a7a934c" alt="image" width="800" />

---

**SOLUTION:**
We next show partial solutions for this exercise as an example. Complete the solutions not provided.

*a. Identify the hazards that occur and explain how this processor handles them.*

For example, this figure illustrates the data hazard between the ```slli``` and the ```add```.

<p align="center">
  <img src="../Images/Hazard1st2ndInstructions.png" width=50% height=50%> 
</p>

The hazard is handled by:
- Inserting a bubble by the ```slli``` instruction (way-1). We can see that Way 1 in the EX1 Stage is empty (```-----```).
- Performing a forwarding from EX1 to Decode. We can see that: ```out=4 → b=4 (Byp)```.

*b. Draw the pipeline diagram for the second iteration of the loop.*

<p align="center">
  <img src="../Images/Ex5-b.png" width=90% height=90%> 
</p>

*c. Calculate the CPI (Cycles Per Instruction) of the loop.*

To calculate the CPI of the loop, simulate until a given instruction of the loop reaches the Decode stage in two consecutive iterations (e.g., the third and fourth iterations). Then, subtract the cycle numbers of these two iterations and divide this result by the number of instructions in the loop.

For example:

<p align="center">
  <img src="../Images/Cycle25.png" width=90% height=90%>
</p>

<p align="center">
  <img src="../Images/Cycle33.png" width=90% height=90%>
</p>

In this case, ```CPI = (33-25)/8 = 1```

*d. Indicate on the following figure where each instruction is and the values of the various signals of the VeeR EH1 processor in the cycle when the first load instruction is in the Write-Back stage.*

<p align="center">
  <img src="../Images/Solution_5-f.png" width=90% height=90%>
</p>

<p align="center">
  <img src="../Images/Solution_5-f_Simulator.png" width=90% height=90%> 
</p>

*e. Show a screenshot of the RVfpga-Pipeline simulator in the cycle when the two ```load``` instructions perform a forwarding to the subsequent ```add``` instruction.*

<p align="center">
  <img src="../Images/Solution_5-e_Simulator.png" width=90% height=90%> 
</p>



## Exercise 2
Given the following program, which can be executed in RVfpga-Pipeline (using the first code below) and in Ripes (using the second code below):

**RVfpga-Pipeline:**

```
.globl main

.section .midccm
D: .space 20

.text
main:

li t2, 0x080             # Disable Secondary ALUs
csrrs t1, 0x7F9, t2

la t0, D

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

la   t1 , D
addi s1 ,x0 ,4
addi s2 ,x0 ,0

and zero, t4, t5

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

**Ripes:**

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

a. Draw the execution diagram of the program on the H&H 5-stage pipelined processor, from the beginning of the second iteration of the loop until the cycle in which the ```add``` instruction exits the pipeline in the third iteration. Indicate on the diagram the structural, data, and control dependencies that arise and explain for each one how the processor handles it.

b. Simulate the program in Ripes. How many cycles does it take to execute one iteration?

c. Is it possible to improve the loop's performance by reordering the code? Justify your answer and, if it can be improved, explain how you would modify the code.

d. Indicate the values of all data and control signals in the cycle where the ```add``` instruction is in the execution stage. Also, indicate which instruction is in each stage. Assume that the address of the first instruction is 0.

e. Draw the execution diagram of the program on the VeeR EH1 processor, from the beginning of the second iteration of the loop until the cycle in which the ```add``` instruction exits the pipeline in the third iteration. Indicate on the diagram the structural, data, and control dependencies that arise and explain for each one how the processor handles it.

f. Simulate the program in RVfpga-Pipeline (you can use the project located at ```/home/rvfpga/Simuladores_EC_24-25/RVfpga/Projects/ProyectoP2``` and simply replace the program in file ```src/Programa.S``` for the new one). How many cycles does it take to execute one iteration?

g. Is it possible to improve the loop's performance by reordering the code? Justify your answer and, if it can be improved, explain how you would modify the code.



## Exercise 3
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

Solve the following sections, both theoretically and practically on the RVfpga-Pipeline simulator. You can use the project located at ```/home/rvfpga/Simuladores_EC_24-25/RVfpga/Projects/ProyectoP2``` and simply replace the program in file ```src/Programa.S``` for the new one:

a. Run the assembly program in RVfpga-Pipeline with superscalar execution, the Secondary ALU, and the Gshare branch predictor disabled (this is the default configuration provided in the program above), and stop right at the beginning of iteration n=0, k=1. To get to that iteration, you must skip some cycles after the breakpoint (instruction: and zero, t4, t5). Specifically, you must advance until the point when Cycles=21. At this point, the first instruction of the loop is at the Decode stage. See the following screenshot:

<p align="center">
  <img src="../Images/Ex7.png" width=80% height=80%>
</p>

* Draw the execution diagram.
* Analyze the data/control/structural hazards for this iteration. For that purpose, simulate cycle-by-cycle and analyze and explain how each hazard is handled by the VeeR EH1 core. 
* Calculate the CPI for iteration n=0, k=1, of the loop_k loop. For that purpose, you must stop the simulation at the point shown above, and count the number of cycles until the same point (first load instruction at Decode stage) of the next iteration. Then, you must divide that number by the number of instructions executed in the loop.

b. Repeat the analysis from *item a* but now enable superscalar execution with respect to the configuration used at *item a*.

c. Repeat the analysis from *item a* but now enable the Gshare branch predictor with respect to the configuration used at *item b*.

d. Repeat the analysis from *item a* but now enable the Secondary ALU with respect to the configuration used at *item c*.

e. Finally, with the configuration of *item d*, reorder the code of the loop_k loop to improve performance as much as possible, and repeat the analysis from *item a*.



## Exercise 4
Similarly to what we did in the video for the bypass 10-1 multiplexer, where we found it in the SoC Verilog code, try to find the following elements (in our case, the Verilog files for the VeeR EH1 core are in folder ```/home/rvfpga/Simuladores_EC_24-25/RVfpga/src/SweRVolfSoC/SweRVEh1CoreComplex```):

+ 3-1 multiplexer:

<p align="center">
  <img src="../Images/3-1mux.png" width=20% height=20%> 
</p>

+ ALU in the I0 Pipe:

<p align="center">
  <img src="../Images/ALU.png" width=40% height=40%> 
</p>

+ Register File:

<p align="center">
  <img src="../Images/RF.png" width=20% height=20%> 
</p>

+ Multiplier and forwarding path from the load:

<p align="center">
  <img src="../Images/LS-Mul.png" width=60% height=60%> 
</p>
