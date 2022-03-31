#!/usr/bin/env python3

'''
python programme to make the following kind of pattern

sample input:
5

sample output:
'''

size = int(input())

for r in range(size):
    for c in range(r,size):
        print(end=' ')
    for c in range(2*r + 1):
        print(chr( 65 + c) , end = '')
    print()
