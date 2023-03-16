#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):

    sort_dict_list = list(sorted(a_dictionary))

    for i in sort_dict_list:
        print("{}: {}".format(i, a_dictionary.get(i)))
