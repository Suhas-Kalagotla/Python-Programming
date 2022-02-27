#!/usr/bin/env python3

'''
Python programm to make the following pattern

* * * * * 
* * * * 
* * * 
* * 
* 

'''

num = int(input('Enter the size of the Triangle: \n'))

for r in range(1,num+1):
    for c in range(r,num+1):
        print('*',end=' ')
    print()
