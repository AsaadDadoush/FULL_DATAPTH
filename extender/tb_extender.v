module tb_extender;

reg [19:0] input_12or20;
wire [31:0] output32;

initial begin
    $from_myhdl(
        input_12or20
    );
    $to_myhdl(
        output32
    );
end

extender dut(
    input_12or20,
    output32
);

endmodule
