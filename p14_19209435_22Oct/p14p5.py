#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 16:38:40 2020

@author: Hank.Da
"""

"""
Pesudocode: 
    
    function fib :
        implement Fibonacci formula
        
    function main:
        prompt enter a positive integer number
        while number > 0
        
            print the number term of Fibonacci is fib(number)
            prompt enter a positive integer number
        print finished!
            

"""

ls_fib=[0,1]


def fib(n):

    if n ==1 :
        print('recusiton finished')
        print('n :',n)
        return 0
    elif n == 2:
        print('recusiton finished')
        print('n :',n)
        return 1
    else:
        print('recusiton processing')
        print('n :',n)
        return fib(n-2)+fib(n-1)
    
        
def main():
    
    num_inp = int(input('Enter a positive integer:'))
    while(num_inp>0):
        
        print("the %d term of Fibonacci is %d" %(num_inp,fib(num_inp)))
        num_inp = int(input('Enter a positive integer:'))

    print('Finished!')
    
main()
        
        