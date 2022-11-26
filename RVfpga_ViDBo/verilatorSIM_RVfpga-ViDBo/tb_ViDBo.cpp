// SPDX-License-Identifier: Apache-2.0
// Copyright 2021 Olof Kindgren
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
// http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#include <stdint.h>
#include <signal.h>

#include "vidbo.h"

#include "Vrvfpgasim.h"

using namespace std;

static bool done;

vluint64_t main_time = 0;

double sc_time_stamp () {
  return main_time;
}

void INThandler(int signal) {
  printf("\nCaught ctrl-c\n");
  done = true;
}


int main(int argc, char **argv, char **env) {
  vidbo_context_t vidbo_context;

  const char * const inputs[] = {
    "gpio.SW0",
    "gpio.SW1",
    "gpio.SW2",
    "gpio.SW3",
    "gpio.SW4",
    "gpio.SW5",
    "gpio.SW6",
    "gpio.SW7",
    "gpio.SW8",
    "gpio.SW9",
    "gpio.SW10",
    "gpio.SW11",
    "gpio.SW12",
    "gpio.SW13",
    "gpio.SW14",
    "gpio.SW15",
    "gpio.SW16",
    "gpio.SW17",
    "gpio.SW18",
    "gpio.SW19",
    "gpio.SW20",
  };
  int num_inputs = sizeof(inputs) / sizeof(inputs[0]);

  int *input_vals = (int *)calloc(num_inputs, sizeof(int));

  vidbo_init(&vidbo_context, 8081);

  vidbo_register_inputs(&vidbo_context, inputs, num_inputs);
  
  Verilated::commandArgs(argc, argv);

  Vrvfpgasim* top = new Vrvfpgasim;

  signal(SIGINT, INThandler);

  int check_vidbo = 0;

  printf("\nHELLO_TB\n");

  top->clk = 1;
  int last_leds = top->o_led;
  int new_SevSegDispl = 0;
  int last_SevSegDispl = 0;
  int new_Enables = 0;
  int sidx = 0;
  int SevSegDispl4;
  int Digit, Digit_Hex, CheckDigit=0;
  char item2[13] = {0}; //Space for SevSegDispl?\0

  while (!(done || Verilated::gotFinish())) {

    top->eval();

    check_vidbo++;

    char item[5] = {0}; //Space for LD??\0
    if (last_leds != top->o_led) {
        for (int i=0;i<16;i++) {
          snprintf(item, 5, "LD%d", i);
          vidbo_send(&vidbo_context, main_time, "gpio", item, (top->o_led>>i) & 0x1);
        }
        last_leds = top->o_led;
    }

    if (vidbo_recv(&vidbo_context, input_vals)) {
      /* Update the GPIO inputs from the received frame */
      top->i_sw = 0;
      for (int i=0;i<16;i++)
        if (input_vals[i])
          top->i_sw |= (1 << i);

      /* Update the GPIO2 inputs from the received frame */
      top->i_pb = 0;
      for (int i=0;i<5;i++)
        if (input_vals[i+16])
          top->i_pb |= (1 << i);
    }

    if (top->tf_push && top->clk==1) {
      vidbo_send(&vidbo_context, main_time, "serial", "uart", top->wb_m2s_uart_dat_output);
    }


    if (main_time % 10000 == 0) CheckDigit = 8;

    if ((CheckDigit > 0) && (top->clk == 0)) {
          CheckDigit = CheckDigit-1;

          if (CheckDigit == 7){
            new_SevSegDispl = 0;
            new_Enables = 0;
          }

          Digit = (top->CA<<6)+(top->CB<<5)+(top->CC<<4)+(top->CD<<3)+(top->CE<<2)+(top->CF<<1)+(top->CG);

          if (Digit == 0x01) Digit_Hex = 0;
          if (Digit == 0x4f) Digit_Hex = 1;
          if (Digit == 0x12) Digit_Hex = 2;
          if (Digit == 0x06) Digit_Hex = 3;
          if (Digit == 0x4c) Digit_Hex = 4;
          if (Digit == 0x24) Digit_Hex = 5;
          if (Digit == 0x20) Digit_Hex = 6;
          if (Digit == 0x0f) Digit_Hex = 7;
          if (Digit == 0x00) Digit_Hex = 8;
          if (Digit == 0x0c) Digit_Hex = 9;
          if (Digit == 0x08) Digit_Hex = 10;
          if (Digit == 0x60) Digit_Hex = 11;
          if (Digit == 0x72) Digit_Hex = 12;
          if (Digit == 0x42) Digit_Hex = 13;
          if (Digit == 0x30) Digit_Hex = 14;
          if (Digit == 0x38) Digit_Hex = 15;

          if (top->AN == 0xFE){
            new_SevSegDispl = new_SevSegDispl + (Digit_Hex);
            new_Enables = new_Enables + (1);
          }
          if (top->AN == 0xFD){
            new_SevSegDispl = new_SevSegDispl + (Digit_Hex<<4);
            new_Enables = new_Enables + (2);
          } 
          if (top->AN == 0xFB){
            new_SevSegDispl = new_SevSegDispl + (Digit_Hex<<8);
            new_Enables = new_Enables + (4);
          } 
          if (top->AN == 0xF7){
            new_SevSegDispl = new_SevSegDispl + (Digit_Hex<<12);
            new_Enables = new_Enables + (8);
          } 
          if (top->AN == 0xEF){
            new_SevSegDispl = new_SevSegDispl + (Digit_Hex<<16);
            new_Enables = new_Enables + (16);
          } 
          if (top->AN == 0xDF){
            new_SevSegDispl = new_SevSegDispl + (Digit_Hex<<20);
            new_Enables = new_Enables + (32);
          } 
          if (top->AN == 0xBF){
            new_SevSegDispl = new_SevSegDispl + (Digit_Hex<<24);
            new_Enables = new_Enables + (64);
          } 
          if (top->AN == 0x7F){
            new_SevSegDispl = new_SevSegDispl + (Digit_Hex<<28);
            new_Enables = new_Enables + (128);
          }
    }

    if ((last_SevSegDispl != new_SevSegDispl) && CheckDigit==0) {
        for (int i=0;i<8;i++) {
          if ((((new_Enables) >> i) & 1) == 0){
              SevSegDispl4 = 32;
          } 
          else{
              if((((new_SevSegDispl)>>(i*4)) & 0xF) < 10) SevSegDispl4 = (((new_SevSegDispl)>>(i*4)) & 0xF)+48;
              else SevSegDispl4 = (((new_SevSegDispl)>>(i*4)) & 0xF)+55;
          }
          snprintf(item2, 13, "SevSegDispl%d", i);
          vidbo_send(&vidbo_context, main_time, item2, "digit", SevSegDispl4);
        }
        last_SevSegDispl = new_SevSegDispl;
    }


    top->clk = !top->clk;
    main_time+=10;

  }


  exit(0);
}
