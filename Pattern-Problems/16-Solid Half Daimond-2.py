#!/usr/bin/env python3

'''
python grogramme to make the following pattern

here input is given as 4
1
2*3
4*5*6
7*8*9*10
7*8*9*10
4*5*6
2*3
1

This pattern is challenging but makes us to understand how to define variables
inside the loop
'''

num = int(input('Enter the size of the Triangle: '))
sum = 0
for r in range(1,num+1):
    for c in range(1,r+1):
        sum += 1
        if c == r :
            print(sum,end=' ')
        else:
            print(sum,end='*')
    print()
for r in range(1,num+1):
    start = sum                   # as the variable name states it helps to start the row
    for c in range(r,num+1):
        diff = sum - num + c
        start -= 1                # by the end of the loop this value helps to define the next row starting value
        if c == num :
            print(diff,end=' ')
            sum = start            # at the end of the column we define sum which is linked to start value
        else:
            print(diff,end='*')
# the diff , start variables are used to print the column in reverse decreasing order 
    print()
