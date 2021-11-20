module tb_alu;

reg [31:0] a;
reg [31:0] b;
reg [3:0] sel;
wire [31:0] out;

initial begin
    $from_myhdl(
        a,
        b,
        sel
    );
    $to_myhdl(
        out
    );
end

alu dut(
    a,
    b,
    sel,
    out
);

endmodule
