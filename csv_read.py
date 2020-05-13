# -*- coding: utf-8 -*-
"""
Created on Sun May 10 23:37:57 2020

@author: Ayush
"""


import csv
import matplotlib.pyplot  as plt
X=[]
Y=[]
with open("OldFaithfulData.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    for lines in csv_reader:
        X.append(float(lines['eruptions']))
        Y.append(float(lines['waiting']))    
        
plt.scatter(X,Y,color='g')
plt.show()