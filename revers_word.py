#!/usr/bin/python3.6


'''You need to write a function that reverses the words in a given string.
 A word can also fit an empty string. If this is not clear enough, here are some examples:

As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.'''

txt = input("Enter some words: ")
my_list = txt.split()
my_list.reverse()

for x in range(len(my_list)):
	print(my_list[x], end=" ")

#FUNCTION


# def revers(words):
# 	my_new_list = words.split()
# 	my_new_list.reverse()
# 	for item in range(len(my_new_list)):
# 		print(my_new_list[item], end = " ")

#txt = input("Enter some words: ")

# revers(txt)