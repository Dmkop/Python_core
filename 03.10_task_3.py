#!/usr/bin/python3.6

'''Create a class Ghost

Ghost objects are instantiated without any arguments.

Ghost objects are given a random color attribute of white" or "yellow" or "purple" or "red" when instantiated'''


from random import randint

class Ghost():
	def __init__(self):
		self.color = randint(1, 4)
	def color_ghost(self):
		if self.color == 1:
			return 'White'
		elif self.color == 2:
			return 'Yellow'
		elif self.color == 3:
			return 'Purple'
		elif self.color == 4:
			return 'Red'

ghost = Ghost()
print(ghost.color_ghost())