#!/usr/bin/python3

def complex_delete(a_dictionary, value):

    if a_dictionary is None:
        return

    key_val_get = 0
    dict_keys = list(a_dictionary)

    for i in dict_keys:
        key_val_get = a_dictionary.get(i)
        if key_val_get == value:
            del(a_dictionary[i])

    return a_dictionary
