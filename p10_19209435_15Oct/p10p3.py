#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 17:30:50 2020

@author: Hank.Da
"""

"""
Pesudocode:
    
    define a vowel list
    
    while enter string not = ""
    
        prompt user enter a string
    
        define count list ={0}
        
        for i in range len(vowel list) 
            for character in entered string
                if character == vowels
                    count of vowels+=1
        
        print the count report
    
"""

ls_vowel = ['a','e','i','o','u']


while(True):
     
    str_inp = input('plz enter a string:')
    
    print('Entered string:', str_inp)
    
    ls_count =[0,0,0,0,0,0]
    
    if str_inp == '':
        
        print('Finished')
        
        break
    
    else:   
        
        for i in range(len(ls_vowel)):
            for ch in str_inp:
                if ch ==  ls_vowel[i]:
                    ls_count[i]+=1
                    
        for j in range(len(ls_vowel)):
            print('count %s: %d' %(ls_vowel[j],ls_count[j]))
    