#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 15:50:16 2020

@author: Hank.Da
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 15:47:16 2020

@author: Hank.Da
"""
"""
Pesudocode:
    
    while(True)
        promp user enter a positive number
        
        if entered number >= 0 then
            for i in range(entered number+1)
                Factorial = Factorial * i
                print Factorial
        elif entered number = 1 then
            print Factorial = 1
        
        else 
            print Finished!
            Break
"""

while(True):

    num_inp = int(input("plz enter a positive number:"))
    print('entered number',num_inp)
    total=1
    if num_inp>=0:
        for i in range(1,num_inp+1):
            total *= i
        print("Factorial:", total) 
    elif num_inp ==0:
    
        print("Factorial:", 1) 
    else:
        print('Finished')
        break