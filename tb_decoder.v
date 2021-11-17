module tb_decoder;

reg [31:0] instruction;
wire [4:0] rs1;
wire [4:0] rs2;
wire [4:0] rd;
wire [31:0] imm;

initial begin
    $from_myhdl(
        instruction
    );
    $to_myhdl(
        rs1,
        rs2,
        rd,
        imm
    );
end

decoder dut(
    instruction,
    rs1,
    rs2,
    rd,
    imm
);

endmodule
