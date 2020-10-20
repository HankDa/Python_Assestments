#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 19:00:40 2020

@author: Hank.Da
"""

"""
Pesudocode: 
    
    Function implment
"""

# Program to illustrate scoping in Python
def f(x):
    print('In function f:')
    x += 1
    y=1
    print('x is', x)
    print('y is', y)
    print('z is', z)
    return x

x, y, z = 5, 10, 15
print('Before function f:')
print('x is', x)
print('y is', y)
print('z is', z)

z = f(x)
print('After function f:')
print('x is', x)
print('y is', y)
print('z is', z)