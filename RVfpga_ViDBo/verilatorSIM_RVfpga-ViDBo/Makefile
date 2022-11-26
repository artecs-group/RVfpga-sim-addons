TOP_MODULE = rvfpgasim

VC_FILE = swervolf_0.7_ViDBo.vc
VERILATOR_OPTIONS = -Wno-fatal

#Assume a local installation if VERILATOR_ROOT is set
ifeq ($(VERILATOR_ROOT),)
VERILATOR ?= verilator
else
VERILATOR ?= $(VERILATOR_ROOT)/bin/verilator
endif

# Make sim
V$(TOP_MODULE): V$(TOP_MODULE).mk
	$(MAKE) $(MAKE_OPTIONS) -f $<
	
# Generate makefile
V$(TOP_MODULE).mk:
	$(VERILATOR) -f $(VC_FILE) $(VERILATOR_OPTIONS)

.PHONY : clean
clean :
	-rm V$(TOP_MODULE)*
	-rm *.o
	-rm *.d