#!/usr/bin/env python3

'''
This program makes the following pattern
      *
     * *
    *   *
   *     *
  *       *
 *         *
* * * * * * *

'''

num =int(input('Enter the size of the Pyramid: '))

for r in range(num):
    for c in range(r,num-1):
        print(end=' ') # single spacing
    for c in range(r+1):
        if r == num-1 or c == 0 or c == r :
            print('*',end = ' ')
        else:
            print(end='  ') # double spacing
    print()
