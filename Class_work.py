#!/usr/bin/python3.6

'''1.  Роздрукувати всі парні числа менші 100 (написати два варіанти коду:
 один використовуючи цикл while, а інший з використанням циклу for).'''

numb = 0
while numb < 100:
	if numb % 2 == 0:
		print(numb)
	numb += 1


for numb1 in range(0, 100):
	if numb1 % 2 == 0:
		print(numb1)


'''2.  Роздрукувати всі непарні числа менші 100. (написати два варіанти коду: 
	один використовуючи оператор continue, а інший без цього оператора).'''


numb2 = 0
while numb2 < 100:
	if numb2 % 2 != 0:
		print(numb2)
	numb2 += 1


for numb3 in range(0, 100):
	if numb3 % 2 == 1:
		print(numb3)

'''3.  Перевірити чи список містить непарні числа.
          (Підказка: використати оператор break)'''


my_list = [2, 4, 6, 8, 9, 10, 12]
for item in my_list:
	if item % 2 != 0:
		print("Список містить непарне число %d" % item)
		break
	print(item)


'''4.  Створити список, який містить елементи цілочисельного типу, 
потім за допомогою циклу перебору змінити тип даних елементів на числа з плаваючою крапкою. 
(Підказка: використати вбудовану функцію float ()).'''

stop = int(input("numbers of list items: "))
my_list = []
for item in range(stop):
	my_list.append(input("Enter list data: "))
print(my_list)

for res in range(len(my_list)):
	my_list[res] = float(my_list[res])
print(my_list)

'''5.  Вивести числа Фібоначі включно до введеного числа n, використовуючи цикли.
 (Послідовність чисел Фібоначі 0, 1, 1, 2, 3, 5, 8, 13 і т.д.)'''

stop = int(input("Enter iterations count: "))

fib1 = 0
fib2 = 1

for res in range(stop):
	print(fib2)
	fib1, fib2 = fib2, fib1 + fib2



'''6.  Створити список, що складається з чотирьох елементів типу string.
 Потім, за допомогою циклу for, вивести елементи по черзі на екран.'''

words = ["h", "e", "l", "l", "o"]

for elements in words:
	print(elements)

'''7.  Змінити попередню програму так, щоб в кінці кожної букви елементів при виводі додавався певний символ,
 наприклад “#”. 
  (Підказка: цикл for може бути вкладений в інший цикл, а також  треба використати функцію print(“ ”, end=”%”)).'''

words = ['a', 'b', 's', 'd']
for item in words:
	print(item, end='#')
	print()

'''8.  Юзер вводить число з клавіатури, написати скріпт, який визначає чи це число просте чи складне.'''

user_data = int(input('enter some digit for verification: '))
while user_data:
	if user_data == 1:
		print("Число %d не є складним і не є простим" % user_data)
	elif user_data == 2 or user_data % 2 != 0:
		print("Число {} є простим".format(user_data))
	else:
		print(f"Число {user_data} є складеним")
	user_data = int(input('enter next digit for verification: '))