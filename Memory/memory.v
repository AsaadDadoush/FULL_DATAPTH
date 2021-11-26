// File: memory.v
// Generated by MyHDL 0.11
// Date: Fri Nov 26 20:27:04 2021


`timescale 1ns/10ps

module memory (
    addres,
    data_in,
    enable,
    clk,
    data_out,
    size
);


input [13:0] addres;
input [31:0] data_in;
input enable;
input clk;
output [31:0] data_out;
reg [31:0] data_out;
input [2:0] size;

reg [31:0] MainMemory [0:12287-1];



always @(posedge clk) begin: MEMORY_WRITE
    if ((enable == 1)) begin
        if ((size == 1)) begin
            MainMemory[addres] <= data_in[8-1:0];
        end
        if ((size == 2)) begin
            MainMemory[addres] <= data_in[8-1:0];
            MainMemory[(addres + 1)] <= data_in[16-1:9];
        end
        if ((size == 4)) begin
            MainMemory[addres] <= data_in[8-1:0];
            MainMemory[(addres + 1)] <= data_in[16-1:9];
            MainMemory[(addres + 2)] <= data_in[24-1:17];
            MainMemory[(addres + 3)] <= data_in[32-1:25];
        end
    end
    case (size)
        'h1: begin
            data_out <= MainMemory[addres];
        end
        'h2: begin
            data_out <= {8'b00000000, 8'b00000000, MainMemory[(addres + 1)], MainMemory[addres]};
        end
        'h4: begin
            data_out <= {MainMemory[(addres + 3)], MainMemory[(addres + 2)], MainMemory[(addres + 1)], MainMemory[addres]};
        end
    endcase
end

endmodule