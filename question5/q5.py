import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x*(x-1.)


#analytical derivative of f(x) is df/dx = 2x-1
#at x = 1, df/dx=1

derivatives=[]
deltas=np.logspace(-4,-14,200)
for d in deltas:
    dfdx=(f(1.+d)-f(1.))/d
    derivatives.append(dfdx)


fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(deltas,derivatives)
ax.set_xscale('log')
ax.set_ylabel('df/dx    at x=1')
ax.set_xlabel('delta')
plt.savefig('derivatives.pdf')

#I find I get the most precision from delta = 10^-10 .. 10^-5
#below 10^-10 it varies greatly
#around 10^-4 it increases slightly
