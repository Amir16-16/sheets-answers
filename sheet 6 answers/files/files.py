# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 19:51:09 2025

@author: Amir
"""

# 1 Write a program that create a new file, then write Hello from file to the file.
# 2 Write a program that append your name to the previous file.
# 3 Write a program that write a list of numbers from 1 to 100 to the same file.
# 4 Read the lines from 50 to 60 and print it on the screen


with open ("newfile.txt","w") as file:
    file.write("Hello from file\n")
    
with open("newfile.txt","a") as file:
    file.write("amir\n")
    
with open('newfile.txt','a') as file :
  for number in range(1,101):
      file.write(f'{number}\n')
      
with open('newfile.txt','r') as file :
 lines= file.readlines()
 for j in range(49,60) : 
   print(lines[j].strip())