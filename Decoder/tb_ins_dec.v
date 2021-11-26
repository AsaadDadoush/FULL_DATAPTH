module tb_ins_dec;

reg [31:0] data_in;
wire [6:0] opcode;
wire [4:0] rd;
wire [2:0] func3;
wire [4:0] rs1;
wire [4:0] rs2;
wire [6:0] func7;
wire [11:0] immI;
wire [11:0] immS;
wire [11:0] immB;
wire [19:0] immU;
wire [19:0] immJ;

initial begin
    $from_myhdl(
        data_in
    );
    $to_myhdl(
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
end

ins_dec dut(
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

endmodule
