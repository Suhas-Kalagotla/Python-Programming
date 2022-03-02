#!/usr/bin/env python3
'''
Python program to make the following pattern

1

2 3

4 5 6

7 8 9 10

11 12 13 14 15
'''

num = int(input('Enter the size of the triangle: '))

z=0
for x in range(num+1):
    for y in range(x):
        z+=1
        print(f'{z}',end=' ')
    print('\n')
