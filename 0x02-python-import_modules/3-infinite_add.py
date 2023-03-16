#!/usr/bin/python3
import sys

sum = 0
length = len(sys.argv)

if __name__ == "__main__":
    for i in range(1, length):
        sum += int(sys.argv[i])
    print("{}".format(sum))
