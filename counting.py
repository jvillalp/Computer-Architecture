"""
decimal (base 10)
0-9

1
2
3
...
9 (out of symbols)

10
20
30
...
99(out of symbols, looking for spot)
100 (add spot - now with 3 spots)

IV
V
VI
VII
VIII
IX
X
VII
CLX
(roman numerals are difficult to keep track of)

hexadecimals (base 16)
0
...
9
A (10)
B (11)
C (12)
D (13)
E (14)
F (15)
10 or 0x10 (16)

11 (17)
12
13
14
15
16
17
18
19
1A (26)
1B
1C
...
1F (15 + 16)(31)
20
21
22
23
9F
A0
AA
AB
AF
B0

Binary
01

0
1
10
11
100
101
110
111
1000
1001
1010
1011
1100


0x73 = (16 * 7)+ 3 = 115

0x3F = (3 * 16) + 15 = 63

54 -> hex 
54/ 16 = 3.xx
54 - 48 = 6
0x36

0xE3 --> dec
(14 * 16) + 3 = 227

0b11001010 --> dec
2 + 8 + 64 + 128 = 202

0b1010 1100 --> hex
8 bits
1
11
111
0b1111
F

0xAC --> dec
(10 * 16) + 12 = 160 +12 = 172

dec -> hex -> binary

0b1111 1111 --> decimal
0xFF  (each F is 15)

0xff ff ff  (color white)

0b01

 11
3/2 =1, remainder 1
1/2 --> remainder 1

    100
4/2 --> 2, remainder 0
2/2 = 1, reminder 0
1/2 -> 1


    1111
15/2 =7, remainder 1
7/2 = 3 remainder 2
3/2 = 1, remainder 1
1/2 = 1
"""

num = 1234
print(1234)
hex(1234)

"""
>>> s = "1010101"
>>> int(s)
1010101
>>> 
>>> int(s,2)
85
>>> 
>>> int("E3",16)
227
>>> 
"""