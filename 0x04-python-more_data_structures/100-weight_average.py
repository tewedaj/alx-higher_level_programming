#!/usr/bin/python3
""" find the average from datas found in a list
"""
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    return sum([x*y for (x, y) in my_list]) / sum([y for (x, y) in my_list])
