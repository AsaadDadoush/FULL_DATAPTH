import math
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


class Memory_copy:
    def __init__(self, Memory_1=[], Memory_2=[], Memory_3=[], Memory_4=[]):
        self.Memory_1 = Memory_1
        self.Memory_2 = Memory_2
        self.Memory_3 = Memory_3
        self.Memory_4 = Memory_4


global_copy = Memory_copy()

program = Memory()
program.load_binary_file(path="D:/Osama Shits/OsamaPure.txt", starting_address=0)
program.load_binary_file(path="D:/Osama Shits/OsamaPure1.txt", starting_address=8192)


@block
def memory(data_in, enable, size, address, data_out):
    Mem1 = [Signal(intbv(0)[8:]) for i in range(3072)]
    Mem2 = [Signal(intbv(0)[8:]) for i in range(3072)]
    Mem3 = [Signal(intbv(0)[8:]) for i in range(3072)]
    Mem4 = [Signal(intbv(0)[8:]) for i in range(3072)]
    address_index = 0
    for i in range(3072):
        data = Signal(intbv(to_number(program.read(address_index, 4), 4, True))[32:])
        Mem1[i].next = data[8:]
        Mem1[i]._update()
        Mem2[i].next = data[16:8]
        Mem2[i]._update()
        Mem3[i].next = data[24:16]
        Mem3[i]._update()
        Mem4[i].next = data[32:24]
        Mem4[i]._update()
        address_index += 4
        # print("_" * 35)
        # print('Address: ', address_index, "Has been loaded in address %s" % (int(address_index/4)))
        # print("%s|%s|%s|%s" % (bin(Mem4[i], 8), bin(Mem3[i], 8), bin(Mem2[i], 8), bin(Mem1[i], 8)))
        # address_index += 4
    #     global global_copy
    #     global_copy = Memory_copy(Mem1, Mem2, Mem3, Mem4)
    #                                   5        13
    #                    000000000001|00101|000|01101|0010011 done
    #                    0000001|01011|00100|000|00101|0110011 done
    #                                    5       7
    #                    000000000000|00101|010|00111|0000011  # I(load)
    #
    # data = Signal(intbv("00000000000000101000011010010011")[32:])
    # Mem1[0].next = data[8:]
    # Mem2[0].next = data[16:8]
    # Mem3[0].next = data[24:16]
    # Mem4[0].next = data[32:24]
    # Mem1[0]._update()
    # Mem2[0]._update()
    # Mem3[0]._update()
    # Mem4[0]._update()
    # data = Signal(intbv("00000000000000101010001110000011")[32:])
    # Mem1[1].next = data[8:]
    # Mem2[1].next = data[16:8]
    # Mem3[1].next = data[24:16]
    # Mem4[1].next = data[32:24]
    # Mem1[1]._update()
    # Mem2[1]._update()
    # Mem3[1]._update()
    # Mem4[1]._update()
    # data = Signal(intbv("00000000000000000000000001000101")[32:])
    # Mem1[2].next = data[8:]
    # Mem2[2].next = data[16:8]
    # Mem3[2].next = data[24:16]
    # Mem4[2].next = data[32:24]
    # Mem1[2]._update()
    # Mem2[2]._update()
    # Mem3[2]._update()
    # Mem4[2]._update()

    @always(data_in)
    def WriteLogic():
        if enable == 1:
            if size == 0:
                Mem1[address].next = data_in[8:0]

            elif size == 1:
                Mem1[address].next = data_in[8:0]
                Mem2[address].next = data_in[16:8]

            elif size == 2:
                Mem1[address].next = data_in[8:0]
                Mem2[address].next = data_in[16:8]
                Mem3[address].next = data_in[24:16]
                Mem4[address].next = data_in[32:24]
            else:
                Mem1[address].next = data_in[8:0]
                Mem2[address].next = data_in[16:8]
                Mem3[address].next = data_in[24:16]
                Mem4[address].next = data_in[32:24]


    @always_comb
    def readLogic():
        if size == 0:
            data_out.next = concat("00000000", "00000000", "00000000", Mem1[address])
        elif size == 1:
            data_out.next = concat("00000000", "00000000", Mem2[address], Mem1[address])
        else:
            data_out.next = concat(Mem4[address], Mem3[address], Mem2[address], Mem1[address])
        print("********************************************************* Instruction *********************************************************")
        print("=============================== Memory ==============================")
        print("Address: ", address.next+0)
        print("Size: ",size+0)
        index = 2
        print(("Memory[%s]: %s%s%s%s")%(index,bin(Mem4[index],8),bin(Mem3[index],8),bin(Mem2[index],8),bin(Mem1[index],8)))
        print(("Memory[%s]: %s (in Decimal)")%(index,concat(bin(Mem4[index],8),bin(Mem3[index],8),bin(Mem2[index],8),bin(Mem1[index],8))+0))
        print("")


    return instances()


@block
def testbench():
    addres = Signal(intbv(0)[32:])
    data_in = Signal(intbv(0)[32:])
    data_out = Signal(intbv(0)[32:])
    enable = Signal(bool(0))
    size = Signal(intbv(0)[2:])
    ins = memory(data_in, enable, size, addres, data_out)

    @instance
    def monitor():
        yield delay(1)
        print("addres |             data_in              |             data_out                | enable")

        enable.next = 1
        yield delay(2)
        address_counter = 0
        for i in range(12287):
            size.next = 2
            yield delay(1)
            addres.next = i
            if address_counter == 12287:
                break
            data_in.next = intbv(to_number(program.read(address_counter, 4), 4, True))[32:]
            address_counter += 4
            yield delay(6)
            print("%s  | %s |   %s  |  %s " % (i, data_in + 0, data_out + 0, bin(enable)))

        yield delay(2)
        enable.next = 0
        for i in range(12287):
            yield delay(2)
            enable.next = 0
            size.next = 2
            addres.next = i
            yield delay(2)
            print("%s  | %s |   %s  |  %s " % (i, data_in + 0, data_out + 0, bin(enable)))

        size.next = 1
        addres.next = 2049
        yield delay(2)
        print(data_out + 0)
        yield delay(1)

    return instances()


def convert():
    addres = Signal(intbv(0)[14:])
    data_in = Signal(intbv(0)[32:])
    data_out = Signal(intbv(0)[32:])
    enable = Signal(bool(0))
    size = Signal(intbv(0)[2:])
    load_flag = Signal(bool(0))
    load_line = Signal(intbv(0)[32:])
    tst = memory(data_in, enable, size, addres, data_out, load_line, load_flag)
    tst.convert(hdl='Verilog')

# convert()

# tb = testbench()
# tb.run_sim()
# print(Mem1)
