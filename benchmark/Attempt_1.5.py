#!/usr/bin/env python3
# https://app.codility.com/programmers/lessons/4-counting_elements/missing_integer/
# 55% Task Score; 100% Correctness; 0% Performance.

A = [1, 3, 6, 4, 1, 2]
B = [1, 2, 3]
C = [-1, -3]
D = [5, 6, 8, -2, -3]
import random
E = list(random.sample(range(9999999), 10))

# This function returns the smallest positive integer missing from a list.
# [1, 3, 6, 4, 1, 2]    >>> 5
# [1, 2, 3]             >>> 4
# [-1, -3]              >>> 1
# [5, 6, 8, -2, -3]     >>> 1
def solution(my_list):
    my_number = float("inf") # Assume my_number is infinate.

    for i in range(1, max(my_list)+1): # For 1, 2, 3, [...], max(my_list)
        if i not in my_list:          # If it doesn't exist in list,
            if i < my_number and i > 0: # And it's smaller than my_number
                my_number = i  # as well as being positive, replace my_number.
            
    if my_number == float("inf"): # If none found, max(my_list)+1
        my_number = max(my_list) + 1
        
    if my_number < 1: # If the smallest missing number is less than 1.
        my_number = 1
        
    return my_number

[print(solution(X)) for X in [A, B, C, D, E]]
