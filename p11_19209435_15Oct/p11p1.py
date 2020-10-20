#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 18:25:39 2020

@author: Hank.Da
"""

"""
Pesudocode:
    prompt user to input a integer
    
    if entered number < 0
        print Error: Number entered was less than 0.
    
    else
        fact =1
        for i in range 1 to entered number+1
            fact *=i
        
        print "Factorial of", number, "is", fact
    
    print("Finished!")
    
"""

number = int(input("Enter the number for which you wish to calculate the factorial (an int >= 0):"))
if number < 0:
    print("Error: Number entered was less than 0.")

else:
    fact = 1
    for i in range(1, number + 1): 
        fact *= i
        
    print("Factorial of", number, "is", fact)
    
print("Finished!")