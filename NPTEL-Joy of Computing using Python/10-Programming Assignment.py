#!/usr/bin/env python3
'''
You are given a string S. Write a function count_letters which will return a dictionary containing letters
(including special character) in string S as keys and their count in string S as values.

(input and output will be handled by us you just need to write the function and return the dictionary)

Input
The Joy of computing

Output
{'T': 1, 'h': 1, 'e': 1, ' ': 3, 'j': 1, 'o': 3, 'y': 1, 'f': 1, 'c': 1, 'm': 1, 'p': 1, 'u': 1, 't': 1, 'i': 1, 'n': 1, 'g': 1}

Explanation: T is appeared once in the string, similarly o is appeared 3 times in the string and so on.
(You do not have to worry about the order of arrangement in your dictionary)
'''

sentence = input()

def count_letters(words):
    letters = {}

    for letter in words:
        if letter not in letters :
            letters[letter] = 1
        else :
            letters[letter] += 1

    return letters

print(count_letters(sentence))
