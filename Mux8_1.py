from myhdl import *
from random import randrange


@block
def mux8_1(i0, i1, i2, i3, i4, out, sel):
    @always(i0, i1, i2, i3, i4, sel)
    def mux():
        if sel == 0:
            out.next = i0
        elif sel == 1:
            out.next = i1
        elif sel == 2:
            out.next = i2
        elif sel == 3:
            out.next = i3
        elif sel == 4:
            out.next = i4
        elif sel == 5:
            out.next = i4
        elif sel == 6:
            out.next = i4
        else:
            out.next = i4
        print("============================== imm mux ==============================")
        print("input i0: ", i0 + 0)
        print("input i1: ", i1 + 0)
        print("input i2: ", i2 + 0)
        print("input i3: ", i3 + 0)
        print("input i4: ", i4 + 0)
        print("Selection: ", sel + 0)
        print("Output: ", out.next + 0)
        print("")
    return mux


@block
def testbench():
    i0 = Signal(intbv(0)[32:])
    i1 = Signal(intbv(0)[32:])
    i2 = Signal(intbv(0)[32:])
    i3 = Signal(intbv(0)[32:])
    i4 = Signal(intbv(0)[32:])
    sel = Signal(intbv(0)[3:])
    out = Signal(intbv(0)[32:])
    ins = mux8_1(i0, i1, i2, i3, i4, out, sel)

    @instance
    def monitor():
        print("               i0               |              i1                 |               i2               |    "
              "           i3              |               i4               |               rs2               "
              "   | sel  | output")
        for i in range(6):
            i0.next, i1.next, i2.next, i3.next, i4.next, sel.next = randrange(32), randrange(32), randrange(32) \
                , randrange(32), randrange(32), i
            yield delay(10)
            print(" %s | %s  |  %s  | %s | %s | %s | %s | " % (
                bin(i0, 32), bin(i1, 32), bin(i2, 32), bin(i3, 32), bin(i4, 32), bin(sel, 2), bin(out, 32)))
    return instances()

def convert():
    i0 = Signal(intbv(0)[32:])
    i1 = Signal(intbv(0)[32:])
    i2 = Signal(intbv(0)[32:])
    i3 = Signal(intbv(0)[32:])
    i4 = Signal(intbv(0)[32:])
    sel = Signal(intbv(0)[3:])
    out = Signal(intbv(0)[32:])
    ins = mux8_1(i0, i1, i2, i3, i4, out, sel)
    ins.convert(hdl='Verilog')

#
# tst = testbench()
# tst.run_sim()
# convert()
#


