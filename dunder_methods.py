# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 00:27:42 2020
Magic methods or dunder methods@__ str__,__repr__
polymorphism :many form
@author: Ayush Gupta
"""


class phone: #base class 
    def __initt__(self, brand,model ,price):
        self.brand = brand
        self.model = model
        self.price=max(price,0) #sso as to reject non negative values
        
        
    def full_name(self):    #class fuction
              return f"{self.brand}{self.model}"
        # why?
    def __ str__(self): #print(str(my_phone))
              return f"{self.brand}{self.model}"
        
        
        
    def  __repr__(self):  #create a lsit on returning
            # for debuggers 
              return f"{self.brand}{self.model}& price is {self.price}"
    def  __len__(self):
        return len(self.phone_name())
    
    def  __add__(self,other):     #operrater overloading
        return self.price +other.price