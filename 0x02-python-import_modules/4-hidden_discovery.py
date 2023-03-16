#!/usr/bin/python3
import hidden_4

names = dir(hidden_4)

if __name__ == "__main__":
    for i in names:
        if i[0] != "_":
            print(i)
