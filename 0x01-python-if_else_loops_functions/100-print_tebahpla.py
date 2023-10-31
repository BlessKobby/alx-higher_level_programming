#!/usr/bin/python3
for character_code in range(ord('z'), ord('A') - 1, -1):
    if character_code % 2 == 0:
        print(chr(character_code), end="")
