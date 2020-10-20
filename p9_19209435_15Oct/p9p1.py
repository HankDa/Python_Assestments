# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
Pesudocode:
    prompt user enter a positive number
    count = 0
    total = 0
    while count <= entered number then
        total + = count
        count + = 1
    print total
"""

num_inp = int(input("plz enter a positive number:"))
count ,total= 0,0

while(count <= num_inp):
    total += count
    count +=1
print("total:", total)    