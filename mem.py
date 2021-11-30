import struct

from myhdl import *
from memory import Memory

ACTIVE_LOW, INACTIVE_HIGH = 0, 1


def number_to_Buff(number: int, size, little_endian=True):
    endianness = '<' if little_endian else '>'
    if size == 1:
        fmt = f'b'
    elif size == 2:
        fmt = f'{endianness}h'
    elif size == 4:
        fmt = f'{endianness}i'
    elif size == 8:
        fmt = f'{endianness}q'
    else:
        raise Exception('unsupported Size')

    retV = struct.pack(fmt, number)
    return retV


def to_number(buff: bytearray, size, signed, little_endian=True):
    endianness = '<' if little_endian else '>'
    if size == 1:
        fmt = f'b' if signed else f'B'
    elif size == 2:
        fmt = f'{endianness}h' if signed else f'{endianness}H'
    elif size == 4:
        fmt = f'{endianness}i' if signed else f'{endianness}I'
    elif size == 8:
        fmt = f'{endianness}q' if signed else f'{endianness}Q'
    else:
        raise Exception('unsupported Size')

    retV = struct.unpack(fmt, buff[0:size])
    return retV[0]


program = Memory()
program.load_binary_file(path="D:/rarsProject/text.txt", starting_address=0)
program.load_binary_file(path="D:/rarsProject/data.txt", starting_address=8191)

@block
def memory(data_in, enable, size, addres, data_out):
    # MainMemory = [Signal(intbv(0)[32:]) for i in range(12287)]
    Mem1 = [Signal(intbv(0)[8:]) for i in range(32)]
    Mem2 = [Signal(intbv(0)[8:]) for i in range(32)]
    Mem3 = [Signal(intbv(0)[8:]) for i in range(32)]
    Mem4 = [Signal(intbv(0)[8:]) for i in range(32)]
    # data_out = Signal(intbv(0)[32:])

    @always_comb
    def WriteLogic():
        if enable == 1:
            if size == 0:
                Mem1[addres].next = data_in[8:0]

            elif size == 1:
                Mem1[addres].next = data_in[8:0]
                Mem2[addres].next = data_in[16:8]

            else:
                Mem1[addres].next = data_in[8:0]
                Mem2[addres].next = data_in[16:8]
                Mem3[addres].next = data_in[24:16]
                Mem4[addres].next = data_in[32:24]

    @always_comb
    def readLogic():
        if size == 0:
            data_out.next = concat("00000000", "00000000", "00000000", Mem1[addres])
        elif size == 1:
            data_out.next = concat("00000000", "00000000", Mem2[addres], Mem1[addres])
        else:
            data_out.next = concat(Mem4[addres], Mem3[addres], Mem2[addres], Mem1[addres])

    return instances()


@block
def testbench():
    addres = Signal(intbv(0)[14:])
    data_in = Signal(intbv(0)[32:])
    data_out = Signal(intbv(0)[32:])
    enable = Signal(bool(0))
    # clk = Signal(bool(0))
    size = Signal(intbv(0)[2:])
    ins = memory(addres, data_in, enable, data_out, size)

    # @always(delay(1))
    # def clkgen():
    #     clk.next = not clk

    @instance
    def monitor():
        yield delay(1)
        print("addres |             data_in              |             data_out                | enable")

        enable.next = 1
        yield delay(2)
        for i in range(12284):
            size.next = 0
            yield delay(1)
            data_in.next, addres.next = intbv(to_number(program.read(i, 1), 1, True))[32:], i
            yield delay(1)
            print("%s  | %s |   %s  |  %s " % (addres + 0, data_in + 0, data_out + 0, bin(enable)))
        # for i in range(8280):
        #     size.next = 0
        #     addres.next = i
        #     enable.next = 0
        #     yield delay(2)
        #     print("%s  | %s |   %s  |  %s " % (addres + 0, data_in + 0, bin(data_out,32), bin(enable)))
        size.next = 0
        addres.next = 8268
        yield delay(2)
        print(bin(data_out, 32))
        # yield delay(1)
        # print(to_number(program.read(8192, 4), 4, True))

    return instances()


def convert():
    addres = Signal(intbv(0)[14:])
    data_in = Signal(intbv(0)[32:])
    data_out = Signal(intbv(0)[32:])
    enable = Signal(bool(0))
    # clk = Signal(bool(0))
    size = Signal(intbv(0)[2:])
    tst = memory(data_in, enable, size, addres, data_out)
    tst.convert(hdl='Verilog')


# convert()
tb = testbench()
tb.run_sim(90000)