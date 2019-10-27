#!/usr/bin/python3.6
'''1.  Напишіть програму, яка пропонує користувачу ввести ціле число і визначає чи це число парне чи непарне, чи введені дані коректні.'''

def except_func():
	try:
		user_input_data = int(input('Enter your data: '))
	except ValueError:
		print('Invalid data')
	else:
		if user_input_data % 2 == 0:
			print('Even')
		elif user_input_data % 2 != 0:
			print('Odd')
	finally:
		print('End')

except_func()

'''2.  Напишіть програму, яка пропонує користувачу ввести свій вік, після чого виводить повідомлення про те чи вік є парним чи непарним числом. 
Необхідно передбачити можливість введення від’ємного числа, в цьому випадку згенерувати власну виняткову ситуацію. 
Головний код має викликати функцію, яка обробляє введену інформацію.'''

class Negative_valeu(Exception):
	def __init__(self, data):
		self.data = data
	def __repr__(self):
		return self.data

class Too_big(Exception):
	def __init__(self, usr_data):
		self.usr_data = usr_data
	def __repr__(self):
		return self.usr_data

try:
	user_age = int(input('Enter your age: '))

	if user_age < 0:
		raise Negative_valeu("Age can't be negative")

	if user_age >= 200:
		raise Too_big('Can`t be a liar')

except Negative_valeu as neg:
		print('Result: {}'.format(neg.data))

except Too_big as bg:
	print(bg.usr_data)

else:
	if user_age % 2 == 0:
		print('Your age is even value')
	elif user_age % 2 == 1:
		print('your age is odd value')
finally:
	print('End)))')


'''3.  Напишіть програму для обчислення частки двох чисел, які вводяться користувачем послідовно через кому, 
передбачити випадок ділення на нуль, 
випадки синтаксичних помилок та випадки інших виняткових ситуацій. 
Використати блоки else та finaly.'''

def fraction(*args):
	try:
		res = args[0] / args[1]
	except ZeroDivisionError:
		print('division by zero is impossible')
	except ValueError:
		print('Please enter digit value')
	except TypeError:
		print('invalid data string is present')
	else:
		print('Your result = {}'.format(res))
	finally:
		print('The end of the program')
fraction()


'''4.  Написати  програму, яка аналізує введене число та в залежності від числа видає день тижня, 
який відповідає цьому числу (1 це Понеділок, 2 це Вівторок і т.д.) . 
Врахувати випадки введення чисел від 8 і більше, а також випадки введення не числових даних.'''

class More(Exception):
	def __init__(self, data):
		self.data = data
	def __repr__(self):
		return self.data

try:
	user_data = int(input("Enter your data: "))
	if user_data >= 8:
		raise More('the value must be less than 8')
except More as M:
	print(M.data)
except ValueError:
	print('Must be digits')
else:
	if user_data == 1:
		print('Monday')
	elif user_data == 2:
		print('Tuesday')
	elif user_data == 3:
		print('Wednesday')
	elif user_data == 4:
		print('Thursday')
	elif usr_data == 5:
		print('Friday')
	elif user_data == 6:
		print("Saturday")
	elif user_data == 7:
		print('Sunday')
finally:
	print('The end of the program')