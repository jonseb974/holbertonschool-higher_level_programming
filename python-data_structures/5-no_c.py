#!/usr/bin/python3
# 5. Can you C me now?

def no_c(my_string):
    print(my_string.translate({ord('c') and ('C'): None}))
