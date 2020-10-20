#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 14:36:09 2020

@author: Hank.Da
"""

"""
Pesudocode :
     prompt user to enter an integer
     
     print Times enterd number
     
     for num1 in range 1 : 20 +1 
        print 
        print num1 and num1 multiply enterd number 

"""

num_inp = int(input('plz enter an integer:'))
    
print('Times %d Table' %(num_inp))
for i in range(1,21):
    print(i,i*num_inp)

    