#!/usr/bin/python3

def remove_char_at(str, n):
    new_string = ""
    count = 0

    for i in str:
        if count != n:
            new_string += i

        count += 1

    return new_string
