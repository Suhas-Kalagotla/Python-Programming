#!/usr/bin/env python3
'''
You are given a list L. Write a function uniqueE which will return a list of unique elements
 is the list L in sorted order. (Unique element means it should appear in list L only once.)

Input will be handled by us

Input
[1,2,3,3,4,4,2,5,6,7]

Output
[1,5,6,7]

Explanation

Elements 1,5,6,7 appears in the input list only once.
'''

nums = list(map(int,input().split()))

def uniqueE(nums):
    ans = []
    [ans.append(x) for x in nums if x not in ans and nums.count(x) == 1]

    return sorted(ans)

print(uniqueE(nums),end='')
