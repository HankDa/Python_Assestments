#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 16:02:04 2020

@author: Hank.Da
"""

"""
Pesudocode:
    function implement

"""

# Look for prime numbers in a range of integers
for number in range(2, 20):
    for i in range(2, number): 
        if number % i == 0:
            print(number, 'equals', i, '*', number//i)
            break

    else:
        # loop fell through without finding a factor
        print(number, 'is a prime number')
            
print('Finished!')