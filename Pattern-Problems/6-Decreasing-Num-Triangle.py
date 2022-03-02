#!/usr/bin/env python3

'''
python programm to make the following pattern

1 
2 1
3 2 1
4 3 2 1
5 4 3 2 1

'''

num = int(input('Enter the size of the triangle: '))
for r in range(1,num+1):
    for c in range(r,0,-1):
        print(c,end=' ')
    print()
