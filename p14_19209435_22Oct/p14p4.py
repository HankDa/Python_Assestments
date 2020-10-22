#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 16:11:37 2020

@author: Hank.Da
"""

"""
Pesudocode:
   
    initiate flag = False
    
    for number in range 2 to enterd number
        divide number by each number(i) in range
            if number mod i == 0 then
                print number, 'equals', i, '*', number//
                flag = True
        
        if flag == False then 
            print number is a prime number
    
    print finished!

"""

def find_primeNum(num_inp):
    flag = False
    # Look for prime numbers in a range of integers
    for number in range(2, num_inp):
        for i in range(2, number): 
            if number % i == 0:
                print(number, 'equals', i, '*', number//i)
                # To indicate number satisify the condition at least once
                flag = True
            
        if(flag): flag = False
        else: print(number, 'is a prime number')
                
    print('Finished!')
    
find_primeNum(20)