#!/usr/bin/python3.6

'''Task
Your task is to complete this Class, the Person class has been created. 
You must fill in the Constructor method to accept a name as string and an age as number, 
complete the get Info property and getInfo method/Info getter which should return'''


class Person():
	def __init__(self, name, age):
		self.name = name
		self.age = age
	@property
	def info(self):
		return '{} age is {}'.format(self.name, self.age)

first = Person('Dmytro', 25)
print(first.info)