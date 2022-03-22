#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""decode each sign from shorter bit code
    python script!"""

code_word = int(input("Code word (int numer 26 bit LSB): ")) # input number

grid = chr((code_word & 0b11111) + 65) 
code_word = code_word >> 5

grid = chr((code_word & 0b11111) + 65) + grid
code_word = code_word >> 7

grid = str(int(code_word & 0b1111111)) + grid
if (code_word & 0b1111111) < 10:
    grid = '0' + grid
code_word = code_word >> 9

int_val = int(code_word & 0b111111111)
print(str(int_val))
if int_val > 17:
    int_first = int_val // 18
    int_sec   = int_val % 18
else:
    int_first = 0
    int_sec   = int_val
grid = chr(int(int_first)+65) + chr(int(int_sec)+65) + grid

print("Grid: " + grid)
