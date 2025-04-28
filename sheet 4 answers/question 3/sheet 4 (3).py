# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 13:25:48 2025

@author: Amir
"""
family_names=["amir","emad"]
unique_letters = {letter for name in family_names for letter in name}
print(unique_letters)
   



################# This is equivalent to: ################


# family_names=["amir","emad"]
# unique_letters = set()  
# for name in family_names:
#     for letter in name:
#         unique_letters.add(letter)
# print(unique_letters)
        
