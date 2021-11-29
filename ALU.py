import random
from myhdl import *


@block
def alu(a, b, sel, out):
    @always_comb
    def alu():
        # ADD
        if sel == 0:
            out.next = a.signed() + b.signed()
        # MULTIPLY
        elif sel == 1:
            out.next = a.signed() * b.signed()
        # DIVISION
        elif sel == 2:
            out.next = a.signed() // b.signed()
        # AND
        elif sel == 3:
            out.next = a.signed() & b.signed()
        # OR
        elif sel == 4:
            out.next = a.signed() | b.signed()
        # XOR
        elif sel == 5:
            out.next = a.signed() ^ b.signed()
        # Shift left
        elif sel == 6:
            out.next = a.signed() << b[5:].signed()
        # Shift right
        elif sel == 7:
            out.next = a.signed() >> b[5:].signed()
        # Branch ==
        elif sel == 8:
            if a.signed() == b.signed():
                out.next = 1
            else:
                out.next = 0
        # Branch !=
        elif sel == 9:
            if a.signed() != b.signed():
                out.next = 1
            else:
                out.next = 0
        # Branch < & Set less than
        elif sel == 10:
            if a.signed() < b.signed():
                out.next = 1
            else:
                out.next = 0
        # Branch < (U) & Set less than (U)
        elif sel == 11:
            if a.signed() < b[32:]:
                out.next = 1
            else:
                out.next = 0
        # Branch <=
        elif sel == 12:
            if a.signed() <= b.signed():
                out.next = 1
            else:
                out.next = 0
        # Shift right Arith
        elif sel == 13:
            out.next = a.signed() >> b[5:].signed()

        # Branch >= (U)
        elif sel == 14:
            if a.signed() > b[32:]:
                out.next = 1
            else:
                out.next = 0
        # DIV (U)
        elif sel == 15:
            out.next = a.signed() // b[32:]
        # Remainder
        elif sel == 16:
            out.next = a.signed() % b.signed()
        # Remainder (U)
        else:
            out.next = a.signed() % b[32:]

    return alu


@block
def testbench():
    sel = Signal(intbv(0)[5:])
    a = Signal(intbv(0)[32:])
    b = Signal(intbv(0)[32:])
    out = Signal(intbv(0)[32:])
    ins = alu(a, b, sel, out)
    operation = ""

    @instance
    def stimulus():
        print("A   OP  B  = Out | selection")
        for i in range(17):
            a.next, b.next, sel.next = 20, 2, i
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
                operation = "< (U)"
            elif sel == 12:
                operation = "<="
            elif sel == 13:
                operation = ">> imm[4:0] Arith"
            elif sel == 14:
                operation = "< (U)"
            elif sel == 15:
                operation = ">= (U)"
            else:
                operation = "%"
            yield delay(1)
            print("%s %s %s = %s " % (a + 0, operation, b + 0, out + 0))

    return instances()


def convert():
    sel = Signal(intbv(0)[5:])
    a = Signal(intbv(0)[32:])
    b = Signal(intbv(0)[32:])
    out = Signal(intbv(0)[32:0])
    ins = alu(a, b, sel, out)
    ins.convert(hdl='Verilog')


tb = testbench()
tb.run_sim()
convert()