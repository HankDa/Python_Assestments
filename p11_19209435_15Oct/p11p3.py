#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 19:30:38 2020

@author: Hank.Da
"""

"""
Pesudocode:
    define a list list_fib = [0,1]

    while entered number > 0
    
        prompt user to enter an integer greater than 1
    
        if entered number greater than 0 then
        
            if Fibonacci Series less than target length then
                for i in range length of list_fib to entered number
                    Fibonacci Series append (list_fib[i-2] + list_fib[i-1])
                    i+=1
            
            print list_fib[0: entered number]
            
        else then
            print Finished!
"""

while(True):
    
    list_fib = [0,1]
    num_inp = int(input("Enter an integer greater than or equal to 1:"))
    
    if num_inp >0:
        
        if(len(list_fib) < num_inp):
            for i in range(len(list_fib),num_inp):
               list_fib.append(list_fib[i-2] + list_fib[i-1])
               i+=1
    
        print(list_fib[:num_inp])
        
    else:
            
        print("Finished!")
        break