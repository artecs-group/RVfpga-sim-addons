#define GPIO_SWs    0x80001400
#define GPIO_LEDs   0x80001404
#define GPIO_INOUT  0x80001408

.globl main
main:

li x28, 0xFFFF
li x29, GPIO_INOUT
sw x28, 0(x29)                  # Write the Enable Register

next:
    li  a1, GPIO_SWs            # Read the Switches
    lw  t0, 0(a1)

    li  a0, GPIO_LEDs
    srl t0, t0, 16
    sw  t0, 0(a0)               # Write the LEDs

    beq zero, zero, next
.end
