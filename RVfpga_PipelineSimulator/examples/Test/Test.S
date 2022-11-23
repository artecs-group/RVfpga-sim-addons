#define INSERT_NOPS_1	   nop;
#define INSERT_NOPS_2	   nop; INSERT_NOPS_1
#define INSERT_NOPS_3	   nop; INSERT_NOPS_2
#define INSERT_NOPS_4	   nop; INSERT_NOPS_3
#define INSERT_NOPS_5	   nop; INSERT_NOPS_4
#define INSERT_NOPS_6	   nop; INSERT_NOPS_5
#define INSERT_NOPS_7	   nop; INSERT_NOPS_6
#define INSERT_NOPS_8	   nop; INSERT_NOPS_7
#define INSERT_NOPS_9	   nop; INSERT_NOPS_8
#define INSERT_NOPS_10	   nop; INSERT_NOPS_9

.globl main

.section .midccm
A: .space 16

.data
D: .word 3,5,6,8,7,10,12,2,1,4,11,9


.text
main:

li t2, 0x028               # Disable non-blocking loads and Branch Predictor.
csrrs t1, 0x7F9, t2

li t3, 0x4                 # t3 = 4
li t4, 0x1                 # t4 = 1
li t5, 0x2                 # t5 = 2

la t0, A					# t0 = addr(A)
li t1, 0x2					# t1 = 2
sw t1, (t0)					# A[0] = 2
add t1,t1,6				    # t1 = 8
sw t1, 4(t0)				# A[1] = 8

la t1, D
li t2, 12
li t6, 0x0

REPEAT:
   INSERT_NOPS_6
   add t3, t3, t3        
   add t3, t3, t3
   mul t3, t3, t4
   mul t5, t5, t5
  	lw t3, 4(t0)
   lw t3, (t1)
   INSERT_NOPS_6
   add t1, t1, 4
   // Control Instruction
   and t2, t4, t5
   INSERT_NOPS_6
   beq  zero, zero, REPEAT # Repeat the loop
   INSERT_NOPS_10


.end