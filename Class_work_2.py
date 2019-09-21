#!/usr/bin/python3.6

'''1.  Створити список цілих чисел,
 які вводяться з терміналу та визначити серед них максимальне та мінімальне число.'''


# my_list = []
# limit = int(input("count elements: "))

# for item in range(limit):
# 	my_list.append(int(input("enter your data in list: ")))
# print(my_list)
#print('Максимальне знчення списку: {} та мінімальне значення списку: {}'.format(max(my_list), min(my_list)))



# limit = int(input("count elements: "))
# my_list = [int(input('enter your data in list: ')) for item in range(limit)]
# print('Максимальне знчення списку: {} та мінімальне значення списку: {}'.format(max(my_list), min(my_list)))




'''2.  В інтервалі від 1 до 10 визначити числа 
•  парні, які діляться на 2,
•  непарні, які діляться на 3, 
•  числа, які не діляться на 2 та 3.'''


# for item in range(1, 11):
# 	if item % 2 != 0 and item % 3 != 0:
# 		print('числа, які не діляться на 2 та 3: {}'.format(item))
# 	elif item % 2 != 0 and item % 3 == 0:
# 		print('непарні, які діляться на 3: {}'.format(item))
# 	elif item % 2 == 0:
# 		print('парні, які діляться на 2: {}'.format(item))


'''3.  Написати програму, яка обчислює факторіал числа,
 яке користувач вводить.(не використовувати рекурсивного виклику функції)'''


# user_numb = int(input("enter your data: "))
# item = 1
# step = 1
# while step <= user_numb:
# 	item *= step
# 	step += 1
# print(f"Факторіал числа {user_numb} == {item}")


'''4.  Напишіть скрипт, який перевіряє логін, який вводить користувач. 
Якщо логін вірний (First), то привітайте користувача. 
Якщо ні, то виведіть повідомлення про помилку. 
(використайте цикл while)'''


# login = input("hello, enter login: ")

# while login:
# 	if login == 'First':
# 		print('Hello dear user)))')
# 	else:
# 		print('Login error')
# 	login = input("hello, enter login: ")