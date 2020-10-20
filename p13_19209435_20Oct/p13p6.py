#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 19:32:43 2020

@author: Hank.Da
"""

"""
pesudocode : 
    
    factorial : 
        
        if n = 0 , factorial(n) = 1
        if n>0 , factorial(n) = n*(n-1)! 
        
    main function :
        
        prompt user enter a positive integer number
        
        if number > 0 then
            using number as a argument for factorial function
            print factorial(number)
        else 
            print number must greater than 0
"""

def factorial(n,i):
    print('Round:',i)
    if n == 0:
        return 1
    else:
        i+=1
        print('n:',n)
        return n*factorial(n-1,i)
    
    
def main():
    
    num_inp = int(input("Enter a positive integer:"))
    
    if num_inp > 0:
        print("factorial(%d) : %d" %(num_inp,factorial(num_inp,0)))
    
    else:
        print("Enter number musr greater than 0")
    
main()