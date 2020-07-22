"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.registers = [0] * 8
        self.pc = 0
        # self.running = True

    def ram_read(self, mar): # mar = address
        return self.ram[mar]

    def ram_write(self, mar, mdr): #mdr value
        self.ram[mar] = mdr

        #might need initial value of the stack pointer
        #add ram_read here?
        #each memory slot has a memory and a value

    def load(self, file_name):
        """Load a program into memory."""

        address = 0

        
        # For now, we've just hardcoded a program:

        # program = [
        #     # From print8.ls8
        #     0b10000010, # LDI R0,8
        #     0b00000000,
        #     0b00001000,
        #     0b01000111, # PRN R0
        #     0b00000000,
        #     0b00000001, # HLT
        # ]

        # for instruction in program:
        #     self.ram[address] = instruction
        #     address += 1

        program =[]

        # file_name = sys.argv[1]
        # load_memory(file_name)

        # def load_memory(file_name):
            # try:
        with open(file_name) as file:
            for line in file:
                split_line = line.split("#")[0]
                command = split_line.strip()

                if command == '':
                    continue
                instructions = int(command,2)
                program.append(instructions)

        for instruction in program:
            self.ram[address] = instruction
            address += 1
                        

        #     except FileNotFoundError:
        #         print(f'{sys.argv[0]}: {sys.argv[1]} file not found')
        #         sys.exit()

        # if len(sys.argv) < 2:
        #     print('please pass in a secod filename')
        #     sys.exit()

    


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        elif op == "MUL":
            self.reg[reg_a] *= self.reg[reg_b]
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        HLT = 0b00000001
        LDI = 0b10000010
        PRN = 0b01000111
        MUL = 0b10100010
        running = True

        while True:
            instruction = self.ram_read(self.pc)
            reg_a = self.ram_read(self.pc + 1)
            reg_b = self.ram_read(self.pc +2)

            if instruction == HLT:
                running = False
                self.pc += 1
                sys.exit()
            elif instruction == LDI:
                self.registers[reg_a] = reg_b
                self.pc += 3
            elif instruction == PRN:
                print(self.registers[reg_a])
                self.pc +=2
            elif instruction == MUL:
                self.registers[reg_a] *= self.registers[reg_b]
                self.pc +=3
            else:
                print(f'this is not valid')
                running = False
                sys.exit()
            

