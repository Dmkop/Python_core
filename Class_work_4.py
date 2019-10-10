#!/usr/bin/python3.6


import pyowm

# Have a pro subscription? Then use:
# owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')
# Search for current weather in London (Great Britain)


owm = pyowm.OWM('a7ab5ba60307b1edd5321a495d1a1658')  # You MUST provide a valid API key
#observation = owm.weather_at_place(input('Hello, enter some city: '))
city = input('What city you are interested: ')
observation = owm.weather_at_place(city)
w = observation.get_weather()
#print(w)                      # <Weather - reference time=2013-12-18 09:20,
                              # status=Clouds>

wind_speed = w.get_wind()['speed']
wind_deg = w.get_wind()['deg']
humidity = w.get_humidity()
temperature = w.get_temperature('celsius')['temp']
details = w.get_detailed_status()
print(f'In {city} city, is the temperature of the air {temperature} for the Celsius, wind speed =  {wind_speed} km/h, humidity is {humidity} %')
print('Also in the city: {}'.format(details))
# Weather details
w.get_wind()                  # {'speed': 4.6, 'deg': 330}
w.get_humidity()              # 87
w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

# Search current weather observations in the surroundings of
# lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
observation_list = owm.weather_around_coords(-22.57, -43.12)


'''1.  Напишіть скрипт-гру, яка генерує випадковим чином число з діапазону чисел від 1 до 100 і пропонує користувачу вгадати це число. 
Програма зчитує числа, які вводить користувач і видає користувачу підказки про те чи загадане число більше чи менше за введене користувачем. 
Гра має тривати до моменту поки користувач не введе число, яке загадане програмою, тоді друкує повідомлення привітання. 
(для виконання завдання необхідно імпортувати  модуль random, а з нього функцію randint())'''


# from random import randint


# rand = randint(1, 100)
# def game(rand_val):
# 	user_data = int(input('Enter your data: '))
# 	while user_data:
# 		if user_data != rand_val:
# 			if user_data < rand_val:
# 				print('Потрібно ввести більше число')
# 			elif user_data > rand_val:
# 				print('Потрібно ввести менше число')
# 		else:
# 			print('You WIN')
# 			break
# 		user_data = int(input('Enter your digit: '))

# game(rand)


'''2.  Напишіть скрипт, який обчислює площу прямокутника a*b, площу трикутника 0.5*h*a, площу кола pi*r**2. 
(для виконання завдання необхідно імпортувати  модуль math, а з нього функцію pow() та значення змінної пі)'''

# from math import pi, sqrt, pow

# def area_triangle(a, b, c):
# 	p = (a + b + c) / 2
# 	S = sqrt(p * (p - a) * (p - b) * (p - c))
# 	return S

# def area_rectangle(l, w):
# 	S = l * w
# 	return S

# def area_circle(R):
# 	S = pi * pow(R, 2)
# 	return S

# def main():
# 	figure = input('hello, enter figure name for definition: ')
# 	if figure == 'triangle' or figure == 'трикутник':
# 		side1 = int(input('side a: '))
# 		side2 = int(input('side b: '))
# 		side3 = int(input('side c: '))
# 		return area_triangle('%.5f' % side1, side2, side3)

# 	elif figure == 'rectangle' or figure == 'rect' or figure == 'прямокутник':
# 		length = int(input('enter rectangle length: '))
# 		width = int(input('enter rectangle width: '))
# 		return area_rectangle(length, width)
# 	elif figure == 'circle' or figure == 'clc' or figure == 'круг':
# 		radius = int(input('enter circle radius: '))
# 		return area_circle('%.5f' % radius)
# 	else:
# 		return 'Figure ERROR, try again'

# print(main())