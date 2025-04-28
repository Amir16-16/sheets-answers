# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 20:30:10 2025

@author: Amir
"""

def modlist(lst):
    for i in range(len(lst)):
        lst[i] = 10 * lst[i]

def modvar(num):
    num += 10

lst = [1, 2, 3]
modlist(lst)
print(lst)                                                       # [10,20,30]

x = 0
modvar(x)
print(x)                                                         # 0