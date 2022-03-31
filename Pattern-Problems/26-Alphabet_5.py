#!/usr/bin/env python3

'''
this programme makes the following pattern

sample input :
Enter the size of the Triangle:
5

sample output:
A
AB
ABC
ABCD
ABCDE
'''

size = int(input('Enter the size of the Triangle:\n'))

for r in range(size):
    for c in range(r+1):
        print(chr(65+c) , end='')
    print()
