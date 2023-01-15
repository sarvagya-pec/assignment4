# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 00:27:17 2023

@author: LENOVO
"""

year = int(input("Enter the year:"))
if year%100 ==0:
    if year%400 ==0:
        print("This year is a leap year")
    else:
                   print("This is not a leap year")
else:
    if year%4 ==0:
        print("This is a leap year") 
        
    else:
        print("This is not a  leap year")