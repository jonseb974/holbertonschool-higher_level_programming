#!/usr/bin/python3
# 2-Replace element
def replace_in_list(my_list, idx, element):
    if idx < 0 and idx > (len(my_list)):
        return None
    if idx >= 0 and idx < (len(my_list)):
        my_list[idx] = element
    return (my_list)
