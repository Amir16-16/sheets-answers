# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 23:02:10 2025

@author: Amir
"""
d1 = {'a': 1}
d2 = {'a': 2}
d3 = {'b': 3} 

# Given list of dictionaries
all_dicts = [d1, d2, d3]

# Initialize the final dictionary
fin_di = {}

# Iterate over each dictionary in the list
for d in all_dicts:
    # Update the final dictionary with the current dictionary
    fin_di.update(d)

# Print the result
print(fin_di)