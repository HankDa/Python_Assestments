#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 13:46:38 2020

@author: Hank.Da
"""

"""
pesudocode:
    
    define find_sroot using number and epsilon as arguments
    
        initiate step = square(epsilon)
        initiate numGuess = 0
        initiate root = 0
        while (absolute number - square(root)) >= epsilon and root <= number
        do 
            root = root + step
            numGuesses += 1
            print Still running. Number of guesses:', numGuesses when numGuesses mod 100000 =0
        done
        
        print number of guesses
        if number - square(root) < epsilon
            print The approximate square root of number is root
        else
            print Failed to find a square root of number
            print Finished!
        
    define main
        prompt user enter number and tolerance
        execute find_sroot(number, tolerance)
        

"""

def find_sroot(number,epsilon):

    step = epsilon ** 2
    numGuesses = 0

    root = 0.0
    while abs(number - root ** 2) >= epsilon and root <= number:
        root += step
        numGuesses += 1
        if numGuesses % 100000 == 0:
            print('Still running. Number of guesses:', numGuesses) 
            
    print('Number of guesses:', numGuesses)
    if abs(number - root ** 2) < epsilon:
        print('The approximate square root of', number, 'is', root)
    else:
        print('Failed to find a square root of', number)
        print('Finished!')
    

def main():
    number = float(input('Enter the number for which you wish to calculate the square root:  '))
    tolerance = float(input('Enter the number for acceptable tolerance:  '))
    find_sroot(number,tolerance)

main()
