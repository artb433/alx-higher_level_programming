#!/usr/bin/python3

"""
   module for indenting text passed in as parameter to function: \
   text_indentation(text)
"""


def text_indentation(text):
    """
       print a newline after the occurence of delimeter in text
       delimeters: [".", "?", ":"]

       text must be a string; otherwise raise TypeError
       Ignore all whitespace after delimeter and print the next character
    """

    check_w_space = 0
    delim_list = [".", "?", ":"]

    if not (isinstance(text, str)):
        raise TypeError("text must be a string")

    for i in range(len(text)):
        for j in delim_list:
            if text[i] == j:
                print("{}\n".format(text[i]))

                i += 1
                check_w_space = 1
                break

        try:
            if check_w_space == 1 and text[i] == " ":
                continue
            else:
                check_w_space = 0

            print("{}".format(text[i]), end="")
        except IndexError:
            pass
