#!/usr/bin/python3.6

def game():

	"""In this game, there are 21 sticks lying in a pile. 
Players take turns taking 1, 2, or 3 sticks. The last person to take a stick wins."""

	sticks = 21
	players = input('enter player number: ')
	for item in range(sticks):
		if players == '1':
			pl_1 = int(input('player one, enter your data: '))
			if pl_1 > 3:
				print('you can only enter one two or three, try agaen')
				continue
			elif sticks == 0:
				print('player one is WINNER')
				break
			print(sticks)
			sticks -= pl_1
			print(f'Player one takes {pl_1}')

		elif players == '2':
			pl_2 = int(input('player two, enter your data: '))
			print(sticks)
			if pl_2 > 3:
				print('you can only enter one two or three, try agaen')
				continue
			elif sticks == 0:
				print('player two is WINNER')
				break
			sticks -= pl_2
			print(f'Player two takes {pl_2}')

		players = input('enter player number: ')

print(game.__doc__)
print(game())

