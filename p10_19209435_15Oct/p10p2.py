#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 17:26:29 2020

@author: Hank.Da
"""

"""
Pesudocode:
    
    
    while enter integer not< 0
    
        prompt user enter a integer
        
        if entered number not = 0 then
            while cube_root**3 < abs entered number
                cube_root +=1
            
            if cube_root**3 = abs entered number then
                if entered number < 0 then
                    cube_root *= -1
                print cube root of entered number: cube_root
            else
                print Could not found cube root of entered number
"""


while(True):
    num_inp = int(input("plz enter an integer:"))
    cube_root = 0
    
    if num_inp !=0:
        while((cube_root**3) <abs(num_inp)):
            cube_root+=1
        
        if (cube_root**3) == abs(num_inp) :
            if num_inp < 0:
                cube_root *= -1
            print('cube root of entered number: ', cube_root)
        else:
            print('Could not found cube root of', num_inp)
            
    else: break