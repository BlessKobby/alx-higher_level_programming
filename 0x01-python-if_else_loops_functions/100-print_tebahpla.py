#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    char = chr(i)
    if i % 2 == 1:
        char = chr(i - ord('a') + ord('A'))
    print("{}".format(char), end='')
