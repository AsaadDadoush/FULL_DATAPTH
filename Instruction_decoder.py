from myhdl import *


@block
def ins_dec(data_in, opcode, rd, func3, rs1, rs2, func7, immI, immS, immB, immU, immJ):

    @always_comb
    def decoder():
        opcode.next = data_in[7:0]  # opcode
        func3.next = data_in[15:12]  # func3
        func7.next = data_in[32:25]  # func7
        rd.next = data_in[12:7]  # rd
        rs1.next = data_in[20:15]  # rs1
        rs2.next = data_in[25:20]  # rs2

        # I-type
        immI.next = intbv(data_in[32:20])

        # S-type
        immS.next = intbv(concat(data_in[32:25], data_in[12:7]))

        # B-type
        immB.next = intbv(concat(data_in[32:31], data_in[8:7], data_in[31:25], data_in[12:8]))

        # U-type
        immU.next = intbv(data_in[32:12])

        # J-Type
        immJ.next = intbv(concat(data_in[31], data_in[20:12], data_in[20], data_in[31:21]))

    return decoder


@block
def Test():
    data_in = Signal(intbv(0)[32:0])
    opcode = Signal(intbv(0)[7:0])
    rd = Signal(intbv(0)[5:0])
    func3 = Signal(intbv(0)[3:0])
    rs1 = Signal(intbv(0)[5:0])
    rs2 = Signal(intbv(0)[5:0])
    func7 = Signal(intbv(0)[7:0])
    immU = Signal(intbv(0)[20:0])
    immJ = Signal(intbv(0)[20:0])
    immI = Signal(intbv(0)[12:0])
    immS = Signal(intbv(0)[12:0])
    immB = Signal(intbv(0)[12:0])
    ins = ins_dec(data_in, opcode, rd, func3, rs1, rs2, func7, immI, immS, immB, immU, immJ)

    @instance
    def stimulus():
        data_in.next = 0b00000000000000000010010100010111  # U-AUIPC
        yield delay(2)
        data_in.next = 0b00000000101100000000001010110011  # R-type
        yield delay(2)
        data_in.next = 0b11111111111100101000001010010011  # I-Type
        yield delay(2)
        data_in.next = 0b00000000000000101010001110000011  # I(load)
        yield delay(2)
        data_in.next = 0b00000000000000001000000001100111  # I(JALR)
        yield delay(2)
        data_in.next = 0b00000000000000000000000001110011  # I(sys)
        yield delay(2)
        data_in.next = 0b00000000000001010010000000100011  # S-type
        yield delay(2)
        data_in.next = 0b11111110000000101001101011100011  # B-Type
        yield delay(2)
        data_in.next = 0b11111110110111111111000011101111  # J-type

    @instance
    def monitor():
        yield delay(2)
        print("%s" % (bin(data_in, 32)))
        print("%s%s%s" % (bin(immU, 20), bin(rd, 5), bin(opcode, 7)))
        yield delay(2)
        print()
        print("%s" % (bin(data_in, 32)))
        print("%s%s%s%s%s%s" % (bin(func7, 7), bin(rs2, 5), bin(rs1, 5), bin(func3, 3), bin(rd, 5), bin(opcode, 7)))
        yield delay(2)
        print()
        print("%s" % (bin(data_in, 32)))
        print("%s%s%s%s%s" % (bin(immI, 12), bin(rs1, 5), bin(func3, 3), bin(rd, 5), bin(opcode, 7)))
        yield delay(2)
        print()
        print("%s" % (bin(data_in, 32)))
        print("%s%s%s%s%s" % (bin(immI, 12), bin(rs1, 5), bin(func3, 3), bin(rd, 5), bin(opcode, 7)))
        yield delay(2)
        print()
        print("%s" % (bin(data_in, 32)))
        print("%s%s%s%s%s" % (bin(immI, 12), bin(rs1, 5), bin(func3, 3), bin(rd, 5), bin(opcode, 7)))
        yield delay(2)
        print()
        print("%s" % (bin(data_in, 32)))
        print("%s%s%s%s%s" % (bin(immI, 12), bin(rs1, 5), bin(func3, 3), bin(rd, 5), bin(opcode, 7)))
        yield delay(2)
        print()
        print("%s" % (bin(data_in, 32)))
        print("%s%s%s%s%s%s" % (bin(immS[12:5], 7), bin(rs2, 5), bin(rs1, 5), bin(func3, 3), bin(immS[5:0], 5),
                                bin(opcode, 7)))
        yield delay(2)
        print()
        print("%s" % (bin(data_in, 32)))
        print("%s" % (bin(immB, 12)))
        yield delay(2)
        print()
        print("%s" % (bin(data_in, 32)))
        print("%s" % (bin(immJ, 20)))
        yield delay(2)

    return instances()


def convert():
    data_in = Signal(intbv(0)[32:0])
    opcode = Signal(intbv(0)[7:0])
    rd = Signal(intbv(0)[5:0])
    func3 = Signal(intbv(0)[3:0])
    rs1 = Signal(intbv(0)[5:0])
    rs2 = Signal(intbv(0)[5:0])
    func7 = Signal(intbv(0)[7:0])
    immU = Signal(intbv(0)[20:0])
    immJ = Signal(intbv(0)[20:0])
    immI = Signal(intbv(0)[12:0])
    immS = Signal(intbv(0)[12:0])
    immB = Signal(intbv(0)[12:0])
    ins = ins_dec(data_in, opcode, rd, func3, rs1, rs2, func7, immI, immS, immB, immU, immJ)
    ins.convert(hdl='Verilog')


# convert()
# tb = Test()
# tb.run_sim(100)