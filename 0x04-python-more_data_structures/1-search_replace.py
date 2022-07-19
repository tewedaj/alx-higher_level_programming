#!/usr/bin/python3
"""search for a value and replace it with in an array
"""
def search_replace(my_list, search, replace):
    return [replace if search == n else n for n in my_list]
