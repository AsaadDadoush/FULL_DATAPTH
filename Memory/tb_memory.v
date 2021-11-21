module tb_memory;

reg [13:0] addres;
reg [31:0] data_in;
reg enable;
reg clk;
wire [31:0] data_out;
reg [2:0] size;

initial begin
    $from_myhdl(
        addres,
        data_in,
        enable,
        clk,
        size
    );
    $to_myhdl(
        data_out
    );
end

memory dut(
    addres,
    data_in,
    enable,
    clk,
    data_out,
    size
);

endmodule
