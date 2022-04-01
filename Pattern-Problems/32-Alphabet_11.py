#!/usr/bin/env python3

'''
Pattern programme to make the following pattern

sample input:
5

sample output:
     A
    ABC
   ABCDE
  ABCDEFG
 ABCDEFGHI
ABCDEFGHIJK
 ABCDEFGHI
  ABCDEFG
   ABCDE
    ABC
     A
'''

num = int(input())

for r in range(num):
    count = 0
    for c in range(r,num):
        print(end=' ')
    for c in range(2*r+1):
        print(chr( 65 + count ) , end='')
        count+= 1
    print()

for r in range(num+1):
    count = 0
    for c in range(r):
        print(end=' ')
    for c in range(2*r - 1 , 2*num):
        print(chr( 65 + count) , end = '')
        count+=1
    print()
