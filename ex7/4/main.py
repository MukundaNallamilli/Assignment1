import numpy as np
import mpmath as mp
import scipy 
import matplotlib.pyplot as plt
import math
x = np.linspace(0.01,5,50)
randvar = np.loadtxt('ray.dat',dtype='double')	

def gamma_pdf(y):
    return (0.5*(1-math.sqrt(y/(y+2))))
vec_g = scipy.vectorize(gamma_pdf)

plt.plot(x[0:50].T,randvar,'o',label = 'Numerical')
plt.plot(x,vec_g(x),label = 'Theoritical')
plt.grid() 
plt.xlabel('$x_i$')
plt.ylabel('$p_X(x_i)$')
plt.legend()
plt.show() 
