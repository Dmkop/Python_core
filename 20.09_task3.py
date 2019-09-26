#!/usr/bin/python3.6

'''Write a function taking in a string like WOW this is REALLY amazing and returning Wow this is really amazing. String s
hould be capitalized and properly spaced. Using re and string is not allowed.'''

def no_yelling(txt):
	first_letter = txt[0]
	other_txt = txt[1:]
	res = first_letter.upper() + other_txt.lower()
	return res

# OR

# def no_yelling(txt):
# 	return txt[0].upper() + txt[1:].lower()


my_txt = input("Enter your data: ")
print(no_yelling(my_txt))


