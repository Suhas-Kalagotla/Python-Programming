#!/usr/bin/env python3

'''
program to produce the following pattern programming

     *
    * *
   * * *
  * * * *
 * * * * *
* * * * * *
 * * * * *
  * * * *
   * * *
    * *
     *
'''

num = int(input('Enter the size of the Diamond: '))

for r in range(num+1):            # this loop is same as for pyramid
    for c in range(r,num):
        print(end=" ")
    for c in range(r+1):
        print('*',end = " ")
    print()
for r in range(num):              # this loop prints the pyramid in reverse 
    for c in range(r+1):
        print(end=" ")
    for c in range(r,num):
        print('*',end=' ')
    print()
