#!/usr/bin/python3

"""
   module containing a simple function that adds two values and returns result

   def add_integer(a, b) - module for performing adddition operation
"""


def add_integer(a, b=98):
    """
       Compute and return the value of (a + b)
    """

    try:
        non_int_msg = ""

        if not (isinstance(a, int) or isinstance(a, float)):
            non_int_msg = "a must be an integer"
        elif not (isinstance(b, int) or isinstance(b, float)):
            non_int_msg = "b must be an integer"

        a = int(a)
        b = int(b)

    except (TypeError, ValueError):
        raise TypeError(non_int_msg)

    return a + b
