#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 18:05:03 2020

@author: Hank.Da
"""
"""
Pesudocode:
    
    function implement 

"""

def max(a, b):
    if a > b:
        return a
    else:
        return b 

# Program to print out the largest of two numbers entered by the user # Uses two functions: max and print_max
def print_max():

    # Prompt the user for two numbers
    number1 = float(input('Enter a number: ')) 
    number2 = float(input('Enter a number: ')) 
    print('The largest of', number1, 'and', number2,'is', max(number1, number2))
    return

print(print_max)
print(hex(id(print_max)))
    
