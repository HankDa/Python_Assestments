#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 14:26:29 2020

@author: Hank.Da
"""

"""
Pesudocode :
     prompt user to input an integer
     
     for num1 in range 1 : entered number +1 
         for num2 in range 1 : entered number +1 
             print num1 multiply num2 
         
        change the print line
"""
num_inp = int(input('plz enter an integer:'))

for i in range(1,num_inp+1):
    for j in range (1,num_inp+1):
        print(i*j,end = ' ')
    print('\n')
