#!/usr/bin/python3
# Function returns higher key value #
def best_score(a_dictionary):
    return max(a_dictionary, key=a_dictionary.get) if a_dictionary else None
