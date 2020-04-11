# -*- coding: utf-8 -*-
"""
Created on Thu May 10 10:51:25 2018

@author: mzm0175
"""


import functools as f
import numpy as np
import operator as op
import matplotlib.pyplot as plt


N=128# bit length

def ncr(n, r): # combination method
    r = min(r, n-r)
    numer = f.reduce(op.mul, range(n, n-r, -1), 1)
    denom = f.reduce(op.mul, range(1, r+1), 1)
    return numer//denom
a=np.zeros((7))
a[0]=ncr(N,1)/(2**N)
for i in range(1,7):
    b=ncr(N,2**i)/(2**N)
    a[i]=(a[i-1]+b)
fig1=plt.figure()
plt.semilogy([1,2,4,8,16,32,64], a, label='Single ID macthing')

#plt.show()
b=np.zeros((7,5))
for k in range(0,7):
    b[k,0]=a[k]*ncr(N-(2**k),1)/(2**(N-(2**k)))
    for i in range(1,5):
        b[k,i]=a[k]*(b[k,i-1]+(ncr(N-(2**k),2**(i))/(2**(N-(2**k)))))
#print(b)
c=np.zeros(7)
#fig2=plt.figure()
for i in range (0,5):
    for j in range(0,7):
        c[j]=b[j,i]
    plt.semilogy([1,2,4,8,16,32,64], c,'--*',  label='$HD_T^\dagger=%s$' % (i+1))

#plt.rcParams.update({'font.size': 7})      

plt.xlabel("Hamming Distance (HD$_T$)",fontname="Times New Roman", fontsize=18)
#plt.xlabel("Median Population", fontname="Arial", fontsize=12)
plt.ylabel("Probabilty of ID matching (log$_{10}$ scale)",fontname="Times New Roman", fontsize=18)

plt.legend(frameon=False, prop={'size':10})
#plt.figure(figsize=(3,1)) 

fig = plt.gcf()

fig.set_size_inches(7, 6.5)
fig1.savefig('plot_'+str(N)+'.png')      


plt.show()





    

    
    