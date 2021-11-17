from myhdl import *


@block
def andG(in1, in2, out):
    @always_comb
    def andG():
        out.next = in1 & in2

    return andG


@block
def test():
    in1 = Signal(bool(0))
    in2 = Signal(bool(0))
    out = Signal(bool(0))
    ins = andG(in1, in2, out)

    @instance
    def stimulus():
        yield delay(2)
        in1.next = 0b1
        yield delay(2)
        in2.next = 0b1
        yield delay(2)
        print(bin(out.next))

    return instances()


def convert():
    in1 = Signal(bool(0))
    in2 = Signal(bool(0))
    out = Signal(bool(0))
    tst = andG(in1, in2, out)
    tst.convert(hdl='Verilog')


convert()
tb = test()
tb.run_sim(500)
