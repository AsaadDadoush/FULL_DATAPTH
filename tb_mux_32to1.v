module tb_mux_32to1;

reg sel;
wire [31:0] out;
reg [31:0] imm;
reg [31:0] rs2;

initial begin
    $from_myhdl(
        sel,
        imm,
        rs2
    );
    $to_myhdl(
        out
    );
end

mux_32to1 dut(
    sel,
    out,
    imm,
    rs2
);

endmodule
