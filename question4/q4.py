import numpy as np
import matplotlib.pyplot as plt

N=500
x= np.linspace(-2,2,N)
y= np.linspace(-2,2,N)

vals=np.zeros((N,N))
for a in range(N):
    for b in range(N):
        z=0
        c=x[a]+1j*y[b]
        for i in range(100):
            z=z**2
            z+=c

            if np.isnan(z):
                break
        z=abs(z)
        vals[a,b] = z


plt.imshow(vals)
plt.savefig('q4.pdf')
