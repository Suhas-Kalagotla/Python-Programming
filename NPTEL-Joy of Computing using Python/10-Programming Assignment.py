#!/usr/bin/env python3

def ans():
    L = [int(x) for x in input().split()]

    ans = []

    for num in L:
        if L.count(num) == 2 and num not in ans:
            ans.append(num)

    return ans

def output():
    nums = ans()
    for x in nums:
        if x == len(nums) - 1 :
            print(x,end='')
        else:
            print(x)

output()
