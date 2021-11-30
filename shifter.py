from myhdl import *


@block
def shifter(data_in, sel, data_out):
    @always(data_in and sel)
    def shift():
        if sel == 0:
            data_out.next = data_in.signed() << 1
        elif sel == 1:
            data_out.next = data_in.signed() << 12
        elif sel == 2:
            data_out.next = data_in.signed()
        else:
            data_out.next = data_in.signed()

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
        print(bin(data_out, 32))
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