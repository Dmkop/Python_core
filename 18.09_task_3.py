#!/usr/bin/python3.6

'''Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!'''


def banjo(name):
	print('Are you playing banjo')
	first_letter = name[0]
	if first_letter == 'R' or first_letter == 'r':
		return name + ' plays banjo'
	else:
		return name + ' doesn`t play banjo'

print(banjo('ron'))
print(banjo('Ron'))
print(banjo('Dmkop'))