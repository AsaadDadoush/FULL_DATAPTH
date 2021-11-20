from myhdl import block, always, instances, instance, Signal, intbv, delay, now


@block
def registersFile(rs1In,rs2In,rd,REGwrite,data,clock,rs1Out,rs2Out,flush):
    registers = [Signal(intbv(0,min=-2**31, max=2**31-1)) for i in range(32)]# create 32 register with weidth of 32-bit
    @always(clock.posedge)
    def registers_b():
        if flush ==1:
             rs1Out.next=0
             rs2Out.next=0
             data.next=0
        else:
            rs1Out.next=registers[rs1In]  #first output value from register number [rs1In]
            rs2Out.next=registers[rs2In]  #second output value from register number [rs2In]
            for i in range (32):
               print('%d , #%d'%(registers[i],i))
            print()
            # print('%d , %d'%(registers[10],now()))
            if REGwrite:
                registers[rd].next = data
    return registers_b


@block
def testBench2():

    clock=Signal(bool(0))

    flush = Signal(bool(0))
    rs1In,rs2In,rd=[Signal(intbv(0,min=-2**31, max=2**31-1)) for i in range(3)]
    REGwrite,data = [Signal(intbv(0)) for i in range(2)]
    rs1Out,rs2Out=[Signal(intbv(0,min=-2**31, max=2**31-1)) for i in range(2)]
    reg1=registersFile(rs1In,rs2In,rd,REGwrite,data,clock,rs1Out,rs2Out, flush)

    @always(delay(5))
    def clockGeneration1():
        clock.next = not clock

    @instance
    def test2():
      yield delay(5)
      print('---------------------------------------------------------------------------------------------------------------')
      rs1In.next=0b11
      rs2In.next=0b111
      rd.next=0b1010
      yield delay (10)


      print("| %-15s | %-15s | %-15s | %-15s | %-15s | %-15s | %-15s |"%('rs1In','rs2In','rd','data','REGwrite','rs1Out','rs2Out'))
      print("| %-15d | %-15d | %-15d | %-15d | %-15d | %-15d | %-15d |"%(rs1In,rs2In,rd,data,REGwrite,rs1Out,rs2Out))
      print('---------------------------------------------------------------------------------------------------------------')
      data.next = 20
      REGwrite.next=1
      yield delay (10)


      print("| %-15s | %-15s | %-15s | %-15s | %-15s | %-15s | %-15s |"%('rs1In','rs2In','rd','data','REGwrite','rs1Out','rs2Out'))
      print("| %-15d | %-15d | %-15d | %-15d | %-15d | %-15d | %-15d |"%(rs1In,rs2In,rd,data,REGwrite,rs1Out,rs2Out))
      print('---------------------------------------------------------------------------------------------------------------')
      REGwrite.next=0
      yield delay (10)

    return instances()



if __name__ =='__main__':
    test=testBench2()
    test.run_sim(120)
