#!/usr/bin/env python3

'''
Python programming for making the following type of pattern
here input is given as 3
*
* 1 *
* 1 2 1 *
* 1 2 3 2 1 *
* 1 2 1 *
* 1 *
*
this pattern is similar to the 14 pattern but this pattern also has a decreasing
lower triangle , making it as a half daimo nd and stars are additional at star and end
of row
'''

num = int(input('Enter the size of the Daimond: '))
num += 1
for r in range(1,num+1):
    for c in range(1,r):
        if c == 1 :
            print('*',end=' ')
        else:
            print(c-1,end=' ')
    for c in range(r,0,-1):
        if c == 1 :
            print('*',end=' ')
        else:
            print(c-1,end=' ')
    print()

for r in range(1,num):
    for c in range(1,num-r):
        if c == 1  or c == num-r+1:
            print('*',end=' ')
        else:
            print(c-1,end=' ')
    for c in range(num-r,0,-1):
        if c ==1 :
            print('*',end=' ')
        else:
            print(c-1,end=' ')
    print()
