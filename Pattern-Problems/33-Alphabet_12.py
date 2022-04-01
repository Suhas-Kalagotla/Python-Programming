#!/usr/bin/env python3

'''
Python programme to make the following kind of pattern

sample input:
5

sample output:
ABCDEFGHI
 ABCDEFG
  ABCDE
   ABC
    A
    A
   ABC
  ABCDE
 ABCDEFG
ABCDEFGHI
'''

num = int(input())

for r in range(num):
    count = 0
    for c in range(r):
        print(end=' ')
    for c in range(2*r+1,2*num):
        print(chr( 65 + count ) , end='')
        count += 1
    print()

for r in range(num):
    count = 0
    for c in range(r,num-1):
        print(end=' ')
    for c in range(2*r+1):
        print(chr( 65 + count) , end='')
        count += 1
    print()
