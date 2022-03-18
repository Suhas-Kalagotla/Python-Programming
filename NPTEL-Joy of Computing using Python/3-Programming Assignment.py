#!/usr/bin/env python3

'''
You given a number as the an input. You have to display all the numbers from 0 till x.

Input
x

Output
0
1
2
.
.
x
'''

num = int(input())

for number in range(num+1):
    print(number)
