#!/usr/bin/env python3

'''
programme to make the following kind of pattern
(input should be an odd number only, else the desired ouput will not be obtained)
sample input:
7
sample output:
      *
     ***
    * * *
   *  *  *
  *   *   *
 *    *    *
*************
 *    *    *
  *   *   *
   *  *  *
    * * *
     ***
      *
'''

num = int(input('Enter the desired size: '))


for r in range(num):
    for c in range(r,num-1):
        print(end=' ')

    for c in range(r+1):
        if c == 0 or c == r:
            print('*',end='')
        elif r == num-1 :
            print('*',end='')
        else:
            print(end=' ')

    for c in range(r):
        if c == r-1 or r == num-1 :
            print('*',end='')
        else:
            print(end=' ')
    print()

for r in range(1,num):
    for c in range(r):
        print(end=' ')
    for c in range(r,num):
        if c==r or c==num-1 :
            print('*',end='')
        else:
            print(end=' ')
    for c in range(r,num-1):
        if c == num-2:
            print('*',end='')
        else:
            print(end=' ')
    print()
