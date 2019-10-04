#!/usr/bin/python3
"""
text_indentation - identate a text and identify if text contain?
and print a new space
>>> text_indentation(text)
"""

def text_indentation(text):
    """
    text_indentation - construct the string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    n_txt = text.replace('?', '?\n\n')
    n_txt = n_txt.replace('.', '.\n\n')
    n_txt = n_txt.replace(':', ':\n\n')

    print("\n".join([li.strip() for li in n_txt.split("\n")]), end="")
