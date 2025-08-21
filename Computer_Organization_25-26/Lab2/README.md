# Lab 2 - The Ripes core and the VeeR EH1 core
This practice aims to help students gain a thorough understanding of the commercial VeeR EH1 core, an advanced 2-way superscalar processor with 9 pipeline stages. The processor is explained both theoretically, through a detailed presentation, and practically, using the RVfpga-Pipeline simulator. As a preparatory step, we first focus on the typical academic 5-stage pipelined processor, exploring it theoretically (using the pipelined processor from the Harris and Harris book, H&H) and practically (through the Ripes simulator). 

Follow the next steps:

1. **Ripes core:** You can start using Ripes to simulate and analyze a 5-stage processor that is almost identical to the one described in the H&H textbook.

    * Read again the instructions provided at [Ripes_Introduction](https://github.com/mortbopet/Ripes/blob/master/docs/introduction.md).
    * Replicate the instructions provided below in section *Basic use of the Pipelined processor*.
    * Finally, complete exercises ...

2. **VeeR EH1 core:** Once you have a clear understanding of the 5-stage processor used in the textbook and the one used in Ripes, you will start your analysis of a more complex processor, the VeeR EH1 core.

    * ...
    * ...


## Basic use of the *Pipelined processor*
The construction of the Pipelined processor is first explained theoretically using the slides provided above. During this explanation, students must perform the corresponding tests from the list below, executing the instructions and carefully analyzing the processor signals in detail.

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

#### Analysis of the final cycle: ```lw``` - ```beq``` - ```add``` - ```or``` - ```sw```

Advance step-by-step until the final cycle. This is the processor in that cycle. As you can see, five instructions are being executed simultaneously in the processor (in-flight), each at a different stage. 

![image](https://github.com/user-attachments/assets/e08335a0-2b4c-4e79-a031-07274116b849)

We'll use the signal names provided in the following figure.

![image](https://github.com/user-attachments/assets/4e7c4b1d-6e77-404e-af28-32e5607c94c6)

In the same window, look at the bottom right corner (shown next), where you can see the *Instruction Memory* window, which helps us follow the program's execution step by step, and the *Execution info* window, which displays performance metrics such as cycles, instructions, and CPI/IPC.

![image](https://github.com/user-attachments/assets/d8c137b5-47f4-420d-b62c-4ae4d6bef39d)

Let's analyze a few important signals of the pipeline in this cycle.

   - ```sw``` instruction:
      - ```Addr```= 0x2c, which is the address where the store instruction is placed in the Instruction Memory. Confirm this in the memory tab.
      - ```Instr```= 0x0064a423. You can confirm, using the slides from Module 4, that this hexadecimal value corresponds to the ```sw``` instruction included in the program.

   - ```or``` instruction:
      - ```Reg1```= 0x3. This will be used as the first operand for the OR operation that will be performed next cycle.
      - ```Reg2```= 0x3. This will be used as the second operand for the OR operation that will be performed next cycle.
      - ```C1(d)```= 1. This will be the Register File write enable in the WB stage. The ```or``` instruction must write the result to the RF.
      - ```C2(d)```= ALURES. This will be used to select the data in the 3-1 multiplexer of the WB stage.
      - ```C6(d)```= 0, as it is not a ```jump``` instruction.
      - ```C7(d)```= 0, as it is not a ```branch``` instruction.
      - ```C8(d)```= ```C9(d)```= REG1/2, as the operands are provided from the Register File in this instruction.
      - ```C10(d)```= OR, as the ALU must perform an OR operation.

   - ```add``` instruction:
      - ```Op1```= 0x2. This is the first operand for the ADD operation that is performed this cycle.
      - ```Op2```= 0x2. This is the second operand for the ADD operation that is performed this cycle.
      - ```C1(e)```= 1. This will be the Register File write enable in the WB stage. The ```add``` instruction must write the result to the RF.
      - ```C2(e)```= ALURES. This will be used to select the data in the 3-1 multiplexer of the WB stage.
      - ```C6(e)```= 0, as it is not a ```jump``` instruction.
      - ```C7(e)```= 0, as it is not a ```branch``` instruction.
      - ```C8(e)```= ```C9(e)```= REG1/2, as the operands are provided from the Register File in this instruction.
      - ```C10(e)```= ADD, as the ALU must perform an ADD operation.
      - ```Res```= 0x4, which is the result of the addition.
      - ```C14```= 0, as the next PC after the ```add``` instruction is PC+4.

   - ```beq``` instruction:
      - ```C1(m)```= ```C3(m)```= 0, as neither the Data Memory nor the Register File must be written by this instruction.

   - ```lw``` instruction:
      - ```C1(w)```= 1, as the Register File must be written by this instruction.
      - ```C2(w)```= 0, as the 3-1 multiplexer must select the data read from memory.
      - ```Wr```= 0x6, which is the register idx where the value read from memory must be written.
      - ```DInRF```= 0xa, which is the data read from memory that must be written to the RF.


