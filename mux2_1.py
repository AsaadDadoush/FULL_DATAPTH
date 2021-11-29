import random
from myhdl import *

random.seed()
randrange = random.randrange


@block
def mux2_1(sel, out, imm, rs2):
    @always_comb
    def mux():
        if sel == 0:
            out.next = rs2
        else:
            out.next = imm

    return mux

@block
def testbench():
    sel = Signal(bool(0))
    imm = Signal(intbv(0)[32:])
    rs2 = Signal(intbv(0)[32:])
    out = Signal(intbv(0)[32:])
    mux = mux2_1(sel, out, imm, rs2)

    @instance
    def stimulus():
        print("               imm                |              rs2                  | sel  | output")
        for i in range(20):
            imm.next, rs2.next, sel.next = randrange(32), randrange(32), randrange(2)
            yield delay(10)
            print(" %s | %s  |  %s  | %s" % (bin(imm, 32), bin(rs2, 32), bin(sel, 1), bin(out, 32)))

    return instances()

def convert():
    sel = Signal(bool(0))
    imm = Signal(intbv(0)[32:])
    rs2 = Signal(intbv(0)[32:])
    out = Signal(intbv(0)[32:])
    mux = mux2_1(sel, out, imm, rs2)
    mux.convert(hdl='Verilog')


convert()
tst = testbench()
tst.run_sim()
