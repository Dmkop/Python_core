#!/usr/bin/python3.6

'''1.  Спробуйте переписати наступний код через map. Він приймає список реальних імен і замінює їх хеш-прізвищами, 
використовуючи  більш надійний метод-хешування.

names = ['Sam', 'Don', 'Daniel'] 
for i in range(len(names)): 
    names[i] = hash(names[i]) 
print(names) 

=> [6306819796133686941, 8135353348168144921, -1228887169324443034]'''

names = ['Sam', 'Don', 'Daniel']
result = map(lambda x: hash(x), names)
print(list(result))



'''2.  Вивести список кольору “red”, який найчастіше зустрічається в даному списку  
[“red”, “green”, “black”, “red”, “brown”, “red”, “blue”, “red”, “red”, “yellow” ] використовуючи функцію filter.'''

color = ['red', 'green', 'black', 'red', 'brown', 'red', 'blue', 'red', 'red', 'yellow']
def color_f(clr):
	return clr == 'red'
result = filter(color_f, color)
print(list(result))

'''3. Всі ці числа в списку мають стрічковий тип даних, наприклад  [‘1’,’2’,’3’,’4’,’5’,’7’], перетворити цей список  в список, всі числа якого мають тип даних integer:
1)  використовуючи метод  append
2)  використовуючи метод  map'''

#1)
my_list = ['1', '2', '3', '4', '5', '6', '7']
new_list = []
for item in range(len(my_list)):
	new_list.append(int(my_list[item]))
print(new_list)

#2)
my_list = ['1', '2', '3', '4', '5', '6', '7']
result = map(lambda item: int(item) , my_list)
#or
result = map(int, my_list)
print(list(result))



'''4. Перетворити список, який містить милі ,  в список, який містить кілометри (1 миля=1.6 кілометра)
a) використовуючи функцію map
b) використовуючи функцію map та lambda'''

miles = [12, 32, 45, 4]
result = map(lambda item: item * 1.6, miles)
print(list(result))

def kilometer_f(val):
	return val * 1.6

miles = [12, 32, 45, 4]
result = map(kilometer_f, miles)
print(list(result))



'''5.  Знайти найбільший елемент в списку  використовуючи функцію reduce'''

from functools import reduce
my_list = [1, 32, 67, 10, 43, 100, 382]
result = reduce(lambda a, x: a if a > x else x, my_list)
print(result)

'''6. Перепишіть наступний код, використовуючи map, reduce і filter. Filter приймає функцію і колекцію. 
Повертає колекцію тих елементів, для яких функція повертає True.'''

from functools import reduce
people = [{'name': 'Sam', 'height': 160}, {'name': 'Alex', 'height': 80}, {'name': 'Jack'}] 
# height_total = 0 
# height_count = 0 
# for person in people: 
#     if 'height' in person: 
#         height_total += person['height'] 
#         height_count += 1 
# print(height_total)
# print(height_count)


result = list(filter(lambda x: 'height' in x, people))
print(result)
result_2 = list(map(lambda item : item['height'], result))
print(result_2)
result_3 = reduce(lambda a, x: a + x, result_2)
print(result_3)