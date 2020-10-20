#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 14:17:47 2020

@author: Hank.Da
"""

"""
#pseudocode:
    
ask user enter two numbers.
sum up these two numbers
if the sum of numbers greater than 100
print : That is a big number!

"""

num_1 = int(input('plz enter 1st number :'))
num_2 = int(input('plz enter 2st number :'))

sum_12 = num_1+ num_2

if sum_12>100: print('That is a big number!')
else : print('the sum of these two numbers is :', str(sum_12))