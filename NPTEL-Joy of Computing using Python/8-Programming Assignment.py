#!/usr/bin/env python3
'''
You are given a string s. Print the string s
with every character except vowels in s replaced by _.
(input will be handled by us)

Input
weekend

output
_ee_e__

Explanation
Consonants w, k, n, d in weekend is replaced by _ and
string s printed with the changes.
'''
s = input()
replaced_string = ''

for letter in s :
    if letter.lower() not in 'aeiou':
        replaced_string += '_'
    else:
        replaced_string += letter

print(replaced_string,end='')
