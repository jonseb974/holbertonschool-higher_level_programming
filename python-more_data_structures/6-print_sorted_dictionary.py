#!/usr/bin/python3
# 6. Print sorted dictionary

def print_sorted_dictionary(a_dictionary):
    for elem in sorted(a_dictionary.keys()):
        print("{:s}:{}".format(elem, a_dictionary[elem]))
