#!/usr/bin/python3.6

'''HELP! Jason can't find his textbook! It is two days before the test date, and Jason's textbooks are all out of order! 
Help him sort a list (ArrayList in java) full of textbooks by subject, so he can study before the test.

The sorting should NOT be case sensitive'''

textbooks_list = ['Java', 'C++', 'c', 'Python', 'paskal', 'javascript']
def sort_list(textbooks):
	sorted_list = [item.lower() for item in textbooks]
	sorted_list.sort()
	return sorted_list

print(sort_list(textbooks_list))
