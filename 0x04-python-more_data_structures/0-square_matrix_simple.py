#!/usr/bin/python3
""" find the square matrix
"""
def square_matrix_simple(matrix=[]):
    squared = []
    for line in matrix:
        squared.append([c**2 for c in line])
    return squared
