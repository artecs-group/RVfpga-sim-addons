# VeeRWolf Zephyr Module

The folder `$VEERWOLF_ROOT/fusesoc_libraries/veerwolf/zephyr` defines a module used for compiling programs for the veerwolf_nexys board. Below is a concise overview of its key components. A detailed analysis of all the files is left as an exercise.

**TASK:** Before analyzing the module, review the [Introduction to Devicetree](https://docs.zephyrproject.org/2.7.4/guides/dts/intro.html) and follow the steps outlined in the [Devicetree HOWTO](https://docs.zephyrproject.org/2.7.4/guides/dts/howtos.html) to build a solid foundational understanding.

## File tree of the module

```
➜  zephyr git:(main) tree 
.
├── boards
│   └── riscv
│       └── veerwolf_nexys
│           ├── board.h
│           ├── CMakeLists.txt
│           ├── Kconfig.board
│           ├── Kconfig.defconfig
│           ├── veerwolf_nexys_defconfig
│           ├── veerwolf_nexys.dts
│           └── veerwolf_nexys.yaml
├── CMakeLists.txt
├── drivers
│   ├── CMakeLists.txt
│   ├── gpio
│   │   ├── CMakeLists.txt
│   │   ├── gpio_veerwolf.c
│   │   └── Kconfig
│   └── Kconfig
├── dts
│   ├── bindings
│   │   └── gpio
│   │       └── veerwolf,gpio.yaml
│   └── riscv
│       └── riscv32-veer.dtsi
├── Kconfig
├── module.yml
└── soc
    ├── Kconfig
    └── riscv
        └── veerwolf
            ├── CMakeLists.txt
            ├── dts_fixup.h
            ├── irq.c
            ├── Kconfig.defconfig
            ├── Kconfig.soc
            ├── linker.ld
            ├── soc.c
            ├── soc_common.h
            ├── soc.h
            ├── soc_irq.S
            └── vector.S

13 directories, 29 files
```

## Boards definition

The folder `boards/riscv/veerwolf_nexys` contains the files required to define the board. Below, we summarize the most relevant ones:

* `Kconfig.board`:  *Kconfig* file that makes the board available as a selectable option in the *Kconfig menu*.

* `Kconfig.defconfig`:  *Kconfig* file specifies additional board-specific default settings; it provides supplementary defaults for features or peripherals required by the board.

* `veerwolf_nexys_defconfig`: Provides the complete, ready-to-use default configuration for building applications.

* `veerwolf_nexys.dts`: board's *devitceree file*, for more information see [*Zephyr's devicetree guide*](https://docs.zephyrproject.org/2.7.4/reference/devicetree/index.html).  However, let's briefly analyse the node definition for `led_0` to better understand the `blinky` example:

  ```dtd
  / {
  
  ...
  
  	aliases {
  		led0 = &led_0;
  	};
  
  ...
  
  	leds {
  		compatible = "gpio-leds";
  		led_0: led {
  			gpios = <&gpio_led0 0 GPIO_ACTIVE_HIGH>;
  			label = "Red LED";
  		};
  	};
  
  };
  
  ...
  
  &gpio_led0 {
  	status = "okay";
  };
  
  ...
  ```
  
  * Sets alias `led0`
  
  * Defines tha node is compatible with the *GPIO-LED driver*, a generic driver for LEDs controlled via GPIO pins. 
    * `&gpio_led0`: A reference to the *GPIO controller* (`gpio_led0`) that manages this pin.
  
    * `0`: the GPIO pin number to which the LED is connected.
  
    * `GPIO_ACTIVE_HIGH`: Indicates that the LED is *active-high*, meaning it turns ON when the GPIO pin is set to a high state (1).
  

**TASK:** Examine the DTS file carefully to gain a clear understanding of its structure and content.

## Drivers definition

The folder `driver/gpio/` contains the files required to define the GPIO driver. Below, we summarise the most relevant:

* `gpio_veerwolf.c`:  This file defines GPIO driver implementation for the `veerwolf_nexys` module. The file serves as a custom GPIO driver that interfaces with hardware GPIO registers. A detailed breakdown of its key components and significance is provided:

  * Set Bits:

    ```c
    static int gpio_veerwolf_port_set_bits_raw(const struct device *dev,
    					gpio_port_pins_t pins)
    {
    	mem_addr_t addr = DEV_GPIO_ADDR(dev);
    	uint32_t port_val;
    
    	port_val = sys_read32(addr) | pins;
    	sys_write32(port_val, addr);
    
    	return 0;
    }
    ```

  * Clear Bits:

    ```c
    static int gpio_veerwolf_port_clear_bits_raw(const struct device *dev,
    					  gpio_port_pins_t pins)
    {
    	mem_addr_t addr = DEV_GPIO_ADDR(dev);
    	uint32_t port_val;
    
    	port_val = sys_read32(addr) & ~pins;
    	sys_write32(port_val, addr);
    
    	return 0;
    }
    ```

  * Driver API registration:

    ```c
    static const struct gpio_driver_api gpio_veerwolf_driver_api = {
        .pin_configure = gpio_veerwolf_configure,
        .port_get_raw = gpio_veerwolf_port_get_raw,
        .port_set_masked_raw = gpio_veerwolf_port_set_masked_raw,
        .port_set_bits_raw = gpio_veerwolf_port_set_bits_raw,
        .port_clear_bits_raw = gpio_veerwolf_port_clear_bits_raw,
        .port_toggle_bits = gpio_veerwolf_port_toggle_bits,
        .pin_interrupt_configure = gpio_veerwolf_pin_interrupt_configure,
    };
    ```

**TASK:** Examine the driver code thoroughly to understand its functionality and design. Pay attention to the following aspects:

* Purpose: Identify the specific hardware or functionality the driver is designed to control or interface with.
* Initialization: Observe how the driver initializes and configures the hardware. Look for functions or routines related to setup.
* Core Functionality: Analyze the primary operations implemented by the driver.
* API Integration: Check how the driver interacts with higher-level software or external APIs. Look for functions or methods exposed for external use.
* Error Handling: Study how the driver handles errors or exceptions.

## Devicetree source

The folder `dts` contains the files required to handle the *DeviceTree* files. Below, we summarise the most relevant:

* ``bindings/gpio/veerwolf,gpio.yaml`: defines *DeviceTree bindings* for the custom GPIO controller. These bindings describe how hardware properties are represented in the DeviceTree source (DTS) files and how they map to drivers.

* `dts/riscv/riscv32-veer.dtsi`:  *DeviceTree Include (DTSI)* file that defines the hardware description specific to the veerwolf SoC.  Note that a `.dtsi` file is a reusable include file that can be shared across multiple boards or systems. It provides common definitions, such as peripherals, memory regions, and hardware properties that are relevant for a particular SoC.

  * Below is a breakdown for the GPIO component:

    ```dtd
    gpio0: gpio@40002000 {
        compatible = "veerwolf,gpio";
        reg = <0x40002000 0x100>; /* Base address and size of GPIO registers */
        ngpios = <32>;
        gpio-controller;
    };
    ```

**TASK:** Analyze the DTSI file carefully to understand its structure, purpose, and how it contributes to the device’s hardware configuration.

## SoC initialization code

The folder`soc/riscv/veerwolf/` contains the source files that handle low-level initialisation of the SoC, such as setting up the CPU clock**, **reset configuration, and enabling specific hardware blocks during the boot process.


## Exercise

Using as reference the [Introduction to Devicetree Guide](https://docs.zephyrproject.org/2.7.4/guides/dts/intro.html), create the directory `zephyr/samples/basic/blinky/boards` and add a devicetree overlay file named `veerwolf_nexys.overlay` to modify certain aspects of the board’s behavior (eg. changing the led, the behavior of writing `0`/`1`, etc.). Ensure that everything is functioning correctly by testing the modifications.

## Exercise (optional, not easy)

Modify the module to add support to read the switches of the `veerwolf_nexys` board. 

*Hints: it is required to change the devicetree and the driver.*

## Reference

* [Devicetree Guide](https://docs.zephyrproject.org/2.7.4/guides/dts/index.html#devicetree-guide): This is a high-level guide to devicetree as it is used for Zephyr development.

* [Devicetree](https://docs.zephyrproject.org/2.7.4/reference/devicetree/index.html): This is reference documentation for devicetree as it is used for Zephyr development. For a platform-independent specification, see the [Devicetree specification](https://www.devicetree.org/).

* [Board Porting Guide](https://docs.zephyrproject.org/2.7.4/guides/porting/board_porting.html?highlight=soc): This is howto guide for porting s new board to Zephyr and it is a good starting point to understand the `veerwolf` module.
