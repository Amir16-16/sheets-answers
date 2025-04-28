# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 01:06:57 2025

@author: Amir
"""
################# using shorthand if-else and list comprehension #################

x = [1, 2, 10, 13, 1]
output = [True if num % 2 == 0 else False for num in x]
print(output)  # Output: [False, True, True, False, False]



                            #another solution#

# for i in range(len(x)):
lst=[True if x[i]%2==0 else False for i in range(len(x))]
print(lst)