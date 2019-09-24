#!/usr/bin/python3.6

'''Consider an array of sheep where some sheep may be missing from their place. 
We need a function that counts the number of sheep present in the array (true means present).'''



def count_sheeps(array):
	res = 0
	for item in range(len(array)):
		if array[item]:
			res += 1
		else:
			continue
	return res


print(count_sheeps([True, False, True, True]))