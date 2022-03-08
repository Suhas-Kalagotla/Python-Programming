#!/usr/bin/env python3
'''
The python programme for making the following kind of patterns

********1********
*******2*2*******
******3*3*3******
*****4*4*4*4*****
****5*5*5*5*5****

'''
num = int(input('Enter the size of the pattern: '))

for r in range(1,num+1):
    for c in range(r,num+4):
        print('*' , end = '')
    for n in range(1,r+1):
        print(r,end='*')
    for s in range(r,num+3):
        print('*',end = '')
    print()
