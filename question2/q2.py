import scipy.special as sp
import numpy
import matplotlib.pyplot as plt


#part A
#Binomial Coefficients
def factorial(x):
    y=1
    while x > 0: 
        y=y*x 
        x=x-1
    return y

def bc(a,b):
    z=0    
    n_fact = factorial(a)
    k_fact = factorial(b)
    k_minus_n_fact = factorial(a-b)

    z = n_fact/k_fact/k_minus_n_fact
    return z
#compare against scipy
#print bc(7,2)
#print sp.binom(7,2)

#########################################

#part B
#PASCALS TRIANGLE
def triangle(n):
    for i in range(0,n):
        line=''

        for x in range(i,n):
            line+=' '

        for j in range(0,i+1):
            line+=str(bc(i,j))+' '

        print line
#triangle(20)

########################################


#part C
#Biased Coin
def find_prob(p,n,k):
    prob= bc(n,k)*p**k*(1-p)**(n-k)
    return prob
#print find_prob(0.5,1,1)

def prob_at_least_k(p,n,k):
    prob=0.
    n=int(n)
    for x in range(1,n+1):
        if x >= k:     
            prob+=find_prob(p,n,x)
    return prob

#print prob_at_least_k(0.5,10,10)

##########################################


#Part D
#simulation
p=0.25
frac=[]

ns=numpy.logspace(1,4,1000)


for n in ns:
    counter=0
    for x in range(int(n)):
        e=numpy.random.random(1)
        if e > p:
            counter+=1
    frac.append(counter/n)



fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(ns,frac)
ax.set_xscale('log')
ax.set_ylim(0,1)
ax.set_ylabel('Fraction Successful')
ax.set_xlabel('Amount of Times Simulated')
ax.set_title('p=%.2f'%(p))
plt.savefig('q2d.pdf')






