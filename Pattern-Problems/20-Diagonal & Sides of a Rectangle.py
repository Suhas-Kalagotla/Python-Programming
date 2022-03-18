#!/usr/bin/env python3

'''
Python programme to make the following type of patterns

Sample Input:
Enter the size of the Rectangle: 5
Sample Output:
*****
** **
* * *
** **
*****

This is the first pattern where I used formula to print stars all the before
patterns are done without using any formula

Note:
-> Input should be an odd number only, else the desired output will not be obtained
-> For 2,4 as inputs the outputs are squares 
'''

num = int(input('Enter the size of the Rectangle: '))

for r in range(num):
    for c in range(num):
        if r == 0 or r == num-1:  # this helps to print stars at the start and at end .
            print('*',end='') # no space
        elif c == 0 or c == num-1 :
            print('*',end='')
        elif c == r or c == num-r-1 :
            print('*',end='')
        else:
            print(end=' ') # single space

    print()
