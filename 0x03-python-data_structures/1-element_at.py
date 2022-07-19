#!/usr/bin/python3
""" this is a great way to find the index of a value with in
an array
"""
def element_at(my_list, idx):
    return my_list[idx] if (0 <= idx < len(my_list)) else None
