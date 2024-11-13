# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 13:19:35 2024

@author: Meshewa
"""

#A python program to generate 10 random numbers upper(),lower(),len() and replace().
print('Enter your first name:')
x=input()
print('Enter last name:')
y=input()
print('Your full name is: ',x+y)
a=x.upper()
b=y.lower()
c=len(x)
d=x.replace(x,'Lec.') #old string x is replaced
print('First name in upper case:',a)
print('Last name in lowercase:',b)
print('Length of first name: ',c)
print('First name replaced:',d)
print('The new name is:',d,'',y)
print('The original name is :',x,' ',y)
