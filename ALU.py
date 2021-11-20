import random
from myhdl import *


@block
def alu(a, b, sel, out):
    @always_comb
    def alu():
        # ADD
        if sel == 0:
            out.next = a + b
        # MULTIPLY
        elif sel == 1:
            out.next = a * b
        # DIVISION
        elif sel == 2:
            out.next = a // b
        # AND
        elif sel == 3:
            out.next = a & b
        # OR
        elif sel == 4:
            out.next = a | b
        elif sel == 5:
            out.next = a ^ b
        # Shift left
        elif sel == 6:
            out.next = a << b
        # Shift right
        elif sel == 7:
            out.next = a >> b
        # Branch ==
        elif sel == 8:
            if a == b:
                out.next = 1
            else:
                out.next = 0
        # Branch !=
        elif sel == 9:
            if a != b:
                out.next = 1
            else:
                out.next = 0
        # Branch <
        elif sel == 10:
            if a < b:
                out.next = 1
            else:
                out.next = 0
        # Branch <=
        elif sel == 11:
            if a <= b:
                out.next = 1
            else:
                out.next = 0

    return alu


@block
def testbench():
    sel = Signal(intbv(0)[4:])
    a = Signal(intbv(0)[32:])
    b = Signal(intbv(0)[32:])
    out = Signal(intbv(0)[32:])
    ins = alu(a, b, sel, out)
    operation = ""

    @instance
    def stimulus():
        print("A   OP  B  = Out | selection")
        for i in range(12):
                a.next, b.next, sel.next = intbv(20), intbv(15), i
                yield delay(5)
                yield delay(1)
                operation = ""
                if sel == 0:
                    operation = "Add"
                elif sel == 1:
                    operation = "MUL"
                elif sel == 2:
                    operation = "DIV"
                elif sel == 3:
                    operation = "AND"
                elif sel == 4:
                    operation = "OR"
                elif sel == 5:
                    operation = "XOR"
                elif sel == 6:
                    operation = "<<"
                elif sel == 7:
                    operation = ">>"
                elif sel == 8:
                    operation = "=="
                elif sel == 9:
                    operation = "=!"
                elif sel == 10:
                    operation = "<"
                elif sel == 11:
                    operation = "<="
                yield delay(1)
                print("%s %s %s = %s " % (a + 0, operation, b + 0, out + 0))

    return instances()


def convert():
    sel = Signal(intbv(0)[4:])
    a = Signal(intbv(0)[32:])
    b = Signal(intbv(0)[32:])
    out = Signal(intbv(0)[32:0])
    ins = alu(a, b, sel, out)
    ins.convert(hdl='Verilog')


tb = testbench()
tb.run_sim()
convert()

