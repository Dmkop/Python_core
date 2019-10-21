#!/usr/bin/python3.6

'''Given a string, you have to return a string in which each character (case-sensitive) is repeated once.'''

def double_char(txt):
	res = ''
	for item in txt:
		res += item * 2
	return res



user_input = input('Enter some word: ')
while user_input:
	print(double_char(user_input))
	user_input = input('Enter some word: ')