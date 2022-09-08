#!/usr/bin/python3
for digit in range(0, 10):
    for digit_b in range(digit + 1, 10):
        if digit == 8 and digit_b == 9:
            print("{}{}".format(digit, digit_b))
        else:
            print("{}{}".format(digit, digit_b), end=", ")
