import numpy as np
from scipy.stats import binom
from math import comb
simlen=int(1e6)
#binomial parameters
k=4
pp=2/3
nn=6
#calculation of theoritical probability of a binomial distribution
def prob(n,k,p):
	prob=comb(n,k)*(p**k)*((1-p)**(n-k))
	return(prob)

#Simulations using Bernoulli r.v.
data_bin = binom.rvs(n=nn,p=pp,size=simlen)

#Calculating the number of favourable outcomes from the simulation
def fav(data_bin,k):
	err_ind = np.nonzero(data_bin ==k)
	err_n = np.size(err_ind)/simlen
	return(err_n)
#atleast 4
err_n_2=0
prob2=0
for i in range(4,7):
	prob2=prob2+prob(nn,i,pp)
	err_n_2=err_n_2+fav(data_bin,i)

#Theory vs simulation
print(err_n_2,prob2)
