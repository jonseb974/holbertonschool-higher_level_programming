#!/usr/bin/python3
# 2. Unique addition


def uniq_add(my_list=[]):
    unique_numbers = list(set(my_list))
    result = 0
    for i in (unique_numbers):
        result += i
    return("Result: {:d}".format(result))
