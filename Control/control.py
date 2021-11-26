import opcode

from myhdl import *


@block
def control(opcode, func3, func7, branch_result, size_sel, operation_sel, enable_write,PC_genrator_sel, imm_sel, rs2_or_imm_or_4,
            PC_or_Address, PC_or_rs1, ALU_or_load_or_immShiftedBy12):
    @always_comb
    def control_cir():
        # R-type
        if opcode == 0b0110011:
            size_sel.next = 2
            enable_write.next = 0
            PC_genrator_sel.next = 0
            #todo
            imm_sel.next = 0
            rs2_or_imm_or_4.next = 0
            PC_or_Address.next = 0
            PC_or_rs1.next = 1
            ALU_or_load_or_immShiftedBy12.next = 0
            # ADD
            if func3 == 0x0 and func7 == 0x00:
                operation_sel.next = 0
            # Todo  SUB
            # elif func3 == 0x00 and 0x20:
            #     operation_sel.next = 0

            # XOR
            elif func3 == 0x4 and func7 == 0x00:
                operation_sel.next = 5
            # OR
            elif func3 == 0x6 and func7 == 0x00:
                operation_sel.next = 4

            # AND
            elif func3 == 0x7 and func7 == 0x00:
                operation_sel.next = 3

            # Shift Right logical
            elif func3 == 0x1 and func7 == 0x00:
                operation_sel.next = 6


            # Shift Right logical
            elif func3 == 0x5 and func7 == 0x00:
                operation_sel.next = 7

            # Shift Right Arith*
            elif func3 == 0x5 and func7 == 0x20:
                operation_sel.next = 7

            # set less than
            elif func3 == 0x2 and func7 == 0x00:
                operation_sel.next = 10

            # set less than(U)
            elif func3 == 0x3 and func7 == 0x00:
                operation_sel.next = 10


            # MUL
            elif func3 == 0x0 and func7 == 0x01:
                operation_sel.next = 1


            # DIV
            elif func3 == 0x4 and func7 == 0x01:
                operation_sel.next = 2


            # DIV (U)
            elif func3 == 0x5 and func7 == 0x01:
                operation_sel.next = 2


            # Remainder
            elif func3 == 0x6 and func7 == 0x01:
                operation_sel.next = 12

            # Remainder (U)
            elif func3 == 0x7 and func7 == 0x01:
                operation_sel.next = 12

        # I-type
        elif opcode == 0b0010011:
            size_sel.next = 2
            enable_write.next = 0
            PC_genrator_sel.next = 0
            #todo
            imm_sel.next = 0
            rs2_or_imm_or_4.next = 1
            PC_or_Address.next = 0
            PC_or_rs1.next = 1
            ALU_or_load_or_immShiftedBy12.next = 0
            # Add imm
            if func3 == 0x0:
                operation_sel.next = 0
            # XOR imm
            elif func3 == 0x4:
                operation_sel.next = 5

            # OR imm
            elif func3 == 0x6:
                operation_sel.next = 4

            # AND imm
            elif func3 == 0x7:
                operation_sel.next = 3

            # Shift left logical imm
            elif func3 == 0x1 and func7 == 0x00:
                operation_sel.next = 12

            # Shift right logical imm
            elif func3 == 0x5 and func7 == 0x00:
                operation_sel.next = 13

            # Shift right Arith imm
            elif func3 == 0x5 and func7 == 0x20:
                operation_sel.next = 14

            # Set less than imm
            elif func3 == 0x2:
                operation_sel.next = 10

            # Set less than imm (U)
            elif func3 == 0x3:
                operation_sel.next = 10

        # I-type (LOAD instructions)
        elif opcode == 0b0000011:
            enable_write.next = 0
            PC_genrator_sel.next = 0
            #todo
            imm_sel.next = 0
            rs2_or_imm_or_4.next = 1
            PC_or_Address.next = 1
            PC_or_rs1.next = 1
            ALU_or_load_or_immShiftedBy12.next = 1
            # load Byte
            if func3 == 0x0:
                size_sel.next = 0
                operation_sel.next = 0

            # load Half
            elif func3 == 0x1:
                size_sel.next = 1
                operation_sel.next = 0

            # load Word
            elif func3 == 0x2:
                size_sel.next = 2
                operation_sel.next = 0
            #todo
            # load Byte(U)
            elif func3 == 0x4:
                size_sel.next = 0
                operation_sel.next = 0
            #todo
            # load Half(U)
            elif func3 == 0x5:
                size_sel.next = 1
                operation_sel.next = 0

        # S-Type
        elif opcode == 0b0100011:
            enable_write.next = 1
            PC_genrator_sel.next = 0
            # todo
            imm_sel.next = 0
            rs2_or_imm_or_4.next = 1
            PC_or_Address.next = 1
            PC_or_rs1.next = 1
            ALU_or_load_or_immShiftedBy12.next = 1
            # Store Byte
            if func3 == 0x0:
                size_sel.next = 0
                operation_sel.next = 0

            # Store Half
            elif func3 == 0x1:
                size_sel.next = 1
                operation_sel.next = 0

            # Store word
            elif func3 == 0x2:
                size_sel.next = 2
                operation_sel.next = 0

        # B-type
        elif opcode == 0b1100011:
            size_sel.next=2
            enable_write.next = 0
            # todo
            imm_sel.next = 0
            rs2_or_imm_or_4.next = 0
            PC_or_Address.next = 0
            PC_or_rs1.next = 1
            ALU_or_load_or_immShiftedBy12.next = 0
            # Branch ==
            if func3 == 0x0:
                operation_sel.next = 8
                if branch_result == 1:
                    PC_genrator_sel.next = 1
                else:
                    PC_genrator_sel.next = 0
            # Branch !=
            elif func3 == 0x1:
                operation_sel.next = 9
                if branch_result == 1:
                    PC_genrator_sel.next = 1
                else:
                    PC_genrator_sel.next = 0
            # Branch <
            elif func3 == 0x4:
                operation_sel.next = 10
                if branch_result == 1:
                    PC_genrator_sel.next = 1
                else:
                    PC_genrator_sel.next = 0
            # Branch <=
            elif func3 == 0x5:
                operation_sel.next = 11
                if branch_result == 1:
                    PC_genrator_sel.next = 1
                else:
                    PC_genrator_sel.next = 0
            # Branch <(U)
            elif func3 == 0x6:
                operation_sel.next = 10
                if branch_result == 1:
                    PC_genrator_sel.next = 1
                else:
                    PC_genrator_sel.next = 0
            # Branch <=(U)
            elif func3 == 0x7:
                operation_sel.next = 11
                if branch_result == 1:
                    PC_genrator_sel.next = 1
                else:
                    PC_genrator_sel.next = 0
        # J-type (Jump And Link)
        elif opcode == 0b1101111:
            size_sel.next = 2
            operation_sel.next = 0
            enable_write.next = 0
            PC_genrator_sel.next = 1
            # todo
            imm_sel.next = 0
            rs2_or_imm_or_4.next = 2
            PC_or_Address.next = 0
            PC_or_rs1.next = 0
            ALU_or_load_or_immShiftedBy12.next = 0
        # I-type (Jump And Link Reg)
        elif opcode == 0b1100111:
            size_sel.next = 2
            operation_sel.next = 0
            enable_write.next = 0
            PC_genrator_sel.next = 1
            # todo
            imm_sel.next = 0
            rs2_or_imm_or_4.next = 2
            PC_or_Address.next = 0
            PC_or_rs1.next = 0
            ALU_or_load_or_immShiftedBy12.next = 0
        # U-type (Load Upper Imm)
        elif opcode==0b0110111:
            size_sel.next = 2
            operation_sel.next = 0
            enable_write.next = 0
            PC_genrator_sel.next = 0
            # todo
            imm_sel.next = 0
            rs2_or_imm_or_4.next = 0
            PC_or_Address.next = 0
            PC_or_rs1.next = 0
            ALU_or_load_or_immShiftedBy12.next = 2 # rd = imm << 12
        # U-type (Add Upper Imm to PC)
        else:
            size_sel.next = 2
            operation_sel.next = 0
            enable_write.next = 0
            PC_genrator_sel.next = 0
            # todo
            imm_sel.next = 0
            rs2_or_imm_or_4.next = 1
            PC_or_Address.next = 0
            PC_or_rs1.next = 0
            ALU_or_load_or_immShiftedBy12.next = 0  # rd = PC + (imm << 12)
    return instances()


@block
def test_bench():
    opcode = Signal(intbv(0)[7:])
    func3 = Signal(intbv(0)[5:])
    func7 = Signal(intbv(0)[5:])
    branch_result = Signal(intbv(0)[32:])
    size_sel = Signal(intbv(0)[2:])
    operation_sel = Signal(intbv(0)[4:])
    enable_write = Signal(bool(0))
    PC_genrator_sel = Signal(intbv(0)[2:])
    # todo
    imm_sel = Signal(intbv(0)[32:])
    rs2_or_imm_or_4 = Signal(intbv(0)[2:])
    PC_or_Address= Signal(bool(0))
    PC_or_rs1 = Signal(bool(0))
    ALU_or_load_or_immShiftedBy12 = Signal(intbv(0)[2:])
    ins = control(opcode, func3, func7, branch_result, size_sel, operation_sel, enable_write,PC_genrator_sel, imm_sel, rs2_or_imm_or_4,
            PC_or_Address, PC_or_rs1, ALU_or_load_or_immShiftedBy12)


def convert():
    opcode = Signal(intbv(0)[7:])
    func3 = Signal(intbv(0)[5:])
    func7 = Signal(intbv(0)[5:])
    branch_result = Signal(intbv(0)[32:])
    size_sel = Signal(intbv(0)[2:])
    operation_sel = Signal(intbv(0)[4:])
    enable_write = Signal(bool(0))
    PC_genrator_sel = Signal(intbv(0)[2:])
    # todo
    imm_sel = Signal(intbv(0)[32:])
    rs2_or_imm_or_4 = Signal(intbv(0)[2:])
    PC_or_Address = Signal(bool(0))
    PC_or_rs1 = Signal(bool(0))
    ALU_or_load_or_immShiftedBy12 = Signal(intbv(0)[2:])
    ins = control(opcode, func3, func7, branch_result, size_sel, operation_sel, enable_write, PC_genrator_sel, imm_sel,
                  rs2_or_imm_or_4,
                  PC_or_Address, PC_or_rs1, ALU_or_load_or_immShiftedBy12)
    ins.convert(hdl='Verilog')


convert()
