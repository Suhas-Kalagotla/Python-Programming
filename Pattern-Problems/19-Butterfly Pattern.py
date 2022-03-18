#!/usr/bin/env python3

'''
Progamme to make the following type of pattern
here input is given as 5
*        *
**      **
***    ***
****  ****
**********
**********
****  ****
***    ***
**      **
*        *
'''

num = int(input('Enter the size of the Butterfly: '))

# upper half
for r in range(num):
    for c in range(r+1):
        print('*',end='')  # single space

    for white_space in range(r,num-1):
        print(end=' ') # single space
    for white_space in range(r,num-1):
        print(end=' ')

    for c in range(r+1):
        print('*',end='')
    print()

# bottom half
for r in range(num):
    for c in range(r,num):
        print('*', end='')

    for white_space in range(r):
        print(end=' ')
    for white_space in range(r):
        print(end=' ')

    for c in range(r,num):
        print('*',end='')
    print()
