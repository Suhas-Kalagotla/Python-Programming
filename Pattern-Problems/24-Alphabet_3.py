#!/usr/bin/env python3

'''
python code to make the following kind of alphabet pattern

sample input:
Enter the size of the square:
5

sample output:
A A A A A 
B B B B B
C C C C C
D D D D D
E E E E E

'''
size = int(input('Enter the size of the square:\n'))

for r in range(size):
    for c in range(size):
        print(chr(65+r) , end = ' ')
    print()
