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
        print("=========== Rs2 or imm or Costant 4 mux (input b for ALU) ===========")
        print("input i0: ", i0 + 0)
        print("input i1: ", i1 + 0)
        print("input i2: ", i2 + 0)
        print("Selection: ", sel + 0)
        print("Output: ", out.next + 0)
        print("")

    return mux3to1

@block
def mux_3to1_for_Register(i0, i1, i2, sel, out):
    @always(sel)
    def mux3to1():
        if sel == 0:
            out.next = i0
        elif sel == 1:
            out.next = i1
        elif sel == 2:
            out.next = i2
        else:
            out.next = i2
        print("============== ALU result or Load Value or imm<<12 mux ==============")
        print("input i0: ", i0 + 0)
        print("input i1: ", i1 + 0)
        print("input i2: ", i2 + 0)
        print("Selection: ", sel + 0)
        print("Output: ", out.next + 0)
        print("")

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
            print(" %s | %s  |  %s  | %s | %s" % (bin(i0, 32), bin(i1, 32), bin(i2, 32), bin(sel, 2), bin(out, 32)))

    return instances()


def convert():
    i0 = Signal(intbv(0)[32:])
    i1 = Signal(intbv(0)[32:])
    i2 = Signal(intbv(0)[32:])
    sel = Signal(intbv(0)[2:])
    out = Signal(intbv(0)[32:])
    mux = mux_3to1(i0, i1, i2, sel, out)
    mux.convert(hdl='Verilog')


# convert()
# tst = tb()
# tst.run_sim()
