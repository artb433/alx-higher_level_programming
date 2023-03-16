#!/usr/bin/python3

def multiple_returns(sentence):

    str_len = len(sentence)

    if str_len == 0:
        str_char = None
    else:
        str_char = sentence[0]

    return (str_len, str_char)
