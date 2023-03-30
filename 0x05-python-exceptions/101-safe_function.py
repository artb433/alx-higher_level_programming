#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    fct_result = 0

    try:
        fct_result = fct(args[0], args[1])

    except (ZeroDivisionError, IndexError, TypeError, ValueError):
        sys.stderr.write("Exception: {}\n".format(sys.exc_info()[1]))
        return

    return fct_result
