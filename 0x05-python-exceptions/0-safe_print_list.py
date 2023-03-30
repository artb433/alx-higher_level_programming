#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    print_count = 0
    try:
        for i in range(x):
            print_count += 1
            print("{:d}".format(my_list[i]), end="")

    except IndexError:
        print_count -= 1
        pass

    finally:
        print()

    return print_count
