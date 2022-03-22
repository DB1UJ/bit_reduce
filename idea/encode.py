#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""This is a awesome
    python script!"""

out_code_word = int(0)
in_str = input("String: ").upper() # upper to be save
for x in in_str:
    int_val = ord(x)-48 # -48 reduce bits, begin with first number utf8 table
    out_code_word = out_code_word << 6 # shift left 6 bit, making space for a new char
    out_code_word = out_code_word | (int_val & 0b111111) # bit OR adds the new char, masked with AND 0b111111
print("Code word (6bit each char): ",end='')
print(out_code_word)
