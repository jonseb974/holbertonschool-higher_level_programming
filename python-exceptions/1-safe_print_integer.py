#!/usr/bin/python3
# 1. Safe printing of an integers list


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return(True)
    except(TypeError, ValueError):
        return(False)
