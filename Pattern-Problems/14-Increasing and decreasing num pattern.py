#!/usr/bin/env python3

'''
this program makes the following type of pattern

1 
1 2 1
1 2 3 2 1
1 2 3 4 3 2 1
1 2 3 4 5 4 3 2 1

'''
num = int(input('Enter the size of the number: '))

for r in range(1,num+1):
    for c in range(1,r):
        print(c,end =' ')
    for c in range(r,0,-1):
        print(c,end=' ')
    print()
