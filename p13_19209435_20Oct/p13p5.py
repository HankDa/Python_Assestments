#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 19:31:09 2020

@author: Hank.Da
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 19:00:40 2020

@author: Hank.Da
"""

"""
Pesudocode: 
    
    Function implment
    
    Scope of varibles in f(x) is local scope which means that it will useless out of function.
    while z = f(x) means it return a number and assign to z, it could effect the global variables.
    
"""

# Program to illustrate scoping in Python
def f(x):
    print('In function f:')
    x += 1
    y=1
    z =y
    a =10
    print('x is', x)
    print('y is', y)
    print('z is', z)
    print('a is', a)
    return x

x, y, z = 5, 10, 15
a = 1
print('Before function f:')
print('x is', x)
print('y is', y)
print('z is', z)
print('a is', a)

z = f(x)
print('After function f:')
print('x is', x)
print('y is', y)
print('z is', z)
print('a is', a)