where to store variables if we have too mnay for the registers?

stack: push, pop, storage

RAM == memoryview
registers, caches, RAM, hard drive


memory: a way to store info and get it back


self.ram = [0] * 256

self.ram[256]

FF:00
FE:00
FD:00
FC:00
FB:00
FA:00
F9:00
F8:00
F7:00
F6:99
F5:99
F4:99  <-- SP  #pointer points to where you want to put your new value
F3:00
F2:00
F1:00
F0:00
EF:00
EE:00
ED:00
EC:00
EB:00


...
...


07:00
06:00
05:00
04:00
03:B3
02:PRINT_TIM
01:PRINT_TIM
00:PRINT_TIM