# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 11:40:14 2020

@author: Ayush Gupta
"""
def generator(n):
    for number in range(2,n+1,2):
        yield(number)


even_number=generator(20)
for num in even_number:
    print(num)


# for generator comprehension print(next(square))
    square=(i**2 for i in range(1,11))
    for numb in square:
        print(numb)
           