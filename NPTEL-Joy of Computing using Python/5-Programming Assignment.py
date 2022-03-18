#!/usr/bin/env python3

'''
You are given a list L. Print the list of first 3 smallest elements in
ascending order and last 2 greatest elements in descending order of the list L respectively.
(We will take care of the input)

Input

A list L

Output

A list of first 3 smallest elements in L in ascending order
A list of last 2 greatest elements in L in descending order
'''

L = [int(i) for i in input().split()] # given code

L.sort()
print(L[:3])              # here we are printing the first 3 smallest number after sorting
print(L[::-1][:2],end='') # here we reversed the list and printing first 2
