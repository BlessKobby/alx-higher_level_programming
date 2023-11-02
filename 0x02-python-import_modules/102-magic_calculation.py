#!/usr/bin/python3

# A Python script that works exactly as a given byte-code. #

def magic_calculation(a, b):
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
            return c
        else:
            return sub(a, b)
