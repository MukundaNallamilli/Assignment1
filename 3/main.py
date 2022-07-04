import numpy as np


u1 = np.loadtxt('v.dat',dtype='double')
t1 = open('a.dat','w') 

t =[]
for i in range(len(u1)):
    t.append(str( np.sqrt(u1[i]) ) )
for i in t:
  t1.write(f'{i}\n')

