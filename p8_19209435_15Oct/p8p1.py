#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 14:09:15 2020

@author: Hank.Da
"""

"""
pesudocode :
    while(flag = true) then
        prompt user to input an integer
        print enterd number 
        
        if enterd number >= 0 then
            for num in list[2,3,5,7]
                if enterd number mod num == 0 then
                    print enterd number is divisble by num
                
                else 
                    flag = False
                    print Finished!
"""

flag = True

num_div = [2,3,5,7]

while(flag):
    
    num_input = int(input('plz enter an integer:'))
    print('entered number:',str(num_input))
    
    if num_input >= 0:
        for i in num_div:
            if num_input % i ==0:
                print(str(num_input),'is divisble by',str(i))
    else:
        flag = False
        print('Finished!')
        
    
    