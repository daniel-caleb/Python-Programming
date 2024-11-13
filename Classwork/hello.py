# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 12:11:50 2024

@author: Meshewa
"""

savings=100
rate=1.1
desc="compund interest"
year1=savings*rate
result=savings*rate**7
print(year1)
print(type(year1))
doubledesc=desc+desc
print(doubledesc)
print("I started with $"+str((savings))+" and now have $"+str((result))+". Awesome!")

pi_string="3.1415926"
pi_float=float((pi_string))
print(pi_string)
print(type(pi_string))
print(pi_float)
print(type(pi_float))