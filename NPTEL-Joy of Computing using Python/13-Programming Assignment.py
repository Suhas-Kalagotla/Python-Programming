#!/usr/bin/env python3
'''
Aman likes to study about planets. Every night he goes outside and observe some planets
with his telescope. Then he guesses the distance of each planet and pen it down.
In this process he also pen down his favourite planet position. Given the distance of each planet
to be unique you need to return position of Aman's favourite planet after sorting all the distances.

Input:

N (No of planets)
L (List of distances of planet)
K (position of Aman's favourite planet in unsorted list)

Output:

Position of Aman's favourite planet in sorted List.

Example:

Input
5
[4,5,3,2,1]
2

Output
5

Explanation:

The position of aman's favourite planet in unsorted list is 2 and
list of distances of planets at position 2 the distance is 5.
After sorting the list [1,2,3,4,5] the position of aman's favourite is changed to 5.

Note: Index is different from position. Indexing of the list starts from 0
whereas positioning in the list start form 1. 
'''
num = int(input())
dis = [int(x) for x in input().split()]
pos = int(input())

print(sorted(dis).index(dis[pos-1])+1 , end ='' )
