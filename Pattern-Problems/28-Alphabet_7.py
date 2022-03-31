#!/usr/bin/env python3

'''
python programme to make the following pattern
the code is almost same as the hollow triangle except we have
built in function called chr() to print alphabet

sample input:
Enter the size of the triangle: 6

sample output:
A
AB
A B
A  B
A   B
ABCDEF
'''
size = int(input('Enter the size of the triangle: '))

for r in range(1,size+1):
    count = 0
    for c in range(r):
        if c == 0 or c == r-1 or r == size : #print only in first or last column or last row
            print(chr( 65 + count ) , end='')
            count += 1
        else:
            print(end=' ')
    print()
