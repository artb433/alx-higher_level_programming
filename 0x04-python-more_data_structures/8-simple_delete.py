#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):

    if key == "":
        return a_dictionary

    check_key = 0
    dict_keys_list = list(a_dictionary)

    for i in dict_keys_list:
        if key == i:
            check_key = 1
            break

    if check_key == 0:
        return a_dictionary

    del(a_dictionary[key])
    return a_dictionary
