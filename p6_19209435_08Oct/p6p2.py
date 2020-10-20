#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 14:32:39 2020

@author: Hank.Da
"""

"""
#pseudocode:
    
ask user enter three int numbers

if the number is odd number: then put the number in list
    find the largest number in the list by compare current number and temporary largest number
    print(largest number is: num_largest)
if there are no odd numbers : 
    print(All the numbers are even numbers)



"""


ls_odd =[]


num1 = int(input('plz enter 1st number :'))
num2 = int(input('plz enter 2st number :'))
num3 = int(input('plz enter 3th number :'))

ls_num =[num1,num2,num3]

for i in range(len(ls_num)):
    if (ls_num[i]%2): ls_odd.append(ls_num[i])

if (len(ls_odd)):
    num_largest = ls_num[0]
    for num_test in ls_num:
        if num_test >= num_largest:
            num_largest=num_test
    print('largest number is:', str(num_largest))
        
        
else: print('All the numbers are even numbers')