#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    division_result = 0

    for i in range(0, list_length):

        try:
            int(my_list_1[i])
            int(my_list_2[i])

            float(my_list_1[i])
            float(my_list_2[i])

            division_result = my_list_1[i] / my_list_2[i]
            new_list.append(division_result)

        except (TypeError, ValueError):
            new_list.append(0)
            print("wrong type")

        except IndexError:
            new_list.append(0)
            print("out of range")

        except ZeroDivisionError:
            new_list.append(0)
            print("division by 0")

        finally:
            continue

    return new_list
