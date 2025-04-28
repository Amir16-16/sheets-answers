# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 13:54:56 2025

@author: Amir
"""

fl_num = 1234.5678
bef_int_num = 2
aft_int_num = 3

# Convert the float to a string to manipulate the digits
fl_num_str = str(fl_num)

# Split the string into the integer and decimal parts
integer_part, decimal_part = fl_num_str.split('.')

# Extract the required digits before and after the decimal point
new_integer_part = integer_part[bef_int_num:]   #[34]  #str
new_decimal_part = decimal_part[:aft_int_num]    #[567] #str

# Combine the new parts into a new float
new_float_str = new_integer_part + '.' + new_decimal_part  #str
new_float = float(new_float_str)

print(new_float)
print(type(new_float))