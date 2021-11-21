module tb_barrel_shifter;

wire [31:0] load_value;
reg [31:0] load_input;
reg [1:0] shift_reg;

initial begin
    $from_myhdl(
        load_input,
        shift_reg
    );
    $to_myhdl(
        load_value
    );
end

barrel_shifter dut(
    load_value,
    load_input,
    shift_reg
);

endmodule
