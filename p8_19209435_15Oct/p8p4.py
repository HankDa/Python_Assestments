#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 14:54:55 2020

@author: Hank.Da
"""

"""
Pesudocode :
     
     
    while(flag == True)
         prompt user to enter an integer
         
         if entered number < 0 then
             flag = False
             print analyze report
         else then
             check enterd number in each range and count +=1
             print the range of entered number

"""


flag = True
count0, count1, count2, count3 ,count4 ,count5, count6 = 0,0,0,0,0,0,0

while(flag):

    num_inp = int(input('plz enter an integer:'))
    
    if num_inp < 0:
        flag = False
        print('Number of numbers equal to 0:',count0)
        print('Number of numbers in range(1,21):',count1)
        print('Number of numbers in range(21,41):',count2)
        print('Number of numbers in range(41,61):',count3)
        print('Number of numbers in range(61,81):',count4)
        print('Number of numbers in range(81,101):',count5)
        print('Number of numbers biger than 100:',count6)
    else:
        if num_inp == 0:
            print("Number is equal to 0")
            count0 += 1
            
        elif num_inp >0 and num_inp<= 20 : 
            print("Number is greater than 0 and less than or equal to 20")
            count1 += 1
        elif num_inp >20 and num_inp<= 40 : 
            print("Number is greater than 20 and less than or equal to 40")
            count2 += 1
        elif num_inp >40 and num_inp<= 60 : 
            print("Number is greater than 40 and less than or equal to 60")
            count3+= 1
        elif num_inp >60 and num_inp<= 80 : 
            print("Number is greater than 60 and less than or equal to 80")
            count4 += 1
        elif num_inp >80 and num_inp<= 100 : 
            print("Number is greater than 80 and less than or equal to 100")
            count5 += 1
        elif num_inp >100 : 
            print("Number is greater than 100")
            count6 += 1
