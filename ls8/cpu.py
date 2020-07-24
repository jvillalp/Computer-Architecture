"""CPU functionality."""
"""
1. The CALL instruction doesn't allow you to pass any arguments. 
What are some ways to effectively get arguments to a subroutine?

    - CPUs use a stack to store the return address so we know where to go when we hit the RET instruction
    - CALL will push the address off the instruction after its on the stack
    - will move the PC to the subroutine address
    - RET will pop the return address off the stack and will store it in the PC
(EXAMPLE)
    00: LDI R0,15
    03: LDI R1,0B  # Holds the address of the subroutine
    06: CALL R1
    08: PRN R0
    0A: HLT

    0B: ADD R0,10  # Subroutine!
    0E: RET
    - EXPLAINED:
        - go down the line when in call, will hold address of 0b, 
        - go there and add 10 to R0, get to RET and go to next address after PRN R0) 
        - and then return to HLT


2. What's the result of bitwise-AND between 0b110 and 0b011?

    - 0b010

3. Convert the 8-bit binary number 0bXXXXXXXX (PM's choice) to hex.

    - create groups of 4 bits(0b 0000 0000)
    - 0011 1110
    - 3 14
    - 3E


"""
import sys
# print(sys.argv[0])

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.pc = 0
        self.ram = [0] * 256  # hold 256 bytes of memory 8 bit 2^8 = 256
        self.registers = [0] * 8  # hold 8 general-purpose registerss
        self.sp = 7  # stack pointer
        self.fl = 0b00000000  # flags status can change based on operands given to cmp opcode
        #self.fl = [0,0,0]

    def ram_read(self, mar): # mar = address
        return self.ram[mar]

    def ram_write(self, mar, mdr): #mdr value
        self.ram[mar] = mdr

    def load(self):
        """Load a program into memory."""
        address = 0

        file_name = sys.argv[1]

        with open(file_name) as file:
            for line in file:
                command = line.split("#")[0].strip()
                if command == '':
                    continue
                instructions = int(command,2)
                self.ram[address] = instructions
                address += 1

        # program = []

        # with open(sys.argv[1]) as lines:
        #     for line in lines:
        #         value = line.split('#')[0].strip()
        #         if value == '':
        #             continue
        #         v = int(value, 2)
        #         program.append(v)

    def alu(self, op, registers_a, registers_b):
        """ALU operations."""

        if op == "ADD":
            self.registers[registers_a] += self.registers[registers_b]
        #elif op == "SUB": etc
        elif op == "MUL":
            self.registers[registers_a] *= self.registers[registers_b]
        # set E flag to 1 if equal
        elif op == "CMP":
            if self.registers[registers_a] < self.registers[registers_b]:
                self.fl = 0
                # self.fl[0] = 1
                # self.fl[1] = 0
                # self.fl[2] = 0
            if self.registers[registers_a] > self.registers[registers_b]:
                self.fl = 0
                # self.fl[0] = 0
                # self.fl[1] = 1
                # self.fl[2] = 0
            if self.registers[registers_a] == self.registers[registers_b]:
                self.fl = 1
                # self.fl[0] = 0
                # self.fl[1] = 0
                # self.fl[2] = 1
        elif op == "AND":
            pass
        elif op == "OR":
            pass
        elif op =="XOR":
            pass
        elif op == "NOT":
            pass
        elif op == "SHL":
            pass
        elif op == "SHR":
            pass
        elif op =="MOD":
            pass
        
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
            print(" %02X" % self.registers[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        LDI = 0b10000010  # Set the value of a register to an integer.
        PRN = 0b01000111 
        HLT = 0b00000001  # stop the CPU
        ADD = 0b10100000
        MUL = 0b10100010
        PUSH = 0b01000101  # Push the value in the given register on stack
        POP = 0b01000110   # Pop the value at the top of the stack inside the given register
        CALL = 0b01010000
        RET = 0b00010001
        running = True

        CMP = 0b10100111
        
        # if A < B set L flad to 1
        # if A > B set G flad to 1

        JMP = 0b01010100
        # jump to address stored in given registers
        # set PC to address stored in given registers

        JEQ = 0b01010101
        #if E(equal) flag is true jump to address stored in the given registers

        JNE = 0b01010110
        # if E flag is clear (0), jump to address stored in the given registers

        while running:
            instruction = self.ram_read(self.pc)
            oper_a = self.ram_read(self.pc + 1)
            oper_b = self.ram_read(self.pc + 2)

            if instruction == LDI:
                # set value of a registers to an integer
                self.registers[oper_a] = oper_b
                self.pc += 3

            elif instruction == PRN:
                # Print numeric value stored in a given registers
                print(self.registers[oper_a])
                self.pc += 2

            elif instruction == ADD:
                self.alu("ADD", oper_a, oper_b)
                self.pc += 3

            elif instruction == MUL:
                # * the values in two registers and the result in registers A.
                self.alu("MUL", oper_a, oper_b)
                self.pc += 3

            elif instruction == PUSH:
                # decrease the SP
                self.registers[self.sp] -= 1
                # store value in memory at SP & push the value in the given register on the stack
                self.ram[self.registers[self.sp]] = self.registers[oper_a]
                self.pc += 2

            elif instruction == POP:
                # store value in memeroy at SP & get value out of the registers
                self.registers[oper_a] = self.ram[self.registers[self.sp]]
                # increase the SP
                self.registers[self.sp] += 1
                self.pc += 2

            elif instruction == CALL:
                # push if it is on the stack
                self.registers[self.sp] -= 1
                self.ram[self.registers[self.sp]] = self.pc + 2
                # set the PC to the subroutine address
                self.pc = self.registers[oper_a]

            elif instruction == RET:
                # pop the return address off the stack
                top_stack = self.registers[self.sp]
                self.registers[self.sp] += 1
                # store in PC
                self.pc = self.ram[top_stack]

            elif instruction == CMP:
                self.alu("CMP", oper_a, oper_b)
                self.pc +=3

            elif instruction == JEQ:
                if self.fl == 1:
                    self.pc = self.registers[self.ram_read(self.pc+1)]
                else:
                    self.pc +=2

            elif instruction == JNE:
                if self.fl == 0:
                    self.pc = self.registers[self.ram_read(self.pc + 1)]
                else:
                    self.pc +=2

            elif instruction == JMP:
                self.pc = self.registers[self.ram_read(self.pc + 1)]

            elif instruction == HLT:
                # stop the CPU 
                running = False  # get out of while loop

            else:
                print(
                    F" unknown instruction {instruction} at address {self.pc}")
                sys.exit()  #stops the python program
            

