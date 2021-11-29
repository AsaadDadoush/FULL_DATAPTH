import random
from myhdl import *

random.seed()
randrange = random.randrange

@block
def mux_3to1(i0, i1, i2, sel, out):

    @always(i0, i1, i2, sel)
    def mux3to1():
        if sel == 0:
            out.next = i0
        elif sel == 1:
            out.next = i1
        elif sel == 2:
            out.next = i2
        else:
            out.next = i2

    return mux3to1


@block
def tb():
    i0 = Signal(intbv(0)[32:])
    i1 = Signal(intbv(0)[32:])
    i2 = Signal(intbv(0)[32:])
    sel = Signal(intbv(0)[2:])
    out = Signal(intbv(0)[32:])
    mux = mux_3to1(i0, i1, i2, sel, out)

    @instance
    def stimulus():
        print("               imm                |              rs2                  |               rs2               "
              "   | sel  | output")
        for i in range(20):
            i0.next, i1.next, i2.next, sel.next = randrange(32), randrange(32), randrange(32), randrange(4)
            yield delay(10)
            print(" %s | %s  |  %s  | %s | %s" % (bin(i0, 32), bin(i1, 32), bin(i2,32), bin(sel, 2), bin(out, 32)))

    return instances()


def convert():
    i0 = Signal(intbv(0)[32:])
    i1 = Signal(intbv(0)[32:])
    i2 = Signal(intbv(0)[32:])
    sel = Signal(intbv(0)[2:])
    out = Signal(intbv(0)[32:])
    mux = mux_3to1(i0, i1, i2, sel, out)
    mux.convert(hdl='Verilog')


convert()
tst = tb()
tst.run_sim()
