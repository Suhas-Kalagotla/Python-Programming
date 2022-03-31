#!/usr/bin/env python3

'''
programming to make the following pattern

sample input:
5
sample output:
     A
    A B
   A   B
  A     B
 ABCDEFGHI
'''

num = int(input())

for r in range(num):
    count = 0
    for c in range(r,num):
        print(end=' ')
    for c in range(2*r + 1 ):
        if c == 0 or c == 2*r or r == num-1 :
            print(chr( 65 + count) , end = '')
            count += 1
        else:
            print(end=' ')
    print()
