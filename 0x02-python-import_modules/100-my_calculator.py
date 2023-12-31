#!/usr/bin/python3

# Script to build my personal calculator #

if __name__ == "__main__":
    import sys

    nargs = len(sys.argv) - 1
    if nargs != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>", end="\n")
        sys.exit(1)

    op = sys.argv[2]
    if op != '+' and op != '-' and op != '*' and op != '/':
        print("Unknown operator. Available operators: +, -, * and /", end="\n")
        sys.exit(1)

    from calculator_1 import add, sub, mul, div
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if op == '+':
        print("{} + {} = {}".format(a, b, add(a, b)), end="\n")
    elif op == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)), end="\n")
    elif op == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)), end="\n")
    else:
        print("{} / {} = {}".format(a, b, div(a, b)), end="\n")
