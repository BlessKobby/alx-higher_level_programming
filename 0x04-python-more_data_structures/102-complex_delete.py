#!/usr/bin/python3
# Functions deletes key with a specific value #
def complex_delete(a_dictionary, value):
    for key in list(a_dictionary):
        if a_dictionary[key] == value:
            del a_dictionary[key]
    return a_dictionary
