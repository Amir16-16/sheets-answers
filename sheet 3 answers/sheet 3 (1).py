# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 18:50:56 2025

@author: Amir
"""

# Your code here
number_of_runs = 0
total_time = 0
x=input("enter your 10  km run time : ")
while x !="0" and x != "" :
    total_time+=float(x)
    number_of_runs+=1
    x=input("enter your 10  km run time : ")
else:
    pass

if number_of_runs > 0:
    average=total_time/number_of_runs
    print(f"average of {average} over {number_of_runs} runs ")
else:
    print("no run times added")


    
  
 