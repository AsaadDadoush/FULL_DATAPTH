from myhdl import *


@block
def andG(in1, in2, out):
    @always_comb
    def andG():
        out.next = in1 & in2

    return andG


@block
def test():
    in1 = Signal(intbv(0)[32:])
    in2 = Signal(intbv(0)[32:])
    out = Signal(bool(0))
    ins = andG(in1, in2, out)

    @instance
    def stimulus():
        yield delay(2)
        in1.next = 0b00000000000000000010010100010111
        yield delay(2)
        in2.next = 0b00000000101100000000001010110011
        yield delay(2)
        print(bin(out.next, 32))

    return instances()


def convert():
    in1 = Signal(intbv(0)[32:])
    in2 = Signal(intbv(0)[32:])
    out = Signal(bool(0))
    tst = andG(in1, in2, out)
    tst.convert(hdl='Verilog')


convert()
tb = test()
tb.run_sim(500)
