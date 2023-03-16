#!/usr/bin/python3
import sys

length = len(sys.argv)

if __name__ == "__main__":
    if length == 1:
        print("{} arguments.".format(length - 1))
    elif length == 2:
        print("{} argument:".format(length - 1))
    elif length > 1:
        print("{} arguments:".format(length - 1))

    if length > 1:
        for i in range(1, length):
            print("{}: {}".format(i, sys.argv[i]))
