// File: mux_3to1.v
// Generated by MyHDL 0.11
// Date: Sat Nov 27 00:28:01 2021


`timescale 1ns/10ps

module mux_3to1 (
    i0,
    i1,
    i2,
    sel,
    out
);


input [31:0] i0;
input [31:0] i1;
input [31:0] i2;
input [1:0] sel;
output [31:0] out;
reg [31:0] out;




always @(i0, i2, sel, i1) begin: MUX_3TO1_MUX3TO1
    case (sel)
        'h0: begin
            out = i0;
        end
        'h1: begin
            out = i1;
        end
        'h2: begin
            out = i2;
        end
        default: begin
            out = i2;
        end
    endcase
end

endmodule