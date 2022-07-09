#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt
import scipy

#if using termux
import subprocess
import shlex
#end if



x = np.linspace(-4,4,100)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
#randvar = np.random.normal(0,1,simlen)
randvar = np.loadtxt('../data/uni.dat',dtype='double')
#randvar = np.loadtxt('gau.dat',dtype='double')
for i in range(0,100):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

def cdf(x):
	if (x < 0):
		return 0.0
	elif (x < 1):
		return x
	else :
		return 1.0

cdf_plot=scipy.vectorize(cdf)
plt.plot(x.T,cdf_plot(x),label="theory")
plt.plot(x.T,err,'o',label="numerical")#plotting the CDF
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_U(x)$')

plt.legend(loc="best")
#if using termux
plt.savefig('../figs/uni_cdf.pdf')
plt.savefig('../figs/uni_cdf.eps')
#subprocess.run(shlex.split("termux-open ./figs/uni_cdf.pdf"))
#if using termux
#plt.savefig('../figs/gauss_cdf.pdf')
#plt.savefig('../figs/gauss_cdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/gauss_cdf.pdf"))
#else
#plt.show() #opening the plot window
