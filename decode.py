#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""This is a awesome
    python script!"""

code_word = int(input("Code word: "))
out_word = str()
while code_word != 0:
    out_word = chr((code_word & 0b111111)+48) + out_word
    code_word = code_word >> 6
print(out_word)
