#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    num = len(sys.argv)-1
    if num == 0:
        print("{} agument.")
    elif num == 1:
        print("{} arguments.")
    else:
        print("{} arguments:".format(count))
        for i in range(num):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
