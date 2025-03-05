# Ripes processors
Ripes allows simulating many aspects of computer organization, structure, and architecture. In this lab, we will use it to visualize the execution of programs in two of the simulated processors: *Single-Cycle processor* and *Complete 5-stage Pipelined processor*.

## Building the *Single-Cycle processor*
Look carefully at the following presentation which shows step-by-step how to build the Ripes Single-Cycle processor and several examples of a subset of instructions executing on it: [BuildingRipesSingleCycle](https://drive.google.com/file/d/1ltiDqyqdh34iVbHx_IfEizBPG4y45GcI/view?usp=sharing).

In addition to the previous slides, the following presentation shows step-by-step and in great detail how to build the Single-Cycle processor from the Harris&Harris (H&H) textbook: [SlidesModule5](https://www.fdi.ucm.es/profesor/mendias/FC2/FC2module5.pdf)


## Basic use of the *Single-Cycle processor*
The construction of the Single-Cycle processor is first explained theoretically using the slides provided above. During this explanation, students must perform the corresponding tests from the list below, executing the instructions and carefully analyzing the processor signals in detail.

To use Ripes for the *Single-Cycle processor*, follow these steps:

1. Start the Ripes simulator.

2. Open the Processor tab and in the ```Select Processor``` icon, choose the processor with the following characteristics:
   - Single-Cycle processor.
   - RISC-V base instruction set plus M extension.
   - Extended layout.

![image](https://github.com/user-attachments/assets/ec511bc8-5df3-4fd4-bfae-485d18730213)

3. Add the signal values view in the ```View``` tab.

<p align="center">
  <img src="../Images/View.png" width=40% height=40%>
</p>

4. Perform the example shown in the above slides for the ```sub``` instruction. Use the following code in Ripes:

```
li x2, 5
li x3, 3
sub x1, x2, x3
```

![image](https://github.com/user-attachments/assets/49e6ccc7-630e-4cdc-867f-ffc46cde9f73)

5. Let's perform a simple test in the *Single-Cycle Processor*, extracted from the presentation provided at: [SlidesModule5](https://www.fdi.ucm.es/profesor/mendias/FC2/FC2module5.pdf). Copy the following program into the Editor tab.

```
.data
xa: .word 10
xb: .word 0
xc: .word 0

.text
la x9, xa
L7:
    lw x6, 0(x9)
    sw x6, 8(x9)
    or x4, x5, x6
    beq x4, x4, L7
```

6. Perform the simulation of one iteration of loop L7 in the Single-Cycle processor, cycle-by-cycle, and analyze the control/data signals shown in red in the following figure.

![image](https://github.com/user-attachments/assets/9ae3407b-0b31-4796-8aa8-c7d7ad02dc8f)

7. These are the screenshots showing the execution of each instruction in the loop and the explanation of the control/data signals:

- ```LW``` instruction:
![image](https://github.com/user-attachments/assets/eac7cb38-1c60-4ab9-a0a2-d7cb44f56eb8)

   - ```Addr``` = 0x8, which is the address where the ```lw``` instruction (```0x0004a303```) is placed in memory. See next the instructions in the Ripes memory tab:

     <img src="https://github.com/user-attachments/assets/e6d5f9c2-06cd-49a1-929f-baf7e5575f88" width="300"/>

   - ```PC``` = 0xc, which is the address where the instruction following the ```lw``` is stored in memory and will be fetched in the next cycle.

- ```SW``` instruction:
![image](https://github.com/user-attachments/assets/8ba109e6-ec28-4a83-9799-0a7baebbdd1d)

- ```OR``` instruction:
![image](https://github.com/user-attachments/assets/c5a48734-9266-4b27-b8db-dfaacc324b3c)

- ```BEQ``` instruction:
![image](https://github.com/user-attachments/assets/8c87f9b6-1305-4518-985d-c91064c303de)


## Exercise 1
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

Simulate the program cycle-by-cycle and stop when the ```add``` instruction is executing. What is the value of the signals highlighted in the following figure? Justify each value obtained.

![image](https://github.com/user-attachments/assets/d57bdd0a-0e63-4cc2-974a-2cd80bc1f53d)


**SOLUTION:**
We next show the solution for this exercise as an example.

![image](https://github.com/user-attachments/assets/c0795f78-57a6-4cee-be5f-38a2994043c7)

- ```PC``` = 0x8, which is the address where the ```add``` instruction is placed in memory.
- ```Instr``` = 0x00418133, which are the 32 bits representing the ```add``` instruction.
- ```R1``` and ```R2``` = 0x3 and 0x4, which are the indexes of the two source registers.
- ```Wr``` = 0x2, which is the index of the destination register.
- ```ALU-Op1``` and ```ALU-Op2``` = 0x4 and 0x6, which are the operands that the instruction must add.
- ```ALU-Res``` = 0xa, which is the result of the addition.
- ```3:1 Mux output``` = 0xa, which is the value to write in the Register File.
- ```Write Enable RF``` = 1, as the result of the addition must be saved in the Register File.
- ```2:1 Muxes control``` = REG1 and REG2, as the multiplexers must select the two registers as the ALU input operands.
- ```3:1 Mux control``` = ALURES, as the 3:1 multiplexer must select the ALU output.


## Exercise 2
The following code is executed in Ripes:

```
.data
v: .word 1, 10
.text
main:
la x1 , v
li x2, 0x2
li x3, 0x4
lw x2, 4(x1)
sub x5, x2, x3
or  x6, x2, x5
```

Simulate the program cycle-by-cycle and stop when the ```lw``` instruction is executing. Explain the values of each of the data/control signals obtained in the simulation.


## Exercise 3
The following code is executed in Ripes:

```
.text
main:
li x1, 0x8
li x2, 0x8
li x3, 0x4
beq x2, x1, ELSE
IF:	
   sub x5, x2, x3
    or  x6, x2, x5
    beq x0, x0, END
ELSE:
   add x5, x2, x3
    and x6, x2, x5
END:
nop
```

Answer the following questions for the Single-Cycle Processor:

a. Simulate the program cycle-by-cycle and stop when the first ```beq``` instruction is executing. Explain the values of each of the data/control signals obtained in the simulation.

b. Then, modify the ```x1``` register initialization to 0x7, and analyze the first ```beq``` instruction execution. Explain the values of each of the data/control signals obtained in the simulation.

c. Explain the differences observed between the two cases.

---
## Building the *Pipelined processor*
Look at the following presentation which shows step-by-step how to build the Ripes Pipelined processor and several examples of a subset of instructions executing on it: [BuildingRipesPipelined](https://drive.google.com/file/d/1YEU6boOllnm3OXSRJV4YFuy86CcGv4En/view?usp=sharing).

In addition, the following presentation shows step-by-step and in great detail how to build the Pipelined processor from the Harris&Harris textbook [SlidesModule7](https://www.fdi.ucm.es/profesor/mendias/FC2/FC2module7.pdf).


## Basic use of the *Pipelined processor*
The construction of the Pipelined processor is first explained theoretically using the slides provided above. During this explanation, students must perform the corresponding tests from the list below, executing the instructions and carefully analyzing the processor signals in detail.

1. Start the Ripes simulator.

2. Open the Processor tab and in the ```Select Processor``` icon, choose the processor with the following characteristics:
   - 5-stage processor.
   - RISC-V base instruction set plus M extension.
   - Extended layout.

<p align="center">
  <img src="../Images/SelectProc.png" width=60% height=60%>
</p>

3. Add the signal values view in the ```View``` tab.

<p align="center">
  <img src="../Images/View.png" width=40% height=40%>
</p>

4. Perform the example shown in the above slides for the ```sub``` instruction. Use the following code in Ripes:

```
li x2, 5
li x3, 3
nop
nop
nop
nop
sub x1, x2, x3
```

5. Analyze the ```addi``` instruction in the following example. Highlight the differences with respect to the execution of a ```sub``` instruction.

```
li x2, 5
li x3, 3
nop
nop
nop
nop
addi x1, x2, x3
```

6. Analyze the ```lw``` instruction in the following example.

```
.data
a: .word 5
.text
la x2, a
nop
nop
nop
nop
lw x1, 0(x2)
```

7. Analyze the ```sw``` instruction in the following example.

```
.data
a: .word 0
.text
li x1, 2
la x2, a
nop
nop
nop
nop
sw x1, 0(x2)
```

<!--
8. Analyze the ```beq``` instruction in the following example. Test both taken and non-taken branches by modifying the initial values of ```x2``` and ```x3```.

```
li x2, 5
li x3, 5
REPEAT:
nop
nop
nop
nop
beq x3, x2, REPEAT
addi x2, x2, 1
addi x3, x3, 1
```
-->


## Data and Control Hazards in the *Pipelined processor*
Look at the following presentation which shows, from slide 53 to slide 130, how hazards are handled in the Harris&Harris textbook [SlidesModule7](https://www.fdi.ucm.es/profesor/mendias/FC2/FC2module7.pdf).


## Exercise 4
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

a. Identify the data dependencies that exist in the code and explain how they are resolved in the processor. 

b. Draw the pipeline diagram in paper.

<!--
b. On the figure below (obtained from H&H), indicate the values of the data and control signals in the EX, MEM, and WB stages during the cycle when the ```add``` instruction is in the WB stage.

<p align="center">
  <img src="../Images/ProcessorHH.png" width=90% height=90%>
</p>
-->

c. Analyse the program on the Ripes simulator for the 5-stages processor and answer the following questions:
 - Generate in Ripes the pipeline diagram and compare it with your previous answer.
 - Show screenshots of the pipeline to explain how the different data hazards are handled.
 - Stop the execution during the cycle when the ```add``` instruction is in the WB stage and analyze the data/control signals.


**SOLUTION:**
We next show partial solutions for item c as an example. Complete the solutions not provided.

<!--
*b. On the figure below (obtained from H&H), indicate the values of the data and control signals in the EX, MEM, and WB stages during the cycle when the ```add``` instruction is in the WB stage.*

<p align="center">
  <img src="../Images/Solution_1-c.png" width=90% height=90%>
</p>
-->

*c. Analyse the program on the Ripes simulator.*

*- Generate in Ripes the pipeline diagram and compare it with your previous answer.*

This is the timing diagram obtained with Ripes:

<p align="center">
  <img src="../Images/TimingDiagramRipes.png" width=40% height=40%>
</p>

*- Show screenshots of the pipeline to explain how the different data hazards are handled.*

This is a screenshot of the simulator that highlights the forwarding that occurs between the first ```li``` and the ```add```:

<p align="center">
  <img src="../Images/FwdOp1.png" width=60% height=60%>
</p>

You should explain how the hazard is handled by the pocessor: which multiplexers are used, the stages involved, etc.

*- Stop the execution during the cycle when the ```add``` instruction is in the WB stage and analyze the data/control signals.*

This is a screenshot of the simulator during the cycle when the ```add``` instruction is in the WB stage.

<p align="center">
  <img src="../Images/Solution_1-d.png" width=90% height=90%>
</p>

You should explain the values of the different data/control signals and compare their values with those from the previous item. Most of them should be equal (although a few signals may differ, given that the two processors are not identical).


## Exercise 5
The following code is executed in Ripes:

```
.data
v: .word 1, 10
.text
main:
la x1 , v
li x2, 0x2
li x3, 0x4
lw x2, 4(x1)
sub x5, x2, x3
or  x6, x2, x5
```

Answer the following questions for the 5-stage Pipelined Processor:

a. Identify the data dependencies that exist in the code and explain how they are resolved in the processor. 

b. Draw the pipeline diagram.

<!--
b. On the figure below (obtained from H&H), indicate the values of the data and control signals in the 5 pipeline stages during the cycle when the ```lw``` instruction is in the WB stage.

<p align="center">
  <img src="../Images/ProcessorHH.png" width=90% height=90%>
</p>
-->

c. Analyse the program on the Ripes simulator for the 5-stages processor and answer the following questions:
 - Generate in Ripes the pipeline diagram and compare it with your previous answer.
 - Show screenshots of the pipeline to explain how the different data hazards are handled.
 - Stop the execution during the cycle when the ```lw``` instruction is in the WB stage and analyze the data/control signals.


## Exercise 6
The following code is executed in Ripes:

```
.text
main:
li x1, 0x8
li x2, 0x8
li x3, 0x4
beq x2, x1, ELSE
IF:	
   sub x5, x2, x3
    or  x6, x2, x5
    beq x0, x0, END
ELSE:
   add x5, x2, x3
    and x6, x2, x5
END:
nop
```

Answer the following questions for the 5-stage Pipelined Processor:

a. Identify the data dependencies that exist in the code and explain how they are resolved in the processor. 

b. Draw the pipeline diagram.

<!--
b. On the figure below (obtained from H&H), indicate the values of the data and control signals in the 5 pipeline stages during the cycle when the first ```beq``` instruction is in the EX stage.

<p align="center">
  <img src="../Images/ProcessorHH.png" width=90% height=90%>
</p>
-->

c. Analyse the program on the Ripes simulator for the 5-stages processor and answer the following questions:
 - Generate in Ripes the pipeline diagram and compare it with your previous answer.
 - Show screenshots of the pipeline to explain how the different data hazards are handled.
 - Stop the execution during the cycle when the first ```beq``` instruction is in the EX stage and analyze the data/control signals.


## Exercise 7
Given the following code, which calculates the factorial of the number stored in register t0 (it is assumed to always be an integer greater than 1) and stores the result in the same t0 register:

```
.text
main:

addi t0, x0, 4
addi t1, x0, 1
addi t2, t0, -1

NEXT:
ble t2, t1, END
mul t0, t0, t2
addi t2, t2, -1
j NEXT

END:

addi t1, x0, 0
addi t0, x0, 0
```

<!--
a. Complete the pipeline diagram of the program in the 5-stage pipelined RISC-V processor from H&H. Assume that the processor has extended the ALU to perform multiplication with a latency of 1 cycle; that is, the ```mul``` instruction executes just like any other arithmetic-logical instruction.
-->

a. Draw the pipeline diagram in paper. Identify the structural, data, and control hazards on the diagram, clearly marking them and explaining how the processor handles each one.

b. Analyse the program on the Ripes simulator for the 5-stages processor and answer the following questions:
 - Generate in Ripes the pipeline diagram and compare it with your answer to item *a*.
 - Show screenshots of the pipeline to explain how the different data/control hazards are handled.
 - Indicate the values of the data and control signals in cycle 5 of the program execution.


---


### Lab 5
Given the following code, simulate it in the Ripes Single-Cycle processor and answer the following questions.

```
CODE (to be shown next April)
```



### Lab 6
Given the following code, simulate it in the Ripes Pipelined processor and answer the following questions.

```
CODE (to be shown next April)
```
