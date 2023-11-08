#!/usr/bin/python3
# Function returns multiples of a dictionary #
def multiply_by_2(a_dictionary):
    new_dic = {}
    for i in a_dictionary:
        new_dic[i] = a_dictionary[i] * 2
    return new_dic
