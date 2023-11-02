#!/usr/bin/python3

# A script to reveal the contents of a compiled stript #

if __name__ == "__main__":
    import hidden_4
    for name in dir(hidden_4):
        if name[0] != '_' and name[1] != '_':
            print(name)
