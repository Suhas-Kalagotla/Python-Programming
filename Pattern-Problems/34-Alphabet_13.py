#!/usr/bin/env python3

'''
Programme to make the following pattern

sample input:
Enter the size of the triangle:
5

sample ouput:
A
AB
ABC
ABCD
ABCDE
ABCD
ABC
AB
A
'''

size = int(input('Enter the size of the triangle:\n'))

for r in range(1,size+1):
    count = 0
    for c in range(r):
        print(chr( 65 + count) , end='')
        count += 1
    print()

for r in range(1,size):
    count = 0
    for c in range(r,size):
        print(chr(65 + count) , end='')
        count+= 1
    print()
