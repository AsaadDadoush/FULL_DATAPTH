module tb_registers;

reg [4:0] rs1;
reg [4:0] rs2;
reg [4:0] rd;
wire [31:0] rs1_out;
wire [31:0] rs2_out;
reg clk;
reg enable;
reg [31:0] data;

initial begin
    $from_myhdl(
        rs1,
        rs2,
        rd,
        clk,
        enable,
        data
    );
    $to_myhdl(
        rs1_out,
        rs2_out
    );
end

registers dut(
    rs1,
    rs2,
    rd,
    rs1_out,
    rs2_out,
    clk,
    enable,
    data
);

endmodule
