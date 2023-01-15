# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 00:14:26 2023

@author: LENOVO
"""

marks = int(input("Enter your marks : "))
if marks>=80:
    grade='A'
elif marks >=60:
    grade='B'
elif marks >=50:
        grade='C'
elif marks >=45:
    grade='D'
elif marks >=25:
    grade='E'
else:
    grade = 'F'
    
print("Your grade is "+grade)    
    