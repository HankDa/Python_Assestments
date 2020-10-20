#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 15:25:36 2020

@author: Hank.Da
"""
"""
#pseudocode 

while(chances of enter password > 0):
    if enter password == correct password:
        chances of enter password= 0
        print('You have successfully logged in')
    else enter password is incorrect:
         chances of enter password -=1
         print('password incorrect')
         if chances of enter password == 0:
         print('You have been denied access.') 
"""

password_default = '1234abcd'
count = 3

while(count>0):
    pw_input = input('plz enter password:')
    if pw_input == password_default:
        count = 0 
        print('You have successfully logged in')
    else:
        count-=1
        print('password incorrect')
        print('You have', count ,'chances left')
        if count==0 : 
            print('You have been denied access.')
        
    