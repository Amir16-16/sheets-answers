# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 20:05:58 2025

@author: Amir
"""

x_coor = [1, 2, 3, 4, 5]
y_coor = [2, 4, 6, 8, 10]
z_coor = [0, -1, -2, -3, -4]

points = [(x, y, z) for x, y, z in zip(x_coor, y_coor, z_coor)]
print(points)

### the output : [(1, 2, 0), (2, 4, -1), (3, 6, -2), (4, 8, -3), (5, 10, -4)] 
####################### same as #############################

w=zip(x_coor, y_coor, z_coor)
print(list(w))