#!/usr/bin/python3.6

'''Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.'''

def convert(bool_val):
	if bool_val:
		return 'Yes'
	else:
		return 'No'

print(convert(True))
print(convert(False))