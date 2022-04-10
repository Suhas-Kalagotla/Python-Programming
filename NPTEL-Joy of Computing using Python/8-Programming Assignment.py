#!/usr/bin/env python3

s = input()
replaced_string = ''

for letter in s :
    if letter.lower() not in 'aeiou':
        replaced_string += '_'
    else:
        replaced_string += letter

print(replaced_string,end='')
