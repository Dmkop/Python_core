#!/usr/bin/python3.6

'''Write a program that finds the summation of every number from 1 to num. 
The number will always be a positive integer greater than 0.'''

def summation(num):
	res = 0
	for item in range(1, num + 1):
		res += item
	return res

user_input = int(input('Enter some digit: '))
while user_input:
	print(summation(user_input))
	user_input = int(input('Enter some digit: '))