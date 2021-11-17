module tb_andG;

reg in1;
reg in2;
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
