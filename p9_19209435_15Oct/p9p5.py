#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 16:39:24 2020

@author: Hank.Da
"""

"""
    def factorial (entered number): 
        if entered number >= 0 then
        for i in range(entered number+1)
            Factorial = Factorial * i
            print Factorial
        elif entered number = 1 then
            print Factorial = 1
   
    promp user enter a positive number : k
    promp user enter a positive number : n
    
    if n < k then
        print n must > k
    
    else
        nck = n!/(k!(n-k)!)
        print nck

        
"""

def factorial(num_inp):
    total = 1
    if num_inp>0:
        for i in range(1,num_inp+1):
            total *= i

    elif num_inp ==0:
        total = 1
    else:
        print('num_inp should > 0')
        total = 0
    
    return total

def main():
    
    k = int(input('plz enter k:'))
    n = int(input('plz enter n:'))
    if n< k:
        print('n must > k')
        
    else:
        nck = int(factorial(n)/(factorial(k)*factorial(n-k)))
        
        print('nck:' , nck)
    
main()