# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 19:25:36 2025

@author: Amir
"""

number_of_runs = 0
total_time = 0

while True:
    x=input("enter your 10  km run time : ")
    if x !="0" and x != "" :   
     total_time+=float(x)
     number_of_runs+=1
    else:
        break


if number_of_runs > 0:
    average=total_time/number_of_runs
    print(f"average of {average} over {number_of_runs} runs ")
else:
    print("no run times added")


########################################### OR ###########################################
number_of_runs = 0
total_time = 0

while True:
    x=input("enter your 10  km run time : ")
    if x =="0" or x == "" :  
      break 
    else:
      total_time+=float(x)
      number_of_runs+=1


if number_of_runs > 0:
    average=total_time/number_of_runs
    print(f"average of {average} over {number_of_runs} runs ")
else:
    print("no run times added")