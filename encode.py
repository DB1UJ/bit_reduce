#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""This is a awesome
    python script!"""

"""import sys
print("User Current Version:-", sys.version)"""
from ctypes import c_uint32 as uint
out_code_word = int(0)
grid = input("What Grid: ").upper() # upper damit wir save sind und es einheitlich ist
print(grid)
for x in grid:
    print(x,end='')
    int_val = ord(x)-48 # -48 weil es der offset in der ASCII Tabelle ist zur ersten Ziffer
    print(int_val)
    out_code_word = out_code_word << 6 # um 6 bit stellen nach links verschieben, um Platz zu machen
    out_code_word = out_code_word | (int_val & 0b111111) # OR fügt es hinzu + zur Sicherheit maskieren mit 0b111111
    print("Codeword: ",end='')
    print(out_code_word)
