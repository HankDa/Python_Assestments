#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 14:43:08 2020

@author: Hank.Da
"""

init_amount = 192094.35

ratio = 0.6

tax_rate_large = 0.135
tax_rate_small = 0.23

total_tax = (init_amount*ratio*tax_rate_large)+(init_amount*(1-ratio)*tax_rate_small)

print("total_tax:", str(total_tax),"\n")

total_amount = init_amount + total_tax

print("total_amount:", str(total_amount),"\n")