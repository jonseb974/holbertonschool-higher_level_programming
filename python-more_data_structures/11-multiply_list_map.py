#!/usr/bin/python3
# 11. Multiply by using map


def multiply_list_map(my_list=[], number=0):
    return(list(map(lambda x: x * number, my_list)))
