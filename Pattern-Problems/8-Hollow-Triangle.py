#!/usr/bin/env python3

'''
this programme creates the following hollow triangle patter
*
**
* *
*  *
*   *
*    *
*******
'''

num = int(input('Enter the size of the triangel: '))

for r in range(num):
    for c in range(r+1):
        if c == 0 or r == num -1 or r == 0 or r == c :
            print('*',end='')
        else :
            print(end=' ')
    print()
