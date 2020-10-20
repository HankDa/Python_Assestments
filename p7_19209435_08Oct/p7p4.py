#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 21:33:26 2020

@author: Hank.Da
"""

"""
#pesudocode

while number < 5000 then
    total = total + number
    number = number +1 
print(total)
"""

i = 0
sum_ = 0
while i <5000:
#    print('number:',i)
    sum_ +=i
    i+=1

print('sum of first 5000 integers:',sum_)