# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 00:49:31 2020

@author: Ayush Gupta
"""


#name error : variable not defined
#type error : adding 5 + a
# index error :wrong index
# value error: 
s='abc'
print(int(s))   #abc is not integer

# attribute error :when we use a function that is not defined 
# key error :no key present in dict and we are using it
raise TypeError('') #raise error instead of printing  strings
raise IndexError('')


# NotImplementedError:to force to define a method to each class
def any_func(self):
    # in parent class
    #abstract method @from java
raise NotImplementedError('') 

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''#


# exception are those errors which are faced during program execution
while True:   
  try:
    #write line prone to error
    break
  except"type of error":
        print('invalid input')    
###########################################
 while True:   
  try:
    #write line prone to error
    break
  except"type of error":
        print('invalid input') 
    else: #when try executes succesfully
        # write those line which you want to write in try block
        break
    finally :# it will execute irrespective of error  
        # write any thing
        
# '''''''''''''''''''''''''''''''''''''''''
class Custom_error(ValueError):  #(inherited class)
    pass