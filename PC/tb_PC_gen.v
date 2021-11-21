module tb_PC_gen;

reg [31:0] PC;
reg [31:0] imm;
reg sel;
wire [31:0] out;

initial begin
    $from_myhdl(
        PC,
        imm,
        sel
    );
    $to_myhdl(
        out
    );
end

PC_gen dut(
    PC,
    imm,
    sel,
    out
);

endmodule
