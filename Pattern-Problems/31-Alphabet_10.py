#!/usr/bin/env python3

'''
python programme to make the following kind of pattern

sample input:
Enter the size of the Reverse Pyramid:
5

sample output:
ABCDEFGHI
 ABCDEFG
  ABCDE
   ABC
    A
'''

size = int(input('Enter the size of the Reverse Pyramid:\n'))

for r in range(size):
    count= 0
    for c in range(r):
        print(end=' ')
    for c in range(2*r+1,2*size):
        print(chr( 65 + count ) , end='')
        count+=1
    print()
