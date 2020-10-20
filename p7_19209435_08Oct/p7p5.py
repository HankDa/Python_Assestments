#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 21:40:20 2020

@author: Hank.Da
"""

"""
#pesudocode

for number in 1-10000 than
    if number mod 3 =0 or number mod 5=0 then
        total = total + number
print(total)
"""

i = 0
sum_ = 0
for i in range(1,10001):
    if i%3==0 or i%5==0:
        sum_ +=i
print('total:',sum_)

