#!/usr/bin/env python3

'''
programme to make the following pattern
* * * * *
*       *
*       *
*       *
* * * * * 
'''
num = int(input('Enter the length of the side of the square: '))

for r in range(num):
    for c in range(num):
        if r == 0 or r == num -1 or c == 0 or c == num-1 :
            print('*',end =' ')
        else:
            print(' ',end=' ')
    print()
