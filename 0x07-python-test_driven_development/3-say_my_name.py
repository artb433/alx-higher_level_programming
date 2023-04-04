#!/usr/bin/python3

"""
   print my name

   Format: My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
       print names entered as parameters

       first_name and last_name must be strings
       else raise TypeError
    """

    if not (isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    elif not (isinstance(last_name, str)):
        raise TypeError("last_name must be a string")

    trim = str.strip
    print("My name is {} {}".format(trim(first_name), trim(last_name)))
