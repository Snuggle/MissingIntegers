#!/usr/bin/env python3
# https://app.codility.com/programmers/lessons/4-counting_elements/missing_integer/
# 88% Task Score; 100% Correctness; 75% Performance.

A = [1, 3, 6, 4, 1, 2]
B = [1, 2, 3]
C = [-1, -3]
D = [5, 6, 8, -2, -3]

# This function returns the smallest positive integer missing from a list.
# [1, 3, 6, 4, 1, 2]    >>> 5
# [1, 2, 3]             >>> 4
# [-1, -3]              >>> 1
# [5, 6, 8, -2, -3]     >>> 1
def solution(my_list):
    if max(my_list) < 1: # If no positive integers exist, return 1.
        return 1
    else:
        i = 1
        while i in my_list: # Start at 1 and count upwards until we get something that doesn't exist.
            i += 1
        return i # Return it.

[print(solution(X)) for X in [A, B, C, D]]
