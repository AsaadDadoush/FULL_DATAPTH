from myhdl import *
from random import randrange

@block
def barrel_shifter(load_value, load_input, shift_reg):

    @always_comb
    def shift_bit():
        load_value.next = load_input << shift_reg

    return shift_bit

@block
def test_bench():
    load_value = Signal(intbv(0)[32:])
    load_input = Signal(intbv(0)[32:])
    shift_reg = Signal(intbv(0)[2:])
    test_bench_shifter = barrel_shifter(load_value, load_input,shift_reg)

    @instance
    def monitor():
        for i in range(10):
            load_input.next = randrange(2 ** 12)
            shift_reg.next = 1
            yield delay(1)
            print("  %s  :    %s" % (load_input + 0, load_value + 0))
    return instances()


def convert():
    load_value = Signal(intbv(0)[32:])
    load_input = Signal(intbv(0)[32:])
    shift_reg = Signal(intbv(0)[2:])
    conv = barrel_shifter(load_value, load_input,shift_reg)
    conv.convert(hdl='Verilog')


convert()
tst = test_bench()
tst.run_sim(50)
