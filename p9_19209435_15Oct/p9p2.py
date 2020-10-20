#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 15:21:45 2020

@author: Hank.Da
"""

"""
Pesudocode:
    promp user enter a positive number
    
    if entered number >= 0 then
        for i in range(entered number+1)
            total = total + 1
            print total
    else
        print Finished
"""
total=0


while(True):

    num_inp = int(input("plz enter a positive number:"))
    print('entered number',num_inp)
    if num_inp>=0:
        for i in range(num_inp+1):
            total += i
        print("total:", total)  
    else:
        print('Finished')
        break