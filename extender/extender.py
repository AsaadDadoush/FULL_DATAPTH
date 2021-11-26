from myhdl import *


@block
def extender(sel, immI, immS, immB, immU, immJ, imm32):
    @always_comb
    def extender():
        imm32.next = 0
        if sel == 0:
            imm32.next[32:] = intbv(immI[12:0]).signed()  # singed immI
        elif sel == 1:
            imm32.next[32:] = intbv(immI[12:0])  # unsinged immI
        elif sel == 2:
            imm32.next[32:] = intbv(immS[12:0]).signed()  # singed immS
        elif sel == 3:
            imm32.next[32:] = intbv(immB[12:0]).signed() << 1  # immB shift by 2
        elif sel == 4:
            imm32.next[32:] = intbv(immB[12:0]) << 1  # immB shift by 2 Unsigned
        elif sel == 5:
            imm32.next[32:] = intbv(immU[20:0]).signed() << 12  # immU shift by 12
        elif sel == 6:
            imm32.next[32:] = intbv(immJ[20:0]).signed()  # immJ

    return extender


@block
def test_bench():
    sel = Signal(intbv(0)[3:0])
    immU = Signal(intbv(0)[20:0])
    immJ = Signal(intbv(0)[20:0])
    immI = Signal(intbv(0)[12:0])
    immS = Signal(intbv(0)[12:0])
    immB = Signal(intbv(0)[12:0])
    imm32 = Signal(intbv(0)[32:0])
    ins = extender(sel, immI, immS, immB, immU, immJ, imm32)

    @instance
    def stimulus():
        immI.next = 0b010100010111  # U-AUIPC
        yield delay(2)
        yield delay(2)

    @instance
    def monitor():
        yield delay(2)
        print("imm length: %s" % len(immI))
        print("imm :  %s" % bin(immI, 12))
        print("imm32 length: %s" % len(imm32))
        print("imm32 :  %s" % bin(imm32, 32))

    return instances()


def convert():
    sel = Signal(intbv(0)[3:0])
    immU = Signal(intbv(0)[20:0])
    immJ = Signal(intbv(0)[20:0])
    immI = Signal(intbv(0)[12:0])
    immS = Signal(intbv(0)[12:0])
    immB = Signal(intbv(0)[12:0])
    imm32 = Signal(intbv(0)[32:0])
    ins = extender(sel, immI, immS, immB, immU, immJ, imm32)
    ins.convert(hdl='Verilog')


test = test_bench()
test.run_sim()
convert()
