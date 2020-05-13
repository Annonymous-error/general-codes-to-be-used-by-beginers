# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 00:13:43 2020


Multilevel inheritece



@author: Ayush Gupta
"""
class A: #base class 
        def class_a_method(self):
            return 'i\'m just a method'
        
        
        def hello(self):    #class fuction
            return 'hello from class A'
        
class b: #base class 
        def class_b_method(self):
            return 'i\'m just a method'
                
        
        def hello(self):    #class fuction
            return 'hello from class b'
        
        
class c(A,b):  #Now class c has all methods of class a & class b
     pass
    # method resolution order c a b
        
 
print(c.mro())
         
