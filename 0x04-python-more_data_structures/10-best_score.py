#!/usr/bin/python3

def best_score(a_dictionary):

    if a_dictionary is None:
        return None

    dict_keys_list = list(a_dictionary)

    if dict_keys_list == [] or dict_keys_list is None:
        return None

    max_key_name = dict_keys_list[0]
    max_key_val = a_dictionary.get(dict_keys_list[0])

    for i in dict_keys_list:
        if a_dictionary.get(i) > max_key_val:
            max_key_name = i
            max_key_val = a_dictionary.get(i)

    return max_key_name
