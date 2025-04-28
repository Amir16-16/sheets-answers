# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 21:55:20 2025

@author: Amir
"""

sequence=[10,20,30,40,50,60]
even_sum=0
odd_sum=0
index=0
for value in sequence :
    if index % 2 == 0 :
        even_sum+=value
    else:
        odd_sum+=value
        
    index=index+1

print(f"sum of numbers with even index is : {even_sum}")
print(f"sum of numbers with odd index is : {odd_sum}" ) 

