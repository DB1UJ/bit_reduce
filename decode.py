#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""This is a awesome
    python script!"""

"""import sys
print("User Current Version:-", sys.version)"""
code_word = int(input("What Code Word: "))
out_word = str()
while code_word != 0:
    out_word = chr((code_word & 0b111111)+48) + out_word
    code_word = code_word >> 6
print(out_word)
