#!/usr/bin/python3

def multiply_by_2(a_dictionary):

    new_dict = dict(a_dictionary)
    dict_keys_list = list(new_dict)

    for i in dict_keys_list:
        new_dict[i] = new_dict.get(i) * 2

    return new_dict
