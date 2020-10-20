#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 16:52:58 2020

@author: Hank.Da
"""

def main():
    
    input_int =float(input('plz enter a floating-point number: '))
    
    if input_int > 0:
        print("input_int : Positive number")
        
    elif input_int< 0: 
        print("input_int : Negative number")
        
    else :
        print("input_int : Zero")
        
if __name__ == "__main__":
    main()