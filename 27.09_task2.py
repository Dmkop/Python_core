#!/usr/bin/python3.6


'''Your collegue wrote an simple loop to list his favourite animals. 
But there seems to be a minor mistake in the grammar, which prevents the program to work. Fix it! :)

If you pass the list of your favourite animals to the function, you should get the list of the animals with orderings and newlines added.'''

list_animals = ['dog', 'cat', 'elephant']

def animals_list(my_lits):
	res = ''
	for item in range(len(my_lits)):
		res += str(item + 1) + '. ' + my_lits[item] + '/n'
	return res
print(animals_list(list_animals))