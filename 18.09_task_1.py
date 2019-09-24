#!/usr/bin/python3.6

'''You were camping with your friends far away from home, but when it's time to go back,
 you realize that you fuel is running out and the nearest pump is 50 miles away! You know that on average, 
 your car runs on about 25 miles per gallon. There are 2 gallons left. 
 Considering these factors, write a function that tells you if it is possible to get to the pump or not. 
 Function should return true if it is possible and false if not.'''


def main(miles, gallons):
 	one_gallon = 25
 	res = gallons * one_gallon
 	if res < miles:
 		return False
 	else:
 		return True



miles = int(input('enter the number of miles: '))
gallons = int(input('Enter the numb of gallons: '))
while miles:
	result = main(miles, gallons)
	print(result)
	miles = int(input('enter the number of miles again: '))
	gallons = int(input('Enter the numb of gallons again: '))