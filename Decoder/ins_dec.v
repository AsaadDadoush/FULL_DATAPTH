// File: ins_dec.v
// Generated by MyHDL 0.11
// Date: Fri Nov 26 22:52:10 2021


`timescale 1ns/10ps

module ins_dec (
    data_in,
    opcode,
    rd,
    func3,
    rs1,
    rs2,
    func7,
    immI,
    immS,
    immB,
    immU,
    immJ
);


input [31:0] data_in;
output [6:0] opcode;
wire [6:0] opcode;
output [4:0] rd;
wire [4:0] rd;
output [2:0] func3;
wire [2:0] func3;
output [4:0] rs1;
wire [4:0] rs1;
output [4:0] rs2;
wire [4:0] rs2;
output [6:0] func7;
wire [6:0] func7;
output [11:0] immI;
wire [11:0] immI;
output [11:0] immS;
wire [11:0] immS;
output [11:0] immB;
wire [11:0] immB;
output [19:0] immU;
wire [19:0] immU;
output [19:0] immJ;
wire [19:0] immJ;





assign opcode = data_in[7-1:0];
assign func3 = data_in[15-1:12];
assign func7 = data_in[32-1:25];
assign rd = data_in[12-1:7];
assign rs1 = data_in[20-1:15];
assign rs2 = data_in[25-1:20];
assign immI = data_in[32-1:20];
assign immS = {data_in[32-1:25], data_in[12-1:7]};
assign immB = {data_in[32-1:31], data_in[8-1:7], data_in[31-1:25], data_in[12-1:8]};
assign immU = data_in[32-1:12];
assign immJ = {data_in[31], data_in[20-1:12], data_in[20], data_in[31-1:21]};

endmodule
