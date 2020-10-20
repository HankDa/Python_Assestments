#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 15:05:28 2020

@author: Hank.Da
"""
"""
#pseudocode:

ask user enter their name
if user name equal my name:
    print('That is a cool name!')
elif user name equal virtual name:
    print('Is that your real name?')
else:
    print('You have a nice name.')
    

"""


myName ='Hank'
virtualName =['Mickey Mouse','Spongebob Squarepants']

name_input = input('plz enter your name:')

if name_input == myName: 
    print('That is a cool name!')
elif name_input == virtualName[0] or name_input == virtualName[1]:
    print('Is that your real name?')
else: 
    print('You have a nice name.')
