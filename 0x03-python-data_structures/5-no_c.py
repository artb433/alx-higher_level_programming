#!/usr/bin/python3

def no_c(my_string):

    new_string = ""

    for i in my_string:
        if i != chr(99) and i != chr(67):
            new_string = new_string + i

    return new_string
