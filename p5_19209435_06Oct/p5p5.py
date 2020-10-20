#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 17:18:15 2020

@author: Hank.Da
"""
def find_city(city):
    
    ls_Leinster=["Leinster","Dublin","Kilkenny"]
    ls_Munster= ["Munster","Cork","Limerick","Waterford"]
    ls_Ulster=  ["Ulster","Belfast","Lisburn","Derry"]
    ls_Connacht=["Connacht","Galway","Sligo"]
    
    ls_all = [ls_Leinster ,ls_Munster, ls_Ulster, ls_Connacht]

    for ls_province in ls_all:
        for i in range(len(ls_province)-1):
            if city == ls_province[i+1]:
                print ("You entered :", city+".", city,"is in", ls_province[0])
                return 1
            
    return 0

def main():
    
    input_city = input("Plz enter a city name: ")

    if find_city(input_city):
        print("Finished")
    else:
        print("Sorry, I didn’t recognise that name")

    
if __name__ == "__main__" :
    main()