// File: registers.v
// Generated by MyHDL 0.11
// Date: Sat Nov 20 22:31:02 2021


`timescale 1ns/10ps

module registers (
    rs1,
    rs2,
    rd,
    rs1_out,
    rs2_out,
    clk,
    enable,
    data
);


input [4:0] rs1;
input [4:0] rs2;
input [4:0] rd;
output [31:0] rs1_out;
reg [31:0] rs1_out;
output [31:0] rs2_out;
reg [31:0] rs2_out;
input clk;
input enable;
input [31:0] data;

reg [31:0] Reg [0:32-1];



always @(posedge clk) begin: REGISTERS_REGISTER_SUB
    integer i;
    rs1_out <= Reg[rs1];
    rs2_out <= Reg[rs2];
    for (i=0; i<32; i=i+1) begin
        $write("%0d", Reg[i]);
        $write(" , reg ");
        $write("%0d", i);
        $write("\n");
    end
    $write("\n");
    if ((enable == 1)) begin
        Reg[rd] <= data;
    end
end

endmodule
