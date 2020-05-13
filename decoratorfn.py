# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 00:57:17 2020
decorator fn inceases the functionality of a function
put *args and **kwargs in wrapper fn if calling a fn and giving arg
@author: Ayush Gupta
"""

@decorator_function 
def decorator_function(any_function):
    def wrapper_function():
        print('this is a good fn')
        return any_function(*args, **kwargs)
    return wrapper_function()


@decorator_function 
def func1():
    print('this is fn 1')


def func2():
    print('this is fn 1')
    
     
# v=decorator_function(func1)
# v()
    
###############doc string
from functools import wraps    
@decorator_function 
def add(a,b):
    '''this is add fn'''  ###doc string
    return  a + b


print(add.__doc__)

