#!/usr/bin/python3

"""
Write a function that prints a text with 2 new lines
after each of these characters: ., ? and :
Prototype: def text_indentation(text):
text must be a string, otherwise raise a TypeError exception
with the message text must be a string
There should be no space at the beginning or at the end of each printed line
"""


def text_indentation(text):
    """ Print two new lines after . : or ? """
    if type(text) is not str:
        raise TypeError("text must be a string")
    if not text:
        raise TypeError("text_indentation() missing 1 required \
                positional argument: 'text'")
    i = 0
    new_text = text.replace(". ", ".")
    new_text = new_text.replace("? ", "?")
    new_text = new_text.replace(": ", ":")
    while i < len(new_text):
        if new_text[i] in ".?:":
            print(new_text[i], end="\n\n")
            i += 1
        else:
            print(new_text[i], end="")
            i += 1
