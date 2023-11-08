#!/usr/bin/python3
# Function multiplies keys in a dictionary without looping #
def multiply_list_map(my_list=[], number=0):
    return list(map(lambda x: x * number, my_list))
