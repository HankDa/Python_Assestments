#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 17:14:02 2020

@author: Hank.Da
"""
"""
Pesudocode:
    
    while enter integer not< 0
    
        prompt user enter a integer
        
        if entered number not = 0 then
            while square root**2 < abs entered number
                square root +=1
            
            if square root**2 = entered number then
                print square root of entered number: square root
                
            else
                print Could not found square root of entered number
"""

while(True):
    num_inp = int(input("plz enter a positive integer:"))
    squr_root = 0
    
    if num_inp >=0:
        while((squr_root**2) <num_inp):
            print('Seaching for square root:' ,squr_root)
            squr_root+=1
        
        if (squr_root**2) == num_inp :
            print('square root of entered number: ', squr_root)
        else:
            print('Could not found square root of', num_inp)
    else: break