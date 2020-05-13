
import numpy as np
import matplotlib.pyplot as plt


u=15;  

m=10;
g=10;
theta=np.arange(0,3.14/2,0.01)
F=(u*m*g)/(u*np.sin(theta)+np.cos(theta))
plt.plot(theta,F)
plt.xlabel('theata radian ')
plt.ylabel('force')
plt.title("F vs theta ")
plt.show()
# print(F)
minimum = np.min(F)
print( minimum)
# print( np.where(F == minimum))
print(theta[np.where(F == minimum)])
    



