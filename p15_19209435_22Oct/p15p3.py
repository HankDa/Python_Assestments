#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 17:57:27 2020

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

"""
Pesudocode : 
    
    fun1: 
        implement formula 
        
    main:
        prompt enter a positive integer number
        while number > 0
        
            print the number term of fun1 is fib(number)
            prompt enter a positive integer number
        print finished!
            
"""

ls_fib=[0,1]


def fun1(n):

    if n >= 0:
        
        if n ==0 :
           
            print('recusiton n =0 finished')
            print('n :',n)
            return 13
        
        elif n ==1 :
           
            print('recusiton n =1 finished')
            print('n :',n)
            return 8
        
        else:
            print('recusiton processing')
            print('n :',n)
            return (fun1(n-2) + (13*fun1(n-1)))
    else:
        print('enter number out of range')
    
        
def main():
    
    num_inp = int(input('Enter a positive integer greater or equal to 0:'))
    
    while(num_inp>=0):
        
        print("the %d term of fun1 is %d" %(num_inp,fun1(num_inp)))
        num_inp = int(input('Enter a positive integer greater or equal to 0:'))

    print('Finished!')
    
main()