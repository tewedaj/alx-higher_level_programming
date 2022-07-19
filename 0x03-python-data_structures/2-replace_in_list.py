#!/usr/bin/python3
"""
this is a good way to replace a value in a list using
the index given in the second parameter
"""
def replace_in_list(my_list, idx, element):
    if (0 <= idx < len(my_list)):
        my_list[idx] = element
    return my_list
