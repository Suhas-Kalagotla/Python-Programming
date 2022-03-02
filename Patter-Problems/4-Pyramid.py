#!/usr/bin/env python3

num = int(input('Enter the size of the pyramid: '))

for r in range(num):
    for c in range(r,num):
        print( end=" ")
    for c in range(r):
        print('*',end = " ")
    print()
