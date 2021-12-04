from myhdl import *


@block
def shifter(data_in, sel, data_out):
    @always(data_in, sel)
    def shift():
        if sel == 0:
            data_out.next = data_in.signed() << 1
        elif sel == 1:
            data_out.next = data_in.signed() << 12
        elif sel == 2:
            data_out.next = data_in.signed()
        else:
            data_out.next = data_in.signed()
        print("============================ imm Shifter ============================")
        print("Data in: ", data_in+0)
        print("Selection: ",sel + 0)
        print("Data Out: ", data_out.next + 0)
        print("")

    return shift


@block
def test_bench():
    data_in = Signal(modbv(0)[32:])
    data_out = Signal(modbv(0)[32:])
    sel = Signal(intbv(0)[2:])
    ins = shifter(data_in, sel, data_out)

    @instance
    def monitor():
        sel.next = 0
        data_in.next = 0b11111111111111111111111111110110
        yield delay(1)
        print("Data input: ",bin(data_in,32))
        print("Selection: ", sel + 0)
        print("Data output: ", bin(data_out, 32))
        print('-'*50)
        sel.next = 1
        data_in.next = 0b11111111111111111111111111110110
        yield delay(1)
        print("Data input: ", bin(data_in, 32))
        print("Selection: ", sel + 0)
        print("Data output: ", bin(data_out, 32))
        sel.next = 2
        data_in.next = 0b11111111111111111111111111110110
        yield delay(1)
        print('-' * 50)
        print("Data input: ", bin(data_in, 32))
        print("Selection: ", sel + 0)
        print("Data output: ", bin(data_out, 32))
    return instances()


def convert():
    data_in = Signal(modbv(0)[32:])
    data_out = Signal(modbv(0)[32:])
    sel = Signal(intbv(0)[2:])
    ins = shifter(data_in, sel, data_out)
    ins.convert(hdl='Verilog')


# tst = test_bench()
# tst.run_sim()
# convert()