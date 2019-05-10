#!/usr/bin/env python3
# https://app.codility.com/programmers/lessons/4-counting_elements/missing_integer/
# 55% Task Score; 80% Correctness; 25% Performance.

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
	# Get maximum integer from list.
	my_list_max = max(my_list)

	# If maximum integer is smaller than 0, return {1}.
	if my_list_max < 0:
		missing_numbers = {1}
	else:
		# Make a dummy set ranging from 1 to max(my_list).
		# Find the difference of that set to the actual set.
		dummy_set = range(1, my_list_max)
		missing_numbers = set(dummy_set) - set(my_list)

	# If empty set, return maximum integer plus one.
	if missing_numbers == set():
		missing_numbers = {my_list_max+1}

    # Return smallest missing integer.
	return list(missing_numbers)[0]

[print(solution(X)) for X in [A, B, C, D]]
