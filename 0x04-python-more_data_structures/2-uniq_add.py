#!/usr/bin/python3

def uniq_add(my_list=[]):

    list_sum = 0

    if my_list == [] or my_list is None:
        return list_sum

    for i in set(my_list):
        list_sum += int(i)

    return list_sum
