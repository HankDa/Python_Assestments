#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 21:01:43 2020

@author: Hank.Da
"""
"""
Prompt the user for a year Read the year
if year > 0: then
    if(year mod 4 = 0 and year mod 100 !=0) or year mod 400 =0: then
        print(year, 'is a leap year. ')
    else :
        print(year, 'is not a leap year.')
else:
        print( 'Year must be greater than 0. ')
print( 'Finished! ')
    

"""
year = int(input( 'Enter a year: '))
print('Year entered:', year)
if year >= 0:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0: 
        print(year, 'is a leap year. ')
    else :
        print(year, 'is not a leap year.')
else :
    print( 'Year must be greater than 0. ')
print( 'Finished! ')