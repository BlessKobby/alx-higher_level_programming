#!/usr/bin/python3
# Function to print tuple with length of string #
def multiple_returns(sentence):
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
