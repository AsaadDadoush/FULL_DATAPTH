from myhdl import *


@block
def registers(rs1, rs2, rd, rs1_out, rs2_out, clk, enable, data):
    Reg = [Signal(intbv(0)[32:]) for i in range(32)]

    @always(clk.posedge)
    def register_sub():
        rs1_out.next = Reg[rs1]
        rs2_out.next = Reg[rs2]
        # for i in range(32):
        #     print('%d , reg %d' % (Reg[i], i))
        # print()

        if enable == 1:

            Reg[rd].next = data

    return register_sub


@block
def testbench():
    rs1 = Signal(intbv(0)[5:])
    rs2 = Signal(intbv(0)[5:])
    rd = Signal(intbv(0)[5:])
    rs1_out = Signal(intbv(0)[32:])
    rs2_out = Signal(intbv(0)[32:])
    clk = Signal(bool(0))
    enable = Signal(bool(0))
    data = Signal(intbv(0)[32:])
    reg = registers(rs1, rs2, rd, rs1_out, rs2_out, clk, enable, data)

    @always(delay(2))
    def clkgen():
        clk.next = not clk

    @instance
    def stimulus():
        enable.next = 1
        yield delay(5)
        rd.next = 0b00111
        data.next = 0b11111
        yield delay(5)
        rd.next = 0b00011
        data.next = 0b01001
        yield delay(5)
        print('======================================================')
        rs1.next = 0b00111
        rs2.next = 0b00011
        rd.next = 0b00000
        yield delay(10)

        print("rs1      | rs2   |   rd     |         rs1_out                    |           rs2_out      "
              "                 |                data              |   enable  |")
        print("%s    | %s |   %s  |  %s  |    %s     | %s |        %s  | " % \
              (bin(rs1, 5), bin(rs2, 5), bin(rd, 5), bin(rs1_out, 32), bin(rs1_out, 32), bin(data, 32), bin(enable, 1)))

        data.next = 0b01111
        enable.next = 1
        yield delay(5)

        print("rs1      | rs2   |   rd     |         rs1_out                    |           rs2_out         "
              "              |                data              |   enable  |")
        print("%s    | %s |   %s  |  %s  |    %s     | %s |        %s  | " % \
              (bin(rs1, 5), bin(rs2, 5), bin(rd, 5), bin(rs1_out, 32), bin(rs2_out, 32), bin(data, 32), bin(enable, 1)))
        enable.next = 0
        yield delay(5)

    return instances()

def convert():
    rs1 = Signal(intbv(0)[5:])
    rs2 = Signal(intbv(0)[5:])
    rd = Signal(intbv(0)[5:])
    rs1_out = Signal(intbv(0)[32:])
    rs2_out = Signal(intbv(0)[32:])
    clk = Signal(bool(0))
    enable = Signal(bool(0))
    data = Signal(intbv(0)[32:])
    reg = registers(rs1, rs2, rd, rs1_out, rs2_out, clk, enable, data)
    reg.convert(hdl='Verilog')


convert()
tst = testbench()
tst.run_sim(50)