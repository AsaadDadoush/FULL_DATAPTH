from myhdl import *


@block
def extender(input_12or20, output32):
    @always_comb
    def ext():
        output32.next[32:] = input_12or20
    return ext

@block
def test_bench():
    input_12or20 = Signal(intbv(0)[12:])
    output32 = Signal(intbv(0)[32:])
    extend = extender(input_12or20, output32)

    @instance
    def monitor():
        yield delay(1)
        print("input_12or20 length: %s" % len(input_12or20))
        print("Output32 length:  %s" % (len(output32)))
    return instances()


def convert():
    input_12or20 = Signal(intbv(0)[20:])
    output32 = Signal(intbv(0)[32:])
    extend = extender(input_12or20, output32)
    extend.convert(hdl='Verilog')


test = test_bench()
test.run_sim()
convert()