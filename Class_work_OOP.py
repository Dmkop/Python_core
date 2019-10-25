#!/usr/bin/python3.6

'''Створити батьківський клас Figure з методами init: ініціалізується колір, 
get_color: повертає колір фігури,
info: надає інформацію про фігуру та колір,  
від якого наслідуються такі класи як Rectangle, 
Square, які мають інформацію про ширину, висоту фігури, метод square, який знаходить площу фігури.'''



class Figure:

	def __init__(self, color):
		self.color = color

	def get_color(self):
		return self.color

	def info(self):
		print('Figure')
		print('Color is: '+ self.color)



class Rectangle(Figure):
	def __init__(self, color, width = 100, height = 100):
		super().__init__(color)
		self.width = width
		self.height = height

	def area(self):
		return self.width * self.height

	def info(self):
		print('Rectangle')
		print('Color: ' + self.color)
		print('Width : {}'.format(self.width))
		print('Height: {}'.format(self.height))
		print('Square: {}'.format(self.area()))


class Square(Figure):
	def __init__(self, color, width):
		super().__init__(color)
		self.width = width

	def area(self):
		return self.width ** 2

	def info(self):
		print('Square')
		print('Color is {}'.format(self.color))
		print('Width and height: {}'.format(self.width))
		print('Square: {}'.format(self.area()))


fig1 = Figure('red')
print(fig1.info())
fig2 = Rectangle('red', 89, 45)
print(fig2.info())

fig3 = Square('blue', 200)
print(fig3.info())