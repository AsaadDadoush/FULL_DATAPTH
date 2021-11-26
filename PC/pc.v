// File: pc.v
// Generated by MyHDL 0.11
// Date: Fri Nov 26 22:57:24 2021


`timescale 1ns/10ps

module pc (
    pass_input,
    out,
    reset,
    clk
);


input [31:0] pass_input;
output [31:0] out;
reg [31:0] out;
input reset;
input clk;




always @(posedge clk, posedge reset) begin: PC_PCBLOCK
    if (reset == 1) begin
        out <= 0;
    end
    else begin
        out <= pass_input;
    end
end

endmodule