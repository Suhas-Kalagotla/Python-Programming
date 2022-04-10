#!/usr/bin/env python3

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
