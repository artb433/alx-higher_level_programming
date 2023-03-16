#!/usr/bin/python3

def weight_average(my_list=[]):

    if my_list == [] or my_list is None:
        return 0

    tuple_list = list(my_list)
    list_len = len(my_list)

    weight_sum = my_list[0][1]
    score_weight_sum = 0
    score_weight_mul = 1

    for i in range(0, list_len):
        for j in my_list[i]:
            score_weight_mul *= j

        score_weight_sum += score_weight_mul
        score_weight_mul = 1

    for i in range(0, list_len):
        for j in range(0, 2):
            if j == 1 and i > 0:
                weight_sum += my_list[i][j]

    return score_weight_sum / weight_sum
