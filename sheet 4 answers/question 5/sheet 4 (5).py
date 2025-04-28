# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 13:34:30 2025

@author: Amir
"""


def substitute(equation, **kwargs):
    for variable, value in kwargs.items():
        equation = equation.replace(variable, str(value))
    return equation

# Example usage:
    
# equation = "a + b - c"
result = substitute( "a + b - c", a=5, b=3, c=2)
print(result)  # Output: "5 + 3 - 2"