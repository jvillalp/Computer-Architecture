
# # file = open("print8.ls8", 'r')
# # lines= file.read()
# # print(lines)

# import sys
# if len(sys.argv) < 2:
#     print('please pass in a secod filename')
#     sys.exit()

# file_name = sys.argv[1]

# try:
#     with open(file_name) as file:
#         for line in file:
#             # print(line)
#             split_line = line.split("#")[0]
#             command = split_line.strip()
#             # print(command)

#             if command == ' ':
#                 continue
#             num = int(command, 2)
#             print(num)
#             # print(command)
#             # print(f'{num:8b} is {num}')

# except FileNotFoundError:
#     print(f'{sys.argv[0]}: {sys.argv[1]} file not found')

# # except Exception:
# #     print(file.closed)
