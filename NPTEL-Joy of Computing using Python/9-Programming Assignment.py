#!/usr/bin/env python3
'''
You are given a list L. Write a program to print all numbers
in the list which are exactly repeated twice. The order of numbers
should be same as in list.(for example if 3 appeared before 2 3 should be printed first.)
If no such number exist do not print anything. (input will be handled by us)

Input
[2,2,3,4,5,6,6,7,8,8,8,10, 3]

output
2
3
6

Explanation
Since 2, 3 and 6 is repeated 2 times output is 2, 3 and 6,
whereas 8 is repeated 3 times so it is not printed.
'''
numbers = [int(i) for i in input().split()]
ans = []

for num in numbers:
    if numbers.count(num) == 2 and num not in ans :
        ans.append(num)

for x in ans:
    if ans.index(x) != len(ans) -1 :
        print(x)
    else:
        print(x,end='')
