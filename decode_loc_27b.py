#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""decode each sign from shorter bit code
    python script!"""

code_word = int(input("Code word (int numer 27 bit LSB): ")) # input number

grid = chr((code_word & 0b11111) + 65)
code_word = code_word >> 5

grid = chr((code_word & 0b11111) + 65) + grid
code_word = code_word >> 5

grid = str(int(code_word & 0b1111111)) + grid
if (code_word & 0b1111111) < 10:
    grid = '0' + grid
code_word = code_word >> 7

grid = chr((code_word & 0b11111) + 65) + grid
code_word = code_word >> 5

grid = chr((code_word & 0b11111) + 65) + grid

print("Grid: " + grid)
