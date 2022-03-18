#!/usr/bin/env python3

'''
You are given a list L. Write a function all_even that accepts the list L and print all the even numbers is the list L.(Order of the numbers should be same as the order present in the list)

We will take care of the input.

Input

A list L

output

all the even numbers in list
'''


L = [int(i) for i in input().split()] # given line of code

def all_even(L) :
    for num in L :
        if num % 2 == 0 :
            print(num)

all_even(L) # given line of code 
