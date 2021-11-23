from myhdl import *


@block
def ins_dec(pass_bits, opcode, rd, func3, rs1, rs2, func7, imm12, imm20):

    @always_comb
    def decoder():
        opcode.next = pass_bits[7:0]  # opcode
        func3.next = pass_bits[15:12]  # func3
        func7.next = pass_bits[32:25]  # func7
        # R-type
        if pass_bits[7:0] == 0b0110011:
            rd.next = pass_bits[12:7]  # rd
            rs1.next = pass_bits[20:15]  # rs1
            rs2.next = pass_bits[25:20]  # rs2
            imm12.next = 0
            imm20.next = 0
            # I-type
        elif pass_bits[7:0] == 0b0010011:
            rs2.next = 0
            rd.next = pass_bits[12:7]  # rd
            rs1.next = pass_bits[20:15]  # rs1
            imm12.next = pass_bits[32:20]  # imm
            imm20.next = 0
            # ========I(LOAD)==========================I(JALR)===================I(sys calls)
        elif pass_bits[7:0] == 0b0000011 or pass_bits[7:0] == 0b1100111 or pass_bits[7:0] == 0b1110011:
            rd.next = pass_bits[12:7]  # rd
            rs1.next = pass_bits[20:15]  # rs1
            imm12.next = pass_bits[32:20]  # imm
            rs2.next = 0
            imm20.next = 0
            # S-Type
        elif pass_bits[7:0] == 0b0100011:
            rd.next = 0
            rs1.next = pass_bits[20:15]  # rs1
            rs2.next = pass_bits[25:20]  # rs2
            imm12.next = intbv(concat(pass_bits[32:25], pass_bits[12:7]))
            imm20.next = 0
            # B-type
        elif pass_bits[7:0] == 0b1100011:
            rd.next = 0
            imm20.next = 0
            rs1.next = pass_bits[20:15]  # rs1
            rs2.next = pass_bits[25:20]  # rs2
            imm12.next = intbv(concat(pass_bits[32:31], pass_bits[8:7], pass_bits[31:25], pass_bits[12:8]))
            # ====== U-Type(Load Up) ==========U-Type(AUIPC)
        elif pass_bits[7:0] == 0b0110111 or pass_bits[7:0] == 0b0010111:
            rd.next = pass_bits[12:7]  # rd
            rs1.next = 0
            rs2.next = 0
            imm12.next = 0
            imm20.next = intbv(pass_bits[32:12])  # imm
            # J-Type
        else:
            rs1.next = 0
            rs2.next = 0
            imm12.next = 0
            rd.next = pass_bits[12:7]  # rd
            imm20.next = intbv(concat(pass_bits[31], pass_bits[20:12], pass_bits[20], pass_bits[31:21]))

    return decoder


@block
def Test():
    pass_bits = Signal(intbv(0)[32:0])
    opcode = Signal(intbv(0)[7:0])
    rd = Signal(intbv(0)[5:0])
    func3 = Signal(intbv(0)[3:0])
    rs1 = Signal(intbv(0)[5:0])
    rs2 = Signal(intbv(0)[5:0])
    func7 = Signal(intbv(0)[7:0])
    imm20 = Signal(intbv(0)[20:0])
    imm12 = Signal(intbv(0)[12:0])
    ins = ins_dec(pass_bits, opcode, rd, func3, rs1, rs2, func7, imm12, imm20)

    @instance
    def stimulus():
        pass_bits.next = 0b00000000000000000010010100010111  # U-AUIPC
        yield delay(2)
        pass_bits.next = 0b00000000101100000000001010110011  # R-type
        yield delay(2)
        pass_bits.next = 0b11111111111100101000001010010011  # I-Type
        yield delay(2)
        pass_bits.next = 0b00000000000000101010001110000011  # I(load)
        yield delay(2)
        pass_bits.next = 0b00000000000000001000000001100111  # I(JALR)
        yield delay(2)
        pass_bits.next = 0b00000000000000000000000001110011  # I(sys)
        yield delay(2)
        pass_bits.next = 0b00000000000001010010000000100011  # S-type
        yield delay(2)
        pass_bits.next = 0b11111110000000101001101011100011  # B-Type
        yield delay(2)
        pass_bits.next = 0b00000100100000000000000001101111  # J-type

    @instance
    def monitor():
        yield delay(2)
        print("%s" % (bin(pass_bits, 32)))
        print("%s%s%s" % (bin(imm20, 20), bin(rd, 5), bin(opcode, 7)))
        yield delay(2)
        print()
        print("%s" % (bin(pass_bits, 32)))
        print("%s%s%s%s%s%s" % (bin(func7, 7), bin(rs2, 5), bin(rs1, 5), bin(func3, 3), bin(rd, 5), bin(opcode, 7)))
        yield delay(2)
        print()
        print("%s" % (bin(pass_bits, 32)))
        print("%s%s%s%s%s" % (bin(imm12, 12), bin(rs1, 5), bin(func3, 3), bin(rd, 5), bin(opcode, 7)))
        yield delay(2)
        print()
        print("%s" % (bin(pass_bits, 32)))
        print("%s%s%s%s%s" % (bin(imm12, 12), bin(rs1, 5), bin(func3, 3), bin(rd, 5), bin(opcode, 7)))
        yield delay(2)
        print()
        print("%s" % (bin(pass_bits, 32)))
        print("%s%s%s%s%s" % (bin(imm12, 12), bin(rs1, 5), bin(func3, 3), bin(rd, 5), bin(opcode, 7)))
        yield delay(2)
        print()
        print("%s" % (bin(pass_bits, 32)))
        print("%s%s%s%s%s" % (bin(imm12, 12), bin(rs1, 5), bin(func3, 3), bin(rd, 5), bin(opcode, 7)))
        yield delay(2)
        print()
        print("%s" % (bin(pass_bits, 32)))
        print("%s%s%s%s%s%s" % (bin(imm12[12:5], 7), bin(rs2, 5), bin(rs1, 5), bin(func3, 3), bin(imm12[5:0], 5),
                                bin(opcode, 7)))
        yield delay(2)
        print()
        print("%s" % (bin(pass_bits, 32)))
        print("%s" % (bin(imm12, 12)))
        yield delay(2)
        print()
        print("%s" % (bin(pass_bits, 32)))
        print("%s" % (bin(imm20, 20)))
        yield delay(2)

    return instances()


def convert():
    pass_bits = Signal(intbv(0)[32:0])
    opcode = Signal(intbv(0)[7:0])
    rd = Signal(intbv(0)[5:0])
    func3 = Signal(intbv(0)[3:0])
    rs1 = Signal(intbv(0)[5:0])
    rs2 = Signal(intbv(0)[5:0])
    func7 = Signal(intbv(0)[7:0])
    imm20 = Signal(intbv(0)[20:0])
    imm12 = Signal(intbv(0)[12:0])
    ins = ins_dec(pass_bits, opcode, rd, func3, rs1, rs2, func7, imm12, imm20)
    ins.convert(hdl='Verilog')


convert()
tb = Test()
tb.run_sim(100)
