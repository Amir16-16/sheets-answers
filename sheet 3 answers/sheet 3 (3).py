# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 14:20:05 2025

@author: Amir
"""

# Your code here
s = "Tom Jerry Harry"
words = s.split()
sorted_words=sorted(words)

result=",".join(sorted_words)
print(result)