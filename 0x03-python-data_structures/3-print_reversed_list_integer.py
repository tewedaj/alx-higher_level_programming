#!/usr/bin/python3
"""
log a list but reverted
"""
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return
    for i in reversed(my_list):
        print("{:d}".format(i))
