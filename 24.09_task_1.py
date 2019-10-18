#!/usr/bin/python3.6

'''Given an array of integers.

Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.

If the input array is empty or null, return an empty array.'''

#my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]

def check(val):
	positive = [item for item in val if item > 0]
	negative = [item for item in val if item < 0]
	return len(positive), sum(negative)
print(list(check(my_list)))