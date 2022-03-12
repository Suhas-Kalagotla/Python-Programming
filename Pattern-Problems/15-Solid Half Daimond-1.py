#!/usr/bin/env python3

'''
programme to make the following type of pattern

here input is given as 5

1
2*2
3*3*3
4*4*4*4
4*4*4*4
3*3*3
2*2
1
'''

num = int(input('Enter the size of the numbers: '))

for r in range(1,num):
    for c in range(1,r+1):
        if c == r :
            print(r,end=' ')
        else:
            print(r,end='*')
    print()
for r in range(1,num):
    for c in range(r,num):
        if c == num-1:
            print(num-r,end = '')
        else:
            print(num-r,end='*')
    print()
