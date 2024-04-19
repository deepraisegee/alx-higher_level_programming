#!/usr/bin/python3
import sys

argv = sys.argv
argv_len = len(argv) - 1

if __name__ == "__main__":
    if argv_len == 0:
        print("0 arguments.")
    elif argv_len == 1:
        print("{} argument:".format(argv_len))
    elif argv_len > 1:
        print("{} arguments:".format(argv_len))

    for i, v in enumerate(argv[1:], start=1):
        print("{}: {}".format(i, v))
