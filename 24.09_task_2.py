#!/usr/bin/python3.6

'''In this kata you will create a function that takes in a list and returns a list with the reverse order.'''


my_list = [1, 2, 3, 4]

def revers_func(val):
	val.reverse()
	return val

print(revers_func(my_list))