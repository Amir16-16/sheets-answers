# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 22:07:40 2025

@author: Amir
"""

USERS = {'user1': 'password1', 'user2': 'password2'}
name_input =input("enter the username : ")
pass_input =input("enter your passwrod : ")


if name_input in USERS and pass_input==USERS[name_input]:
     print("success.you are logged in !")
else:
     print("error! invalid username or password")