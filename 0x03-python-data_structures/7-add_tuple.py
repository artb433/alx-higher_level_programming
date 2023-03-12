#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    tuple_a = list(tuple_a)
    tuple_b = list(tuple_b)

    idx = 0
    new_tuple = []
    len_tuple_a = len(tuple_a)
    len_tuple_b = len(tuple_b)

    while len_tuple_a < 3:
        tuple_a.append(0)
        len_tuple_a += 1

    while len_tuple_b < 3:
        tuple_b.append(0)
        len_tuple_b += 1

    if len_tuple_a > 2:
        len_tuple_a = 2

    if len_tuple_b > 2:
        len_tuple_b = 2

    for i in range(0, len_tuple_a):
        for j in range(0, len_tuple_b):
            if j == i:
                new_tuple.append(tuple_a[i] + tuple_b[j])

    return tuple(new_tuple)
