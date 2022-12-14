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

    for i in ".?:":
        text = (i + "\n\n").join([line.strip(" ") for line in text.split(i)])
    print("{}".format(text), end="")
