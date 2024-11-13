# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 11:44:58 2024

            DANIEL-CALEB CHERUIYOT
                21/05045
            CAT TWO! - QUIZ 1
"""
def sum_and_average():
    total = 0
    count = 0
    while True:
        number = float(input("Enter a number (0 to stop): "))
        if number == 0:
            break
        total += number
        count += 1
    if count == 0:
        print("No numbers entered.")
    else:
        average = total / count
        print(f"Sum: {total}, Average: {average}")

sum_and_average()
