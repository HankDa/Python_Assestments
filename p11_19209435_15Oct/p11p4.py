#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 19:44:20 2020

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
            
    def main()
    
        promp user enter an integer n
        cn = factorial(2*n)/(factorial(n+1)*factorial(n))
        print cn 
        
     
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
    
    n = int(input('Enter an iteger:'))
    
    cn = factorial(2*n)/(factorial(n+1)*factorial(n))
    
#    print(2*factorial(n))
#    print(factorial(n+1)*factorial(n))
    
    print("C%d : %d" %(n,cn))
    
main()
    