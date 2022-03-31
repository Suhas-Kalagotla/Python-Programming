#!/usr/bin/env python3

'''
python programme to make the follwing kind of pattern

sample input :
Enter the size of the square:
5

sample output:

'''

num = int(input('Enter the size of the square:\n'))

for r in range(num):
    for c in range(num):
        print(chr(65+c)  , end = ' ' )
    print()
