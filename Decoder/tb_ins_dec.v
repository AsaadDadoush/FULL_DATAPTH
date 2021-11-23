module tb_ins_dec;

reg [31:0] pass_bits;
wire [6:0] opcode;
wire [4:0] rd;
wire [2:0] func3;
wire [4:0] rs1;
wire [4:0] rs2;
wire [6:0] func7;
wire [11:0] imm12;
wire [19:0] imm20;

initial begin
    $from_myhdl(
        pass_bits
    );
    $to_myhdl(
        opcode,
        rd,
        func3,
        rs1,
        rs2,
        func7,
        imm12,
        imm20
    );
end

ins_dec dut(
    pass_bits,
    opcode,
    rd,
    func3,
    rs1,
    rs2,
    func7,
    imm12,
    imm20
);

endmodule
