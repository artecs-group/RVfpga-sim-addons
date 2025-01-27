# Ripes processors

## Basic use
Ripes allows simulating many aspects of computer organization, structure, and architecture. In this lab, we will use it to visualize the execution of programs in the Single-Cycle processor and in the 5-stage Pipelined processor. As an example, to configure Ripes for the Pipelined processor, follow these steps:

1. Start the Ripes simulator.
2. Open the Processor tab and in the ```Select Processor``` icon, choose the processor with the following characteristics:
   - Fully pipelined 5-stage processor: "5-stage processor".
   - RISC-V base instruction set plus M extension.
   - Extended layout.

<p align="center">
  <img src="../Images/SelectProc.png" width=60% height=60%>
</p>

3. Add the signal values view in the ```View``` tab.

<p align="center">
  <img src="../Images/View.png" width=40% height=40%>
</p>


## Exercise 1
Consider the 5-stage pipelined RISC-V processor from Harrys & Harrys book (H&H). The following code is executed on this processor:

```
.text
main:
li x3, 0x4
li x4, 0x6
add x2, x3, x4
sub x5, x2, x3
or  x6, x2, x5
```

Answer the following questions:

a. Identify the data dependencies that exist in the code and explain how they are resolved in the processor. Draw the pipeline diagram.

b. On the figure below (obtained from H&H), indicate the values of the data and control signals in the EX, MEM, and WB stages during the cycle when the ```add``` instruction is in the WB stage.

<p align="center">
  <img src="../Images/ProcessorHH.png" width=90% height=90%>
</p>

c. Analyse the program on the Ripes simulator for the 5-stages processor and answer the following questions:
 - Generate in Ripes the pipeline diagram and compare it with your answer to item *a*.
 - Show screenshots of the pipeline to explain how the different data hazards are handled.
 - Stop the execution in the same cycle analyzed in item *b* and compare the values of the data/control signals on the simulator and on your answer to item *b*.


**SOLUTION:**
We next exceptionally show partial solutions for items b and c as an example. Complete the solutions not provided.

*b. On the figure below (obtained from H&H), indicate the values of the data and control signals in the EX, MEM, and WB stages during the cycle when the ```add``` instruction is in the WB stage.*

<p align="center">
  <img src="../Images/Solution_1-c.png" width=90% height=90%>
</p>

*c. Analyse the program on the Ripes simulator.*

*- Generate in Ripes the pipeline diagram and compare it with your answer to item *a*.*

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

*- Stop the execution in the same cycle analyzed in item *b* and compare the values of the data/control signals on the simulator and on your answer to item *b*.*

This is a screenshot of the simulator during the cycle when the ```add``` instruction is in the WB stage.

<p align="center">
  <img src="../Images/Solution_1-d.png" width=90% height=90%>
</p>

You should explain the values of the different data/control signals and compare their values with those from the previous item. Most of them should be equal (although a few signals may differ, given that the two processors are not identical).


## Exercise 2
Consider the 5-stage pipelined RISC-V processor from Harrys & Harrys book (H&H). The following code is executed on this processor:

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

Answer the following questions:

a. Identify the data dependencies that exist in the code and explain how they are resolved in the processor. Draw the pipeline diagram.

b. On the figure below (obtained from H&H), indicate the values of the data and control signals in the 5 pipeline stages during the cycle when the ```lw``` instruction is in the WB stage.

<p align="center">
  <img src="../Images/ProcessorHH.png" width=90% height=90%>
</p>

c. Analyse the program on the Ripes simulator for the 5-stages processor and answer the following questions:
 - Generate in Ripes the pipeline diagram and compare it with your answer to item *a*.
 - Show screenshots of the pipeline to explain how the different data hazards are handled.
 - Stop the execution in the same cycle analyzed in item *b* and compare the values of the data/control signals on the simulator and on your answer to item *b*.


## Exercise 3
Consider the 5-stage pipelined RISC-V processor from Harrys & Harrys book (H&H). The following code is executed on this processor:

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

Answer the following questions:

a. Identify the data dependencies that exist in the code and explain how they are resolved in the processor. Draw the pipeline diagram.

b. On the figure below (obtained from H&H), indicate the values of the data and control signals in the 5 pipeline stages during the cycle when the ```beq``` instruction is in the EX stage.

<p align="center">
  <img src="../Images/ProcessorHH.png" width=90% height=90%>
</p>

c. Analyse the program on the Ripes simulator for the 5-stages processor and answer the following questions:
 - Generate in Ripes the pipeline diagram and compare it with your answer to item *a*.
 - Show screenshots of the pipeline to explain how the different control/data hazards are handled.
 - Stop the execution in the same cycle analyzed in item *b* and compare the values of the data/control signals on the simulator and on your answer to item *b*.


## Exercise 4
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

a. Complete the pipeline diagram of the program in the 5-stage pipelined RISC-V processor from H&H. Assume that the processor has extended the ALU to perform multiplication with a latency of 1 cycle; that is, the ```mul``` instruction executes just like any other arithmetic-logical instruction.

b. Identify the structural, data, and control hazards on the diagram, clearly marking them and explaining how the processor handles each one.

c. Analyse the program on the Ripes simulator for the 5-stages processor and answer the following questions:
 - Generate in Ripes the pipeline diagram and compare it with your answer to item *a*.
 - Show screenshots of the pipeline to explain how the different data/control hazards are handled.
 - Indicate the values of the data and control signals in cycle 5 of the program execution.
