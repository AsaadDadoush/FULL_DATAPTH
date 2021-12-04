from myhdl import *

@block
def sign_extender(data_in,sel,data_out):
    # sel >> 0 for 8-bit msb extend
    # sel >> 1 for 16-bit msb extend
    # sel >> 2 for zero-extends

    @always(data_in, sel)
    def logic():
        if sel == 0:
            data_out.next = intbv(data_in[8:])[32:]
        elif sel == 1:
            data_out.next = intbv(data_in[16:]).signed()[32:]
        elif sel == 2:
            data_out.next = data_in
        else:
            data_out.next = data_in
        print("=========================== Sign Extender ===========================")
        print("Data in:  ", bin(data_in, 32))
        print("Selection:  ", sel+0)
        print("Data Out: ", bin(data_out.next, 32))
        print("")
    return logic


@block
def test_bench():
    data_in = Signal(intbv(0)[32:])
    data_out = Signal(intbv(0)[32:])
    sel = Signal(intbv(0)[2:])
    ins = sign_extender(data_in, sel, data_out)

    @instance
    def monitor():
        print('-'*50)
        data_in.next = intbv("00000000000000000000000011111101")[32:]
        sel.next = 0
        yield delay(1)
        print("Data input:  ", bin(data_in, 32))
        print("Selection: ", sel+0)
        print("Data output: ",bin(data_out, 32))
        print('-' * 50)
        data_in.next = intbv("00000000000000001111111111111101")[32:]
        sel.next = 1
        yield delay(1)
        print("Data input:  ", bin(data_in, 32))
        print("Selection: ", sel+0)
        print("Data output: ", bin(data_out, 32))
        print('-' * 50)
        data_in.next = intbv("000000000000111111111111111111101")[32:]
        sel.next = 2
        yield delay(1)
        print("Data input:  ", bin(data_in, 32))
        print("Selection: ", sel+0)
        print("Data output: ", bin(data_out, 32))
    return instances()


def convert():
    data_in = Signal(intbv(0)[32:])
    data_out = Signal(intbv(0)[32:])
    sel = Signal(intbv(0)[2:])

    ins = sign_extender(data_in,sel,data_out)
    ins.convert(hdl='Verilog')


# test = test_bench()
# test.run_sim()
# convert()

