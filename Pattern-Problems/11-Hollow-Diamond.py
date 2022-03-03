#!/usr/bin/env python3

'''
Python programme to generate the following pattern
    *
   * *
  *   *
 *     *
*       *
*       *
 *     *
  *   *
   * *
    * 
'''

num = int(input('Enter the size of the diamond: '))

for r in range(num):
    for c in range(r,num-1):
        print(end=' ')     # single spacing
    for c in range(r+1):
        if c== 0 or c ==r :
            print('*',end = ' ')
        else:
            print(end='  ')  # double spacing
    print()
for x in range(num):
    for y in range(x):
        print(end=' ') # single spacing
    for y in range(x,num):
        if y == 0 or y == x or y == num-1 :
            print('*',end=' ')
        else:
            print(end='  ') # double spacing
    print()
