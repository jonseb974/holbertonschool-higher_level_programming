#!/usr/bin/python3
# 5-text_indentation.py
"""
function that prints a text
with 2 new lines after each
of these characters: ., ? and :
"""


def text_indentation(text):
    """print text"""
    if type(text) is not str:
        raise TypeError("text must be a string")

    for delim in ".?:":
        text = (delim + "\n\n").join(
                [line.strio("") for line in text.split(delim)])
    print("{}".format(text), end="")
