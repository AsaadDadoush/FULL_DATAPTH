module tb_mux_3to1;

reg [31:0] i0;
reg [31:0] i1;
reg [31:0] i2;
reg [1:0] sel;
wire [31:0] out;

initial begin
    $from_myhdl(
        i0,
        i1,
        i2,
        sel
    );
    $to_myhdl(
        out
    );
end

mux_3to1 dut(
    i0,
    i1,
    i2,
    sel,
    out
);

endmodule
