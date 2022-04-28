#!/usr/bin/env python3
'''
write a function whole(N) which takes a number N and return the sum of first N whole number. Write the program using recursion.

Input
N

Output
sum of whole numbers till N

Example:

Input
3

Output
6

Explanation
Sum of first 3 natural numbers are 0+1+2+3 = 6
'''
num = int(input())

def sum(x):
    if x == 0 :
        return 0
    else:
        return x + sum(x-1)

print(sum(num) , end = '')
