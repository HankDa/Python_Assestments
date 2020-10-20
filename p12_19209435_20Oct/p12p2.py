#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 13:01:05 2020

@author: Hank.Da
"""

"""
pesudocode:

    Fibonacci : 
        
        initiate  Fibonacci list = [0,1]
        if n > 2 then 
            for i in range 2 to n
              Fibonacci list[i] = Fibonacci list[i-2] + Fibonacci list[i-1]  
        return Fibonacci list[0:n]
        
    main function :
        
        prompt user enter a positive integer number
        
        if number > 0 then
            using number as a argument for Fibonacci function
            print Fibonacci(number)
        else 
            print number must greater than 0

"""

def Fibonacci(n):
    
    list_fib = [0,1]
    
    if  n > 2:
        for i in range(2,n):
            list_fib.append(list_fib[i-2]+list_fib[i-1])
        
    return list_fib[0:n]


def main():
    
    num_inp = int(input("Enter a positive integer:"))
    
    if num_inp > 0:
        print("Fibonacci(%d) : %s" %(num_inp,str(Fibonacci(num_inp))))
    
    else:
        print("Enter number musr greater than 0")
    
main()

        