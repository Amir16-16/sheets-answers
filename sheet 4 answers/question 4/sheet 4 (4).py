# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 12:37:59 2025

@author: Amir
"""

def average(*numbers):
    return sum(numbers) / len(numbers)


# Example usage:

avg = average(10,20,3,4,4,5,2,1,4)
print(f"The average is: {avg}")

