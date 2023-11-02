#!/usr/bin/python3

# A Python script that works exactly as a given byte-code. #

from magic_calculation_102 import add, sub


def magic_calculation(a, b):
    add_func = add
    sub_func = sub

    if a < b:
        c = add_func(a, b)
        for i in range(4, 6):
            c = add_func(c, i)
        return c
    else:
        return sub_func(a, b)
