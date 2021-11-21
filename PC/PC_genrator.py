from myhdl import *


@block
def PC_gen(PC, imm, sel, out):
    @always_comb
    def gen():
        if sel == 0:
            out.next = PC + 4
        else:
            out.next = PC + imm

    return gen


@block
def test():
    PC = Signal(intbv(0)[32:])
    imm = Signal(intbv(0)[32:])
    out = Signal(intbv(0)[32:])
    sel = Signal(bool(0))
    ins = PC_gen(PC, imm, sel, out)

    @instance
    def stimulus():
        PC.next, imm.next, sel.next = 60, 30, 0
        yield delay(2)
        print("When Branch is not taken: ")
        print("sel | PC | imm | Output")
        print("%s   | %s | %s  | %s" % (sel + 0, PC + 0, imm + 0, out + 0))
        print("\nWhen Branch is taken: ")
        PC.next, imm.next, sel.next = 60, 30, 1
        yield delay(2)
        print("sel | PC | imm | Output")
        print("%s   | %s | %s  | %s" % (sel + 0, PC + 0, imm + 0, out + 0))

    return instances()


def convert():
    PC = Signal(intbv(0)[32:])
    imm = Signal(intbv(0)[32:])
    out = Signal(intbv(0)[32:])
    sel = Signal(bool(0))
    test = PC_gen(PC, imm, sel, out)
    test.convert(hdl='Verilog')


tb = test()
tb.run_sim(500)
convert()