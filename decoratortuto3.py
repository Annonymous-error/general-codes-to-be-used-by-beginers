# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 02:11:07 2020

@author: Ayush Gupta
"""


from functools import wraps

def only_data_type_allow(data_type):
    def decoratpr(functon):
        @wraps(function)
        def wrapper(*args,**kwargs):
            if all([type(arg)==data_type for arg in args]):
                return function(*args,**kwargs)
            print('invalid arguments')
            return wrapper 
        return decorator
    
@only_data_type_allow(str)
def string_join(*args):
    string=''
    for i in args:
        string+=1
    
    return string
string_join('ayush','only_data_type_allow')