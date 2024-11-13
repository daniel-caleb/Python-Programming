# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 12:23:50 2024

            DANIEL-CALEB CHERUIYOT
                21/05045
            CAT ONE! - QUIZ 2
"""
def print_prime_numbers(n):
  for num in range(2, n+1):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
      if num % i == 0:
        is_prime = False
        break
    if is_prime:
      print(num, end=",")
number = int(input("Enter a number: "))
print_prime_numbers(number)