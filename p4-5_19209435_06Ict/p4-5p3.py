#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 13:33:46 2020

@author: Hank.Da
"""

import math 

def main():
    
    init_amount = float(input("plz type float_value: "))
    
    if init_amount >=0:
        
        print("init_amount :", str(init_amount),"\n")
        
        ratio = 0.6
        
        tax_rate_large = 0.135
        tax_rate_small = 0.23
        
        tax_l = init_amount*ratio*tax_rate_large
        tax_s = init_amount*(1-ratio)*tax_rate_small
        
        total_tax = tax_l + tax_s
        total_nett_income = init_amount-total_tax
        
        print("tax_large:", str(tax_l),"\n")
        print("tax_small:", str(tax_s),"\n")
        print("total_tax:", str(total_tax),"\n")
        print("total_nett_income:", str(total_nett_income),"\n")
        
    
    else:
        print("Amount of income must be >= 0.")
    
if __name__ == "__main__" :
    main()