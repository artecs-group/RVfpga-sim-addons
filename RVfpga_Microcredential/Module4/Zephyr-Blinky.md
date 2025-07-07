# Zephyr Blinky Sample

## Overview

Blinky is a simple application which blinks an LED forever using the [GPIO API](https://docs.zephyrproject.org/apidoc/2.7.4/group__gpio__interface.html). The source code shows how to configure GPIO pins as outputs, then turn them on and off.

## Requirements

You will see this error if you try to build Blinky for an unsupported board:

```
Unsupported board: led0 devicetree alias is not defined
```

The board must have an LED connected via a GPIO pin. These are called "User LEDs" on many of Zephyr's boards. The LED must be configured using the `led0` *devicetree* alias. This is usually done in the *devicetree* file `<BOARD>.dts` or in an *overlay* file `<BOARD>.overlay`. 

**TASK:** See the [*Zephyr's devicetree guide introduction*](https://docs.zephyrproject.org/2.7.4/guides/dts/intro.html) for a conceptual overview of *devicetree* and how Zephyr uses it.

## Building and running on `veerwolf_nexys`

### Building `.elf`

The program can be compiled in the same way as other Zephyr examples:

```sh
cd $WORKSPACE
west build -p always -b veerwolf_nexys zephyr/samples/basic/blinky
```

### Program FPGA

Since we are using an FPGA, the first step is to program it by loading the appropriate bitstream. Note that `BITFILE_DIR` must be an absolute path.

```sh
openocd -c "set BITFILE $BITFILE_DIR/swervolf_0.7.4_nexys_eh1.bit" \
-f $VEERWOLF_ROOT/data/veerwolf_nexys_program.cfg
```

### Load & run Blinky on `veerwolf_nexys`

Then just load the program to the main memory using `openocd`. 

```sh
export BUILD_DIR=$WORKSPACE/build
```

```sh
openocd -f $VEERWOLF_ROOT/data/veerwolf_nexys_debug.cfg \
-c "reset halt" \
-c "load_image $BUILD_DIR/zephyr/zephyr.elf 0x0 elf" \
-c "resume 0x0" -c shutdown
```

You should see LED0 on the Nexys board blinking.

## Analyzing the Blinky code

The Blinky directory contains the following files:

* `CMakeLists.txt`: CMake configuration file; it provides instructions for configuring and building the example.
* `sample.yaml`: Test definition YAML file.
* `src/main.c`: Application C program code.
* `prj.conf`: Zephyr’s project configuration file defines the *Kconfig options* for the current project and allows configuring the drivers, libraries, and other subsystems to tailor the build to the application’s requirements; in this case, it simply enables the GPIO driver.

  ```
  CONFIG_GPIO=y
  ```

**TASK:** Look carefully at the different files.

### Dissecting `main.c`

Below, we will outline the most relevant aspects of the code; please refer to the original file for more details.

* This macro retrieves the node corresponding to alias `ledo0` in the board’s *devicetree* source file (i.e. `veerwolf_nexys.dts`) :
  ```c
  #define LED0_NODE DT_ALIAS(led0)
  ```
* The following set of macros check wether the device node is enabled and retrieves it correspondinf information from the *devicetree*:
  
  ```c
  #if DT_NODE_HAS_STATUS(LED0_NODE, okay)
  #define LED0	DT_GPIO_LABEL(LED0_NODE, gpios)
  #define PIN	DT_GPIO_PIN(LED0_NODE, gpios)
  #define FLAGS	DT_GPIO_FLAGS(LED0_NODE, gpios)
  #else
  #error "Unsupported board: led0 devicetree alias is not defined"
  #define LED0	""
  #define PIN	0
  #define FLAGS	0
  #endif
  ```
  
* Retrieve the device structure for a driver by name (see [API reference](https://docs.zephyrproject.org/apidoc/2.7.4/group__device__model.html#ga34899198834c2e592a2e312fa94682ab)):

  ```c
  	dev = device_get_binding(LED0);
  	if (dev == NULL) {
  		return;
  	}
  ```
  
* Configure a single pin `PIN `as output with the corresponding default flags (see [API reference](https://docs.zephyrproject.org/apidoc/2.7.4/group__gpio__interface.html#gaed4a2051d76db7eead8ed1719ce2ba33)):
  

  ```c
  ret = gpio_pin_configure(dev, PIN, GPIO_OUTPUT_ACTIVE | FLAGS);
  if (ret < 0) {
  	return;
  }
  ```
  
* Main loop set `PIN` to `led_is_on` value (see [API reference](https://docs.zephyrproject.org/apidoc/2.7.4/group__gpio__interface.html#gabfab69282fb99be119760436f2d18a9b)), toggle its value and than sleep `SLEEP_TIME_MS` milliseconds (see [API reference](https://docs.zephyrproject.org/apidoc/2.7.4/group__thread__apis.html#ga51307cdfe153ab3e918b18755d97c5d9)):
  ```c
  while (1) {
  	gpio_pin_set(dev, PIN, (int)led_is_on);
  	led_is_on = !led_is_on;
  	k_msleep(SLEEP_TIME_MS);
  }
  ```
  Note that  `gpio_pin_set` is internally using `port_set_bits_raw` and `port_clear_bits_raw` via the driver, and hence `PIN` should be considered a set of pins.

**TASK:** Read the code carefully and review the API documentation to fully understand its functionality.

## Exercise

Make the LEDs turn on/off at fixed intervals, sequentially from 0 to 15 and then from 15 to 0.
