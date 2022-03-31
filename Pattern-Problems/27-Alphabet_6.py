#!/usr/bin/env python3

'''
Python programme for making the following pattern

sample input:
5
sample output:
     A
    AB
   ABC
  ABCD
 ABCDE

'''
num = int(input())

for r in range(num):
    for c in range(r,num):
        print(end=' ')
    for c in range(r+1):
        print(chr(65+c),end='')
    print()
