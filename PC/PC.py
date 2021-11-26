from myhdl import*
@block
def pc(pass_input,out,reset,clk):
    @always_seq(clk.posedge,reset=reset)
    def pcblock():
        out.next=pass_input
    return instances()

@block
def test():
    pass_input = Signal(intbv(0)[32:]) #to represrent 16384
    out = Signal(intbv(0)[32:])
    clk = Signal(bool(0))
    reset= ResetSignal(0, active=1, isasync=True)
    ins = pc(pass_input, out,reset, clk)

    @always(delay(1))
    def clkgen():
        clk.next = not clk

    @instance
    def stimulus():
        reset.next=0
        pass_input.next = 0b111

        yield clk.posedge
        yield clk.posedge
        print((out.next))

    return instances()

def convert():
    pass_input = Signal(intbv(0)[32:])  # to represrent 16384
    out = Signal(intbv(0)[32:])
    clk = Signal(bool(0))
    reset = ResetSignal(0, active=1, isasync=True)
    test = pc(pass_input, out,reset, clk)
    test.convert(hdl='Verilog')


convert()
tb=test()
tb.run_sim(500)
