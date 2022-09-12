#!/usr/bin/python3
# 5. Can you C me now?

def no_c(my_string):
    copy = [i for i in (my_string) if i != 'c' and i != 'C']
    return("".join(copy))
