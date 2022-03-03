#!/usr/bin/env python3

'''
program to make the following pattern when size of the pyramid is 5
        1
      1 2 1
    1 2 3 2 1
  1 2 3 4 3 2 1
1 2 3 4 5 4 3 2 1
'''

num = int(input('Enter the size of the Pyramid: '))

for r in range(1,num+1):
    for g in range(r,num):
        print(end = '  ')  # double spacing
    for x in range(1,r):
        print(x,end=" ")
    for c in range(r,0,-1):
        print(c,end=' ')
    print()
