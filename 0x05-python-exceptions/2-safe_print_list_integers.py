#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    print_counter = 0

    for i in range(x):
        try:
            print_counter += 1
            my_list[i] = int(my_list[i])

        except (ValueError, TypeError):
            print_counter -= 1
            continue

        else:
            print("{:d}".format(my_list[i]), end="")

    print()
    return print_counter
