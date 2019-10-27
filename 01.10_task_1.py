#!/usr/bin/python3.6

'''Create a method is_uppercase() to see whether the string is ALL CAPS.'''



def upper(txt):
	return txt.isupper()


user_data = input('Enter some word: ')
while user_data:
	print(upper(user_data))
	user_data = input('Enter next word: ')