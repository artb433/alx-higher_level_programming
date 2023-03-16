#!/usr/bin/python3

def new_in_list(my_list, idx, element):

    new_list = my_list[:]
    list_len = len(my_list) - 1

    if idx < 0 or idx > list_len:
        return new_list

    new_list[idx] = element
    return new_list
