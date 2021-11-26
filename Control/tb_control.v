module tb_control;

reg [6:0] opcode;
reg [4:0] func3;
reg [4:0] func7;
reg [31:0] branch_result;
wire [1:0] size_sel;
wire [3:0] operation_sel;
wire enable_write;
wire [1:0] PC_genrator_sel;
wire [31:0] imm_sel;
wire [1:0] rs2_or_imm_or_4;
wire PC_or_Address;
wire PC_or_rs1;
wire [1:0] ALU_or_load_or_immShiftedBy12;

initial begin
    $from_myhdl(
        opcode,
        func3,
        func7,
        branch_result
    );
    $to_myhdl(
        size_sel,
        operation_sel,
        enable_write,
        PC_genrator_sel,
        imm_sel,
        rs2_or_imm_or_4,
        PC_or_Address,
        PC_or_rs1,
        ALU_or_load_or_immShiftedBy12
    );
end

control dut(
    opcode,
    func3,
    func7,
    branch_result,
    size_sel,
    operation_sel,
    enable_write,
    PC_genrator_sel,
    imm_sel,
    rs2_or_imm_or_4,
    PC_or_Address,
    PC_or_rs1,
    ALU_or_load_or_immShiftedBy12
);

endmodule
