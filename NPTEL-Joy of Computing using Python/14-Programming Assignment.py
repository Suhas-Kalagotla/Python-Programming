#!/usr/bin/env python3
'''
Romeo and Juliet love each other. Romeo wants to send a message to Juliet and also don't want anyone to read it without his permission.
So he shifted every small letter in the sentence by -2 position and every capital letter by -3 position.
(If the letter is c, after shifting to by -2 position it changes to a, and for D new letter will be A).
But the letter is too long and Romeo does not have enough time to encrypt his whole letter. Write a program to help Romeo which prints
the encrypted message. You can assume there are no special characters except spaces and numeric value.

Input
A string S

Output
Encrypted string

Example

Input
Hello Juliet

Output
Ecjjm Gsjgcr

Explanation
H is shifted by -3 position and changed to E. 'e' is shifted by -2 position and changed to c and so on.
'''

import string

sentence = input()
new_sentence = ''

lower = string.ascii_lowercase
capital = string.ascii_uppercase

for letter in sentence:
    if letter in lower:
        index = lower.index(letter)
        index = ((index -2 )+ 26 )% 26
        new_sentence += lower[index]
    elif letter in capital:
        index = capital.index(letter)
        index = ((index - 3)+26) % 26
        new_sentence += capital(index)
    else:
        new_sentence += letter

print(new_sentence)
