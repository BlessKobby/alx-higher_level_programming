#!/usr/bin/python3
# This script is to print each integer on a list unto a new line. #
def print_list_integer(my_list=[]):
    for num in range(len(my_list)):
        print("{:d}".format(my_list[num]))
