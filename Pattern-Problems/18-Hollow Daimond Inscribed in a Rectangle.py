#!/usr/bin/env python3

'''
Programme to make the following kind of pattern
here the input is given as 5

'''

num = int(input('Enter the size of the Diamond: '))

#for upper half daimond
for row in range(num):
    for star in range(row,num):
        print('*',end='') #no space

    for white_space in range(row+1):
        print(end=' ')    # single space
    for white_space in range(row):
        print(end=' ')

    for star in range(row,num):
        print('*',end='')
    print()

#lower half daimond
for row in range(num):
    for star in range(row+1):
        print('*',end='') #no space

    for white_space in range(row,num):
        print(end=' ') # single space
    for white_space in range(row,num-1):
        print(end=' ')

    for star in range(row+1):
        print('*',end='')
    print()
