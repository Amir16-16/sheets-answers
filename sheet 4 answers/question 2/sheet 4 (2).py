# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 12:15:44 2025

@author: Amir
"""

# Generate a string of characters that contains all characters (upper and lower), digits using comprehension
characters = ''.join([chr(i) for i in range(ord('0'), ord('9') + 1)] + 
                     [chr(x) for x in range(ord('A'), ord('Z') + 1)] + 
                     [chr(y) for y in range(ord('a'), ord('z') + 1)])

print(characters)



# the ord function it converts a character into its corresponding numerical representation in the Unicode standard
# The chr function is the inverse of the ord function. It takes an integer (representing a Unicode code point) and returns the corresponding character


##########shr7#############
l=[chr(i) for i in range(ord('0'), ord('9') + 1)]
# print(l)
# l="".join(l)
# print(l)

w=[chr(i) for i in range (ord("A"), ord("Z")+1)]
# print(w)
# w="".join(w)
# print(w)

chars="".join(l+w)
print(chars)