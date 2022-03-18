#!/usr/bin/env python3

'''
You are given a list named L. Print all the elements at odd position of list L.(We will take care of the input, you just have to print elements present at odd position)

Input:

A List L

Output

All elements present at odd position
'''

L = [int(i) for i in input().split()] #given piece of code

for num in range(len(L)):
    if num % 2 != 0 :
        print(L[num])
