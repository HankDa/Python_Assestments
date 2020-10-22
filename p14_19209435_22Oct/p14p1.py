#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 14:21:23 2020

@author: Hank.Da
"""

import time
import sys

sys.setrecursionlimit(3000)
#
print(sys.getrecursionlimit())

def factorial_nr(num_inp):
    total = 1
    
    if num_inp>0:
        for i in range(1,num_inp+1):
            total *= i

    else:
        total = 1
    
    return total


def factorial_r(n):
    if n == 0:
        return 1
    else:
        return n*factorial_r(n-1)
    
def main():
    num_inp = 10000
    
    time_nr = time.time()
    
    factorial_nr(num_inp)
    
    time_nr = time.time()-time_nr
    print('non-recursive factorial run (%d)! , run time: %s sec' %(num_inp,str(time_nr)))
    
    time_r = time.time()
    
    factorial_r(num_inp)
    
    time_r = time.time()-time_r
    print('recursive factorial run (%d)! , run time: %s sec' %(num_inp,str(time_r)))
    
main()