#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""encode and decode maidenhead grid square QTH locator as capital letter into 4 byte (only 26 bit used)
   @auther: DB1UJ"""

def encode_grid(grid):
    """
    Args:
      grid:string: maidenhead QTH locater [a-r][a-r][0-9][0-9][a-x][a-x]

    Returns:
      4 bytes contains 26 bit valid data with encoded grid locator
    """
    out_code_word = int(0)

    grid = grid.upper() # upper case to be save

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

    return out_code_word.to_bytes(length=4, byteorder='big')

def decode_grid(b_code_word:bytes):
    """
    Args:
      b_code_word:bytes: 4 bytes with 26 bit valid data LSB

    Returns:
      grid:str: upper case maidenhead QTH locater [A-R][A-R][0-9][0-9][A-X][A-X]
    """
    code_word = int.from_bytes(b_code_word, byteorder='big', signed=False)

    grid = chr((code_word & 0b11111) + 65) 
    code_word = code_word >> 5

    grid = chr((code_word & 0b11111) + 65) + grid
    code_word = code_word >> 7

    grid = str(int(code_word & 0b1111111)) + grid
    if (code_word & 0b1111111) < 10:
        grid = '0' + grid
    code_word = code_word >> 9

    int_val = int(code_word & 0b111111111)
    int_first = int_val // 18
    int_sec   = int_val % 18
    grid = chr(int(int_first)+65) + chr(int(int_sec)+65) + grid

    return grid

# manual test
grid = input("Grid: ")
print("Codeword (length 26 bit LSB in 4 byte bigendian): ",end='')
print(str(encode_grid(grid)))
print(decode_grid(encode_grid(grid)))

# automatic test
"""
def char_range(c1, c2):
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)
for a1 in char_range('A', 'R'):
    for a2 in char_range('A', 'R'):
        for x1 in range(0, 10):
            for x2 in range(0, 10):
                for b1 in char_range('A', 'X'):
                    for b2 in char_range('A', 'X'):
                        grid = a1 + a2 + str(x1) + str(x2) + b1 + b2
                        grid_decoded = decode_grid(encode_grid(grid))
                        assert grid == grid_decoded, "Error: " + grid_decoded + " should be: " + grid
"""
