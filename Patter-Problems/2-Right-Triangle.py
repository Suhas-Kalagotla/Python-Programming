#!/usr/bin/env python3

'''
program to make the following right triangle pattern

*
**
***
****
*****

here the no.of rows of the trianle is taken as input from the user

'''
num = int(input('Enter the size of the triangle: \n'))
for r in range(1,num+1):
    for c in range(r,num): # to print left spaces
        print(' ',end=' ')
    for c in range(1,r+1):     # to print stars
        print('*', end=' ')
    print() # this function is intended for the row loop to enter the new line after
            # finishing one loop because it has end = '\n' which is default
