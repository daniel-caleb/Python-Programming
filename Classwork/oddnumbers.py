# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 13:19:59 2024

@author: Meshewa
"""

#python program to use while loop to print odd numbers from 3 to a number x
x=int(input('Enter limit:\n'))
print('----Begin-------')
i=3 #initialize
while (i <x):
    print(i,end=',')
    i=i+2 #update
print('\n----End-------')
