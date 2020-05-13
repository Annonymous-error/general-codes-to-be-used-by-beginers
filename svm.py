# -*- coding: utf-8 -*-
"""
Created on Sat May  2 11:59:57 2020

@author: Arun Chauhan, IIIT Dharwad

Algorithm:       Support Vector Machine 
"""
import numpy as np
import matplotlib.pyplot as plt
from cvxopt import matrix as cvxopt_matrix
from cvxopt import solvers as cvxopt_solvers



def dataSet():
    '''Data set '''
    x_neg = np.array([[3,4],[1,4],[2,3]])
    y_neg = np.array([-1,-1,-1])
    x_pos = np.array([[6,-1],[7,-1],[5,-3]])
    y_pos = np.array([1,1,1])
    X = np.vstack((x_pos, x_neg))
    y = np.concatenate((y_pos,y_neg))
    y = y.reshape(-1,1)
    return X,y,x_neg,x_pos
    
def dualOptimizer(H,m,y):
    '''Converting the parameters to standard format for the optimizer function cvxopt_solvers.qp(P, q, G, h, A, b)'''
    H = H*1.0   # Multiply 1.0 to convert all values into float
    y = y*1.0   # Multiply 1.0 to convert all values into float
    P = cvxopt_matrix(H)
    q = cvxopt_matrix(-np.ones((m, 1)))
    G = cvxopt_matrix(-np.eye(m))
    h = cvxopt_matrix(np.zeros(m))
    A = cvxopt_matrix(y.reshape(1, -1))
    b = cvxopt_matrix(np.zeros(1))
    
    #Setting solver parameters (change default to decrease tolerance) 
    cvxopt_solvers.options['show_progress'] = False
    cvxopt_solvers.options['abstol'] = 1e-10
    cvxopt_solvers.options['reltol'] = 1e-10
    cvxopt_solvers.options['feastol'] = 1e-10
    
    #Run solver
    sol = cvxopt_solvers.qp(P, q, G, h, A, b)
    alphas = np.array(sol['x'])
    return alphas
    

''' Implementing SVM hard margin '''
'''Converting second term of dual objective function into standard form, a.T*H*a for the optimizer'''
X,y,x_neg,x_pos = dataSet()
k = np.dot(X,X.T)
t = np.dot(y,y.T)
H = k*t              
m,n = X.shape

alphas = dualOptimizer(H,m,y)


#w parameter in vectorized form
w = ((y * alphas).T @ X).reshape(-1,1)

#Selecting the set of indices S corresponding to non zero parameters
S = (alphas > 1e-4).flatten()

#Computing b
b = np.average(y[S] - np.dot(X[S], w))

#Display results
print('Alphas: ',alphas,'\n Support Vectors: ',S.reshape(-1,1))
print('Alphas for Support Vectors = ',alphas[alphas > 1e-4])
print('w = ', w.flatten())
print('b = ', b)



fig = plt.figure(figsize = (10,10))
x1 = np.linspace(-1,10).reshape(-1,1)
x2 = -(w[0]*x1 + b)/w[1]
plt.plot(x1,x2)

'''margin hyperplanes'''
b_margin = - np.dot(X[S], w)
x2 = -(w[0]*x1 + b_margin[0])/w[1]
plt.plot(x1,x2)

x2 = -(w[0]*x1 + b_margin[1])/w[1]
plt.plot(x1,x2)

plt.scatter(x_neg[:,0], x_neg[:,1], marker = 'x', color = 'r', label = 'Negative -1')
plt.scatter(x_pos[:,0], x_pos[:,1], marker = 'o', color = 'b',label = 'Positive +1')

plt.savefig("SVM.pdf")