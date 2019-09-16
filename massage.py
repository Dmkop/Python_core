#!/usr/bin/python3.6

def greeting(name):
	if name == 'johnny' or name == 'Johnny':
		return 'Hello dear {}'.format(name)
	else:
		return f'Hello {name}'

user_name = input('Enter your name: ')
print(greeting(user_name))