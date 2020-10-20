#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 14:24:27 2020

@author: Hank.Da
"""
import math 

print("plz type float_value:")

float_value = float(input())

print("float_value :", str(float_value),"\n")

# 1. area_square
area_square = math.pow(float_value,2)

# 2. volume_cube
volume_cube = math.pow(float_value,3)

# 3. area_circle
area_circle = math.pow(float_value/2,2)*math.pi

# 4. volume_sphere
volume_sphere = (4/3)*math.pow(float_value,3)*math.pi

# 5. volume_cylinder
volume_cylinder = math.pow(float_value,3)*math.pi


print("1. area_square:" , str(area_square),'\n')
print("2. volume_cube:" , str(volume_cube),'\n')
print("3. area_circle:" , str(area_circle),'\n')
print("4. volume_sphere:" , str(volume_sphere),'\n')
print("5. volume_cylinder:" , str(volume_cylinder),'\n')