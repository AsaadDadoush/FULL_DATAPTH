import random
from myhdl import *

random.seed()
randrange = random.randrange


@block
def mux2_1(sel, out, i0, i1):
    @always(i0,i1,sel)
    def mux():
        if sel == 0:
            out.next = i0
        else:
            out.next = i1
        print("================== PC or Rs1 mux (input a for ALU) ==================")
        print("input i0: ", i0 + 0)
        print("input i1: ", i1 + 0)
        print("Selection: ", sel + 0)
        print("Output: ", out.next + 0)
        print("")
    return mux


@block
def mux2_1_pcANDalu(sel, out, i0, i1):
    @always(i0, i1, sel)
    def mux():
        if sel == 0:
            out.next = int(i0/4)
        else:
            out.next = int(i1/4)
        print("======================== PC and Address mux =========================")
        print("input i0: ", i0+0)
        print("input i1: ", i1 + 0)
        print("Selection: ",sel+0)
        print("Out from  PC and Address mux: ", out.next+0)
        print("")

    return mux


@block
def testbench():
    sel = Signal(bool(0))
    i0 = Signal(intbv(0)[32:])
    i1 = Signal(intbv(0)[32:])
    out = Signal(intbv(0)[32:])
    mux = mux2_1(sel, out, i0, i1)

    @instance
    def stimulus():
        print("               i0                |              i1                  | sel  | output")
        for i in range(20):
            i0.next, i1.next, sel.next = randrange(32), randrange(32), randrange(2)
            yield delay(10)
            print(" %s | %s  |  %s  | %s" % (bin(i0, 32), bin(i1, 32), bin(sel, 1), bin(out, 32)))

    return instances()

def convert():
    sel = Signal(bool(0))
    i0 = Signal(intbv(0)[32:])
    i1 = Signal(intbv(0)[32:])
    out = Signal(intbv(0)[32:])
    mux = mux2_1(sel, out, i0, i1)
    mux.convert(hdl='Verilog')


# convert()
# tst = testbench()
# tst.run_sim()