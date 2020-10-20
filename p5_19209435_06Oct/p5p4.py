#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 16:57:41 2020

@author: Hank.Da
"""

def main():
    
    input_int =int(input('plz enter a positive integer number: '))
    
    if input_int == 0:
        print("Number is zero")
        
    elif input_int >0 and input_int<= 20 : 
        print("Number is greater than 0 and less than or equal to 20")
        
    elif input_int >20 and input_int<= 40 : 
        print("Number is greater than 20 and less than or equal to 40")
    
    elif input_int >40 and input_int<= 60 : 
        print("Number is greater than 40 and less than or equal to 60")
    
    elif input_int >60 and input_int<= 80 : 
        print("Number is greater than 60 and less than or equal to 80")
        
    elif input_int >80 and input_int<= 100 : 
        print("Number is greater than 80 and less than or equal to 100")
        
    elif input_int >100 : 
        print("Number is greater than 100")
        
    
if __name__ == "__main__":
    main()