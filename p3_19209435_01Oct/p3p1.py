#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 15:01:46 2020

@author: Hank.Da
"""

#Currency exchange app - TWD to EUR

def convert_cur(orig_cur, rate):
    
    if orig_cur > 0:
    
        return orig_cur*rate
    else :
        print("The amount of currency must greater than 0!")

    
    

if __name__ == "__main__":
    
    TWD = 192094.35
    exchange_rate = 0.0294551086
    
    EUR = convert_cur(TWD,exchange_rate)
    
    print(str(TWD) + " TWD = " +str(EUR) +" EUR")