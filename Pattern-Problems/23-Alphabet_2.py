#!/usr/bin/env python3

'''
programme to produce following type of pattern

in this pattern every character will change 

sammple output:
A B C D E
F G H I J
K L M N O
P Q R S T
U V W X Y
'''
num = 0
for r in range(5):
    for c in range(5):
        print(chr(65+num),end=' ')
        num += 1
    print()
