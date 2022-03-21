#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""encode each sign as shorter bit code
    python script!"""

out_code_word = int(0)

grid = input("Grid: ").upper() # upper case to be save

int_first = ord(grid[0])-65 # -65 offset for 'A' become zero, utf8 table
int_sec   = ord(grid[1])-65 # -65 offset for 'A' become zero, utf8 table

int_val = (int_first * 18) + int_sec # encode for modulo devisioni, 2 numbers in 1

out_code_word = (int_val & 0b111111111) # only 9 bit LSB A - R * A - R is needed
out_code_word = out_code_word << 9 # shift 9 bit left having space next bits, letter A-R * A-R

int_val = int(grid[2:4]) # number string to number int, highest value 99
out_code_word = out_code_word | (int_val & 0b1111111) # using bit OR to add new value
out_code_word = out_code_word << 7 # shift 7 bit left having space next bits, letter A-X

int_val = ord(grid[4])-65 # -65 offset for 'A' become zero, utf8 table
out_code_word = out_code_word | (int_val & 0b11111) # using bit OR to add new value
out_code_word = out_code_word << 5 # shift 5 bit left having space next bits, letter A-X

int_val = ord(grid[5])-65 # -65 offset for 'A' become zero, utf8 table
out_code_word = out_code_word | (int_val & 0b11111) # using bit OR to add new value

print("Codeword (length 26 bit LSB): ",end='')
print(out_code_word) # length 26 bit LSB
