module tb_andG;

reg [31:0] in1;
reg [31:0] in2;
wire out;

initial begin
    $from_myhdl(
        in1,
        in2
    );
    $to_myhdl(
        out
    );
end

andG dut(
    in1,
    in2,
    out
);

endmodule
