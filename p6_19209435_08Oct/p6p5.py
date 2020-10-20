#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 15:47:46 2020

@author: Hank.Da
"""

"""
#pseudocode 

if enter password == correct password:
    print('You have successfully logged in')
else:
    print('password incorrect')
    print('Plz enter correct passwaord three times')
    for loop 3 times:
        if enter password == correct password:
            count of correct password +=1
    if  count of correct password ==3:
        print('You have successfully logged in')
    else:
        print('You have been denied access.') 
"""

password_default = '1234abcd'
count = 0

pw_input = input('plz enter password:')
if pw_input == password_default:
    print('You have successfully logged in')
else:
    print('password incorrect')
    print('Plz enter correct passwaord three times')
    for i in range(3):
        pw_input = input('plz enter password:')
        if pw_input == password_default:
            count += 1
    
    if count==3:
         print('You have successfully logged in')
    else: 
         print('You have been denied access.')
