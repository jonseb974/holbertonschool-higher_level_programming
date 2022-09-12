#!/usr/bin/python3
# 9. Find the max


def max_integer(my_list=[]):
    if my_list == "":
        return (None)

    maxVal = my_list[0]
    for x in my_list:
        if x > maxVal:
            maxVal = x
        print (maxVal)
