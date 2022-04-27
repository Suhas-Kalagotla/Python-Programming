#!/usr/bin/env python3
'''
You are given an integer n. Write a program to print a right angle triangle. (See output of public test cases for the pattern)
(input will be handled by us)
Input
5

output
    *
   **
  ***
 ****
*****
'''
num = int(input())

for r in range(1,num+1):
    for c in range(r,num):
        print(end=' ')
    for c in range(r):
        print('*',end='')
    if r != num :
        print()
    else:
        print(end='')
