// File: alu.v
// Generated by MyHDL 0.11
// Date: Fri Nov 26 22:31:53 2021


`timescale 1ns/10ps

module alu (
    a,
    b,
    sel,
    out
);


input [31:0] a;
input [31:0] b;
input [4:0] sel;
output [31:0] out;
reg [31:0] out;




always @(b, a, sel) begin: ALU_ALU
    case (sel)
        'h0: begin
            out = ($signed(a) + $signed(b));
        end
        'h1: begin
            out = ($signed(a) * $signed(b));
        end
        'h2: begin
            out = ($signed(a) / $signed(b));
        end
        'h3: begin
            out = ($signed(a) & $signed(b));
        end
        'h4: begin
            out = ($signed(a) | $signed(b));
        end
        'h5: begin
            out = ($signed(a) ^ $signed(b));
        end
        'h6: begin
            out = ($signed(a) << $signed(b[5-1:0]));
        end
        'h7: begin
            out = $signed($signed(a) >>> $signed(b[5-1:0]));
        end
        'h8: begin
            if (($signed(a) == $signed(b))) begin
                out = 1;
            end
            else begin
                out = 0;
            end
        end
        'h9: begin
            if (($signed(a) != $signed(b))) begin
                out = 1;
            end
            else begin
                out = 0;
            end
        end
        'ha: begin
            if (($signed(a) < $signed(b))) begin
                out = 1;
            end
            else begin
                out = 0;
            end
        end
        'hb: begin
            if (($signed(a) < b[32-1:0])) begin
                out = 1;
            end
            else begin
                out = 0;
            end
        end
        'hc: begin
            if (($signed(a) <= $signed(b))) begin
                out = 1;
            end
            else begin
                out = 0;
            end
        end
        'hd: begin
            out = $signed($signed(a) >>> $signed(b[5-1:0]));
        end
        'he: begin
            if (($signed(a) < b[32-1:0])) begin
                out = 1;
            end
            else begin
                out = 0;
            end
        end
        'hf: begin
            if (($signed(a) > b[32-1:0])) begin
                out = 1;
            end
            else begin
                out = 0;
            end
        end
        default: begin
            out = ($signed(a) % $signed(b));
        end
    endcase
end

endmodule
