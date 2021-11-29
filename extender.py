from myhdl import *


@block
def extender(immI, immS, immB, immU, immJ, imm32I, imm32S, imm32B, imm32U, imm32J):
    @always_comb
    def extend():
        imm32I.next = immI.signed()[32:]
        imm32S.next = immS.signed()[32:]
        imm32B.next = immB.signed()[32:]
        imm32U.next = immU.signed()[32:]
        imm32J.next = immJ.signed()[32:]
    return extend


@block
def test_bench():
    immU = Signal(intbv(0)[20:0])
    immJ = Signal(intbv(0)[20:0])
    immI = Signal(intbv(0)[12:0])
    immS = Signal(intbv(0)[12:0])
    immB = Signal(intbv(0)[12:0])
    imm32I = Signal(intbv(0)[32:0])
    imm32S = Signal(intbv(0)[32:0])
    imm32B = Signal(intbv(0)[32:0])
    imm32U = Signal(intbv(0)[32:0])
    imm32J = Signal(intbv(0)[32:0])
    ins = extender( immI, immS, immB, immU, immJ, imm32I, imm32S, imm32B, imm32U, imm32J)

    @instance
    def stimulus():
        immI.next = 0b010100010111  # U-AUIPC
        immS.next = 0b010100010111
        immB.next = 0b010100010111
        immU.next = 0b11111111111111110110
        immJ.next = 0b010100010111
        yield delay(2)

    @instance
    def monitor():
        yield delay(2)
        print("imm length: %s" % len(immI))
        print("imm :  %s" % bin(immI, 12))
        print("imm32 length: %s" % len(imm32I))
        print("imm32 :  %s" % bin(imm32I, 32))
        print("*************** I-type ***************\n")
        # *************************************************
        print("imm length: %s" % len(immS))
        print("imm :  %s" % bin(immS, 12))
        print("imm32 length: %s" % len(imm32S))
        print("imm32 :  %s" % bin(imm32S, 32))
        print("*************** S-type ***************\n")
        # *************************************************
        print("imm length: %s" % len(immB))
        print("imm :  %s" % bin(immB, 12))
        print("imm32 length: %s" % len(imm32B))
        print("imm32 :  %s" % bin(imm32B, 32))
        print("*************** B-type ***************\n")
        # *************************************************
        print("imm length: %s" % len(immU))
        print("imm :  %s" % bin(immU, 12))
        print("imm32 length: %s" % len(imm32U))
        print("imm32 :  %s" % bin(imm32U, 32))
        print("*************** U-type ***************\n")
        # *************************************************
        print("imm length: %s" % len(immJ))
        print("imm :  %s" % bin(immJ, 12))
        print("imm32 length: %s" % len(imm32J))
        print("imm32 :  %s" % bin(imm32J, 32))
        print("*************** J-type ***************\n")

    return instances()


def convert():
    immU = Signal(intbv(0)[20:0])
    immJ = Signal(intbv(0)[20:0])
    immI = Signal(intbv(0)[12:0])
    immS = Signal(intbv(0)[12:0])
    immB = Signal(intbv(0)[12:0])
    imm32I = Signal(intbv(0)[32:0])
    imm32S = Signal(intbv(0)[32:0])
    imm32B = Signal(intbv(0)[32:0])
    imm32U = Signal(intbv(0)[32:0])
    imm32J = Signal(intbv(0)[32:0])
    ins = extender( immI, immS, immB, immU, immJ, imm32I, imm32S, imm32B, imm32U, imm32J)
    ins.convert(hdl='Verilog')


# test = test_bench()
# test.run_sim()
# convert()
