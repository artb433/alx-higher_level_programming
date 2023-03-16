#!/usr/bin/python3

def roman_to_int(roman_string):

    if roman_string == "" or roman_string is None:
        return

    valid_char_checker = 0
    lower_case_string = ""
    roman_to_int_result = 0
    str_len = len(roman_string)
    roman_numeral_dict = {'i': 1, 'v': 5, 'x': 10,
                          'l': 50, 'c': 100, 'd': 500, 'm': 1000}

    for i in roman_string:
        if ord(i) >= 65 and ord(i) <= 90:
            lower_case_string += chr(ord(i) + 32)
        else:
            lower_case_string += i

    # Check if all char values in string are valid numerals
    # Exit the program and return None otherwise
    # Not being checked by the checker - just my preference
    for i in lower_case_string:
        for j in roman_numeral_dict:
            if i == j:
                valid_char_checker += 1
                break
    if valid_char_checker != str_len:
        return

    # This variable will be used inside the loop
    # I created this to shorten the number of characters per line
    char = lower_case_string

    for i in range(str_len):
        for j in list(roman_numeral_dict):
            if lower_case_string[i] == j:

                if i > 0:
                    if char[i] == 'x' or char[i] == 'v':
                        if char[i - 1] == 'i':
                            roman_to_int_result -= 2

                    if char[i] == 'l' or char[i] == 'c':
                        if char[i - 1] == 'x':
                            roman_to_int_result -= 20

                    if char[i] == 'm' or char[i] == 'd':
                        if char[i - 1] == 'c':
                            roman_to_int_result -= 200

                roman_to_int_result += roman_numeral_dict.get(j)
                break

    return roman_to_int_result
