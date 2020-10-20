#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 13:14:38 2020

@author: Hank.Da
"""
def main():
    
    input_currency =float(input('plz type in amount of TWD to exchange to EUR: '))
    print("input_currency : ", str(input_currency) , "TWD")
    if input_currency>=0:
    #TWD to EUR
        excahge_rate = 0.029
        output_currency = input_currency*excahge_rate
        print("output_currency : " , str(output_currency) ,"EUR")
    else: 
        print("Amount must be >= 0. Please try again.")
    
    
if __name__ == "__main__":
    main()