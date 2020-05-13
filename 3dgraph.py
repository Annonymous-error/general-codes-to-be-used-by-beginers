# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from mpl_toolkits import mplot3d

import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
ax = plt.axes(projection='3d')
ax = plt.axes(projection='3d')

def f(x, y):
    return (np.sqrt(x*x +y*y)+np.sqrt((8-x)*(8-x) +y*y)+np.sqrt((8-y)*(8-y) +x*x)+np.sqrt((8-x)*(8-x) +(8-y)*(8-y)))

x = np.linspace(0, 8, 10)
y = np.linspace(0, 8, 10)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax.set_title('surface');


b =min([min(p) for p in Z]) 
print(b)
  
