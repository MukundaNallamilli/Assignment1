import numpy as np

x = np.linspace(0.01,5,50)
f = open("Gamma.dat",'w')
for i in x:
  f.write(f'{i}\n')
