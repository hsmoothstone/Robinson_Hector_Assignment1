
import numpy as np
import matplotlib.pyplot as plt
import scipy
from PIL import Image
from scipy import signal



#trapezoid rule
#theta and f arrays of same length
#f=f(theta) 
def integrate(theta,f):
    A=0.
    i=0
    while i < len(theta)-1:
        A+=((f[i]+f[i+1])/2.0)*(theta[i+1]-theta[i])
        i+=1
    return A


#function that returns bessel function of first kind, of order m, at point x.
def bessel(m,x):
    f=[]
    theta=np.linspace(0,np.pi,200)
  
    for i in theta:
        f.append(np.cos(m*i-x*np.sin(i)))

    g=integrate(theta,f)/np.pi
    return g


#plot bessel function for m=0,1,2
for m in [0,1,2]:
    y=np.linspace(0,20,100)
    h=[]
    for i in y:
        h.append(bessel(m,i))

    plt.plot(y,h)
    plt.xlabel(r'$x$',fontsize=25)
    plt.ylabel(r'$J_m$',fontsize=25)
plt.legend(['m=0','m=1','m=2'])
plt.savefig('q3plot.pdf')

########################################################
#PartB

N=200

R=1.
l=650.
a=1.
I0=100.


I=np.zeros((N,N))
x=np.linspace(-5,5,N)
y=np.linspace(-5,5,N)


xv,yv = np.meshgrid(x,y)
q=np.sqrt(xv**2.+yv**2.)
z=2*np.pi*a*q/l/R
I=I0*(2*bessel(1,z)/z)**2.
        

plt.close()
plt.imshow(I)
plt.xlabel('x')
plt.ylabel('y')
plt.xticks([])
plt.yticks([])
plt.savefig('q3_Image.pdf')

##################################################

im=Image.open('crab.jpg')
im = im.convert('L')
im.show()
h=scipy.signal.convolve2d(im,I)

scipy.misc.imsave('outfile.jpg', h)








 
