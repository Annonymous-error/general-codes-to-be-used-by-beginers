# -*- coding: utf-8 -*-
"""
Spyder Editor
DATE:19/04/2020
Information theory and coding
Title:(7,4) systematic cyclic codes Encoder
Author:Ayush gupta
17BEC02
IIIT Dharwad
 
"""

######################### ENCODER  ######################################################
import numpy as np 
import pandas as pd 

n=4
gen_p=[1, 1,0,1]                                        #generator polynomial used x^3+x^2+1
ip = list(map(int,input("\nEnter four message bits seperated by space  : ").strip().split()))[:n] 
print("data is- ",ip)

# Constructing polynomial   
datap= np.poly1d(ip)  
gp=np.poly1d(gen_p) 
#print ("data polynomial: ", datap)  
#print ("\ngenerator polynomial : \n", gp) 
intermediate=np.polymul([1,0,0,0],ip)
#print ("intermediate:- ", intermediate) 
intermediate_polynomial=np.poly1d(intermediate)
#print ("intermediate_poly:- ", intermediate_polynomial) 
quotient, remainder = np.polydiv(intermediate, gp) 
#print("\n\nquotient  : ", quotient) 
#print("remainder : ", remainder) 
remainder_2 = np.mod(remainder,2)
#print("remainder_mod: ", remainder_2) 

code=np.mod(np.polyadd(intermediate, remainder_2),2)
print("generated code is: ",code)

########################## Decoder  ######################################################3

rcvd_code=[1, 0, 1, 1, 1, 1, 0]
quotient2, syndrome = np.mod(np.polydiv(rcvd_code, gp),2) 

print("syndrome is: ",syndrome)
syndromedict={'110': '1000000','011':'0100000','111':'0010000','101':'0001000','100':'0000100','010':'0000010','001':'0000001','000':'0000000'}
s=''
for i in syndrome:
      s += str(int(i))
    
#print(s)   
for  s in syndromedict.keys() :
    e=syndromedict[s]


error=list(e.strip())
for i in range(0, len(error)): 
    error[i] = int(error[i]) 
  
decoded_code=np.mod(np.polyadd(rcvd_code, error),2)    
print("DECODED CODE IS: ",decoded_code)    
m=decoded_code[:4]
print("Message sent is ",m)
