module tb_extender;

reg [11:0] immI;
reg [11:0] immS;
reg [11:0] immB;
reg [19:0] immU;
reg [19:0] immJ;
wire [31:0] imm32I;
wire [31:0] imm32S;
wire [31:0] imm32B;
wire [31:0] imm32U;
wire [31:0] imm32J;

initial begin
    $from_myhdl(
        immI,
        immS,
        immB,
        immU,
        immJ
    );
    $to_myhdl(
        imm32I,
        imm32S,
        imm32B,
        imm32U,
        imm32J
    );
end

extender dut(
    immI,
    immS,
    immB,
    immU,
    immJ,
    imm32I,
    imm32S,
    imm32B,
    imm32U,
    imm32J
);

endmodule
