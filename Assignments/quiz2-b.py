# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 13:42:40 2024

@author: Daniel-Caleb

            DANIEL-CALEB CHERUIYOT
                21/05045
            CAT ONE! - QUIZ 1-b
"""
carprices = [
    ('Toyota PREMIO', 1749999),
    ('Honda Fit', 1280000),
    ('Toyota Landcruiser Prado TX', 7599999),
    ('Subaru FORESTER', 2099999),
    ('BMW M4 Competition', 7100000),
    ('Audi A4', 3449999),
    ('Mercedes-Benz E250', 3349999),
    ('Lexus LX570', 13690000),
    ('Mazda CX-5', 3329999),
    ('Isuzu DMAX', 1799999)
]
print(carprices)

totalcost = carprices[0][1] + carprices[-1][1]
print("Total cost of the first and last car:",totalcost)
