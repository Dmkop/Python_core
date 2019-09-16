#!/usr/bin/python3.6

'''We need a function that can transform a number into a string.

What ways of achieving this do you know?'''

numb = int(input('Enter data: '))
while numb:
	res = str(numb)
	print('Number {} has {}'.format(res, type(res)))
	numb = int(input('Enter next data: '))

				#OR function

# def convert(numb1):
# 	if type(numb1) == int or type(numb1) == float:
# 		conv = str(numb1)
# 	print(f"Number {numb1} has {type(conv)}")

# numb1 = int(input("enter data: "))

# convert(numb1)