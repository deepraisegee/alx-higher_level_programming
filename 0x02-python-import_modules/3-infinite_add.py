#!/usr/bin/python3
import sys

total = 0

if __name__ == "__main__":
    for i in sys.argv[1:]:
        total += int(i)
    print(total)
