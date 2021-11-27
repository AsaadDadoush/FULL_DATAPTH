// File: extender.v
// Generated by MyHDL 0.11
// Date: Sat Nov 27 21:40:02 2021


`timescale 1ns/10ps

module extender (
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


input [11:0] immI;
input [11:0] immS;
input [11:0] immB;
input [19:0] immU;
input [19:0] immJ;
output [31:0] imm32I;
wire [31:0] imm32I;
output [31:0] imm32S;
wire [31:0] imm32S;
output [31:0] imm32B;
wire [31:0] imm32B;
output [31:0] imm32U;
wire [31:0] imm32U;
output [31:0] imm32J;
wire [31:0] imm32J;





assign imm32I = $signed(immI)[32-1:0];
assign imm32S = $signed(immS)[32-1:0];
assign imm32B = $signed(immB)[32-1:0];
assign imm32U = $signed(immU)[32-1:0];
assign imm32J = $signed(immJ)[32-1:0];

endmodule
