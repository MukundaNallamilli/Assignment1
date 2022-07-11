import numpy as np
import mpmath as mp
import scipy 
import matplotlib.pyplot as plt
import math


x = np.linspace(0.01,5,50)
randvar = np.loadtxt('ray.dat',dtype='double')	
plt.plot(x[0:50].T,randvar,'o')
plt.grid() 
plt.xlabel('$x_i$')
plt.ylabel('$p_X(x_i)$')
plt.legend(["Numerical","Theory"])
plt.show() 
