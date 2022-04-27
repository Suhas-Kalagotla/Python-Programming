#!/usr/bin/env python3

'''
You are given a list L. Write a program to print first prime number encountered in the list L.
(Treat numbers below and equal to 1 as non prime)

Input will be handled by us.

Input
[1,2,3,4,5,6,7,8,9]

output
2

Explanation
Since 2 is the first prime number is list L,
therefor it is printed.
'''

nums = [int(x) for x in input().split()]

def isPrime(num):
        divisors =[]
        for y in range(1,num+1):
            if num % y == 0 :
                divisors.append(y)
        if len(divisors) == 2 :
            return True
        else:
            return False

for x in nums:
    if isPrime(x):
        print(x,end='')
        break
