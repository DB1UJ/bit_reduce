#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""encode each sign as shorter bit code
    python script!"""

out_code_word = int(0)

grid = input("Grid: ").upper() # upper case to be save

int_val = ord(grid[0])-65 # -65 offset for 'A' become zero, utf8 table
out_code_word = (int_val & 0b11111) # only 5 bit LSB A - R is needed
out_code_word = out_code_word << 5 # shift 5 bit left having space next bits, letter A-R

int_val = ord(grid[1])-65 # -65 offset for 'A' become zero, utf8 table
out_code_word = out_code_word | (int_val & 0b11111) # using bit OR to add new value
out_code_word = out_code_word << 7 # shift 7 bit left having space next bits, unsigned number < 100

int_val = int(grid[2:4]) # number string to number int, highest value 99
out_code_word = out_code_word | (int_val & 0b1111111) # using bit OR to add new value
out_code_word = out_code_word << 5 # shift 5 bit left having space next bits, letter A-X

int_val = ord(grid[4])-65 # -65 offset for 'A' become zero, utf8 table
out_code_word = out_code_word | (int_val & 0b11111) # using bit OR to add new value
out_code_word = out_code_word << 5 # shift 5 bit left having space next bits, letter A-X

int_val = ord(grid[5])-65 # -65 offset for 'A' become zero, utf8 table
out_code_word = out_code_word | (int_val & 0b11111) # using bit OR to add new value

print("Codeword (length 27 bit): ",end='')
print(out_code_word) # length 27 bit LSB
