# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 13:02:06 2024

@author: Meshewa
"""

# Python Program to print Floyd's Triangle

x=int(input('Please enter the number of rows :\n'))
i=1
print
("Floyd's Triangle")
for i in range(1,x+1):
    for j in range(1,i+1):
        print('*', end=' ')
        i=i+1
    print()