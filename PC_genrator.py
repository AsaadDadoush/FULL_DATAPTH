from myhdl import *


@block
def PC_gen(PC, rs1, imm, sel, out):
    @always_comb
    def gen():
        if sel == 0:
            out.next = PC + 4
        elif sel == 1:
            out.next = PC + imm
        else:
            out.next = rs1 + imm

    return gen


@block
def test():
    PC = Signal(intbv(0)[32:])
    imm = Signal(intbv(0)[32:])
    out = Signal(intbv(0)[32:])
    rs1 = Signal(intbv(0)[32:])
    sel = Signal(intbv(0)[2:])
    ins = PC_gen(PC, rs1, imm, sel, out)

    @instance
    def stimulus():
        rs1.next, PC.next, imm.next, sel.next = 60, 30, 10, 0
        yield delay(2)
        print("\nWhen Branch is not taken and not jalr instruction : ")
        print("sel | rs1 | PC | imm | Output")
        print("%s   | %s  | %s | %s  | %s" % (sel + 0, rs1+0, PC + 0, imm + 0, out + 0))
        print("\nWhen Branch is taken: ")
        rs1.next, PC.next, imm.next, sel.next = 60, 30, 10, 1
        yield delay(2)
        print("sel | rs1 | PC | imm | Output")
        print("%s   | %s  | %s | %s  | %s" % (sel + 0, rs1+0, PC + 0, imm + 0, out + 0))

        print("\nWhen instruction is Jump And Link Reg: ")
        rs1.next, PC.next, imm.next, sel.next = 60, 30, 10, 2
        yield delay(2)
        print("sel | rs1 | PC | imm | Output")
        print("%s   | %s  | %s | %s  | %s" % (sel + 0, rs1 + 0, PC + 0, imm + 0, out + 0))

    return instances()


def convert():
    PC = Signal(intbv(0)[32:])
    imm = Signal(intbv(0)[32:])
    out = Signal(intbv(0)[32:])
    rs1 = Signal(intbv(0)[32:])
    sel = Signal(intbv(0)[2:])
    test = PC_gen(PC, rs1, imm, sel, out)
    test.convert(hdl='Verilog')


tb = test()
tb.run_sim(500)
convert()

