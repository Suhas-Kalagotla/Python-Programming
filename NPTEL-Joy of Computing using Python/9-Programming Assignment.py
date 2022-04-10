#!/usr/bin/env python3

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
