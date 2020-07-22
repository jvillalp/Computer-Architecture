import sys

PRINT_TIM = 0b01
HALT = 0b10 #2
PRINT_NUM = 0b11 #opcode 3
SAVE = 0b100 
PRINT_REG = 0b101 # opcode 5
ADD = 0b110 # registers[2] = registers[2] + registers[3]


#programs stored in RAM
#save the number 99 into R2
#print whatever is inside R2
# memory = [
#     PRINT_TIM,
#     PRINT_TIM,
#     PRINT_NUM,
#     42,
#     SAVE, #regist to put it in
#     2, #num to save
#     99, 
#     SAVE,
#     3, #register to save in
#     1, #register to save
#     ADD,
#     2, #register to look at in save stuff in
#     3, #other register to look at
#     PRINT_REG,
#     2, #register we want to look at
#     HALT,

# ] #rep the RAM, all commands numbers


memory = [0] * 256

def load_memory(file_name):
    try:
        address = 0
        with open(file_name) as file:
            for line in file:
                # print(line)
                split_line = line.split("#")[0]
                command = split_line.strip()
                # print(command)

                if command == ' ':
                    continue
                instruction = int(command, 2)
                # print(num )
                # print(command)
                # print(f'{num:8b} is {num}')
                memory[address] = instruction
                address +=1


    except FileNotFoundError:
        print(f'{sys.argv[0]}: {sys.argv[1]} file not found')

if len(sys.argv) < 2:
    print('please pass in a secod filename')
    sys.exit()

file_name = sys.argv[1]
load_memory(file_name)
# write a program to pull earch command out of memory and execute

# we can loop over it!

#register aka memory
registers = [0] * 8
#[0,99,0,0,0,0,0,0]
#R0 - R7


pc = 0 # program counter
running = True
while running:
    command = memory[pc]

    if command == PRINT_TIM:
        print("Tim!")
    if command == HALT:
        running = False

    if command == PRINT_NUM:
        num_to_print = memory[pc +1]
        print(num_to_print)
        pc +=1

    if command == SAVE:
        reg = pc + 1
        num_to_save = pc + 2
        registers[reg] = num_to_save
        pc +=2

    if command == PRINT_REG:
        reg_index = memory[pc +1]
        print(registers[reg_index])
        pc += 1

    if command == ADD:
        first_reg = memory[pc +1]
        sec_reg = memory[pc +2]
        registers[first_reg] = registers[first_reg]  + registers[sec_reg]
        pc +=2

    pc += 1
