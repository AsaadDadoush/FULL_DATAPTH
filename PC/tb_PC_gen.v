module tb_PC_gen;

reg [31:0] PC;
reg [31:0] rs1;
reg [31:0] imm;
reg [1:0] sel;
wire [31:0] out;

initial begin
    $from_myhdl(
        PC,
        rs1,
        imm,
        sel
    );
    $to_myhdl(
        out
    );
end

PC_gen dut(
    PC,
    rs1,
    imm,
    sel,
    out
);

endmodule