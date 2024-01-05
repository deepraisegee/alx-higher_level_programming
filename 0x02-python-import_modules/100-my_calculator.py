#!/usr/bin/python3
import sys

from calculator_1 import add, sub, mul, div

argv = sys.argv
args_len = len(argv) - 1

operators = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

if args_len != 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)

if argv[2] not in operators:
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)

arg1 = int(argv[1])
operator = argv[2]
arg2 = int(argv[3])

if __name__ == "__main__":
    print(
      "{} {} {} = {}".format(
                    arg1,
                    operator,
                    arg2,
                    operators[operator](arg1, arg2)
                )
    )
