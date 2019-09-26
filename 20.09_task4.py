#!/usr/bin/python3.6

'''Oh no, Timmy's created an infinite loop! Help Timmy find and fix the bug in his unfinished For Loop!
def create_array(n):
    res=[]
    i=1
    while i<=n: res+=[i]
    return res'''

def create_array(n):
    res=[]
    i=1
    while i<=n: 
    	res+=[i]
    	i += 1
    return res

print(create_array(10))
