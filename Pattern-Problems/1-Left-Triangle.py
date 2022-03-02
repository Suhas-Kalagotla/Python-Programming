#!/usr/bin/env python3

'''
program to make the following right triangle pattern

*
* *
* * *
* * * *
* * * * *

here the no.of rows of the trianle is taken as input from the user

'''
num = int(input('Enter the size of the triangle: \n'))
for r in range(1,num+1):
    for c in range(1,r+1):
        print('*', end=' ')
    print()
