module tb_extender;

reg [2:0] sel;
reg [11:0] immI;
reg [11:0] immS;
reg [11:0] immB;
reg [19:0] immU;
reg [19:0] immJ;
wire [31:0] imm32;

initial begin
    $from_myhdl(
        sel,
        immI,
        immS,
        immB,
        immU,
        immJ
    );
    $to_myhdl(
        imm32
    );
end

extender dut(
    sel,
    immI,
    immS,
    immB,
    immU,
    immJ,
    imm32
);

endmodule
