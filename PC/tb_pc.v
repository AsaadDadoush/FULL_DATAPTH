module tb_pc;

reg [13:0] pass_input;
wire [13:0] out;
reg reset;
reg clk;

initial begin
    $from_myhdl(
        pass_input,
        reset,
        clk
    );
    $to_myhdl(
        out
    );
end

pc dut(
    pass_input,
    out,
    reset,
    clk
);

endmodule
