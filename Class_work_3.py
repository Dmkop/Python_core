#!/usr/bin/python3.6

'''1.  Написати функцію, яка знаходить середнє арифметичне значення
 довільної кількості чисел.'''

def average_val(*args):
	my_avg = sum(args) / len(args)
	return my_avg

print(average_val(10, 12, 24))


'''2.  Написати функцію, яка повертає абсолютне значення числа'''

def absolute(arg):
	val = abs(numb)
	return val

numb = int(input("Enter your number: "))
print(absolute(numb))


'''3.  Написати функцію, яка знаходить максимальне число з двох чисел, 
а також в функції використати рядки документації DocStrings.'''


def max_val(num1, num2):
	""" This function return max value """
	res = max(num1, num2)
	return res

print(max_val(19, 20))




'''4.  Написати програму, яка обчислює площу прямокутника, 
трикутника та кола (написати три функції для обчислення площі, 
і викликати їх в головній програмі в залежності від вибору користувача)'''

from math import pi, sqrt, pow

def area_triangle(a, b, c):
	p = (a + b + c) / 2
	S = sqrt(p * (p - a) * (p - b) * (p - c))
	return S

def area_rectangle(l, w):
	S = l * w
	return S

def area_circle(R):
	S = pi * pow(R, 2)
	return S

def main():
	figure = input('hello, enter figure name for definition: ')
	if figure == 'triangle' or figure == 'трикутник':
		side1 = int(input('side a: '))
		side2 = int(input('side b: '))
		side3 = int(input('side c: '))
		return area_triangle('%.5f' % side1, side2, side3)

	elif figure == 'rectangle' or figure == 'rect' or figure == 'прямокутник':
		length = int(input('enter rectangle length: '))
		width = int(input('enter rectangle width: '))
		return area_rectangle(length, width)
	elif figure == 'circle' or figure == 'clc' or figure == 'круг':
		radius = int(input('enter circle radius: '))
		return area_circle('%.5f' % radius)
	else:
		return 'Figure ERROR, try again'

print(main())


'''5.  Написати функцію, яка обчислює суму цифр введеного числа.'''

def my_sum(num):
	res = 0
	item = list(num)
	for index in range(len(item)):
		res += int(item[index])
	return res


user_input = input('enter your data: ')
while user_input:
	print(my_sum(user_input))
	user_input = input('enter your data: ')


'''6.  Написати програму калькулятор, яка складається з наступних функцій: 

головної, яка пропонує вибрати дію та додаткових, які реалізовують вибрані дії, 
калькулятор працює доти, поки ми не виберемо дію вийти з калькулятора, після виходу, 
користувач отримує повідомлення з подякою за вибір нашого програмного продукту!!!'''


def addition(num1, num2):
	res = num1 + num2
	return res

def subtraction(num1, num2):
	res = num1 - num2
	return res

def multiplication(num1, num2):
	res = num1 * num2
	return res

def division(num1, num2):
	res = num1 / num2
	return res

def module (num1, num2):
	res = num1 % num2
	return res

def main():
	print('welcome to the application')
	print('for adding click "+"')
	print('for subtract click "-"')
	print('for multiplication click "*"')
	print('for division click "/"')
	print('for module click "%"')
	result = input('choosing the math operation: ')
	while result:

		if result == 'addition' or result == '+':
			first_num = int(input('Enter the first digit: '))
			second_num = int(input('Enter the second digit: '))
			return addition(first_num, second_num)

		elif result == 'subtraction' or result == '-':
			first_num = int(input('Enter the first digit: '))
			second_num = int(input('Enter the second digit: '))
			return subtraction(first_num, second_num)

		elif result == 'multiplication' or result == '*':
			first_num = int(input('Enter the first digit: '))
			second_num = int(input('Enter the second digit: '))
			return multiplication(first_num, second_num)

		elif result =='division' or result == '/':
			first_num = int(input('Enter the first digit: '))
			second_num = int(input('Enter the second digit: '))
			return division(first_num, second_num)

		elif result == 'module' or result == '%':
			first_num = int(input('Enter the first digit: '))
			second_num = int(input('Enter the second digit: '))
			return module(first_num, second_num)

		elif result == 'exit':
			return 'thank you for choosing our software'

		else:
			return 'error, try again'
print(main())
