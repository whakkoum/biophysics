# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 23:22:43 2022

@author: walee
"""
# 7.3.1 The poisson distribution

# importing random and graphing libraries

import random
import numpy as np
import scipy.special as ss
import matplotlib.pyplot as plt

# a) plo the function on the interval 0 < l < 20
# np.linspace is working perfectly. 
l = np.linspace(0, 20, 1000)
pois = np.e**-8 * 8**l / ss.factorial(l)
plt.figure()
plt.plot(l,pois)
plt.show()

# b) performing N coin flip trial each consisting of 100 flips:
# Create a function to generate random numbers and saves the number of heads and tails at the end:
def trials(heads,tails,heads_per_trial,tails_per_trial,p,prob):    
    for i in range(100):
        r = random.choices(p,prob)
        if r == [1]:
            heads += 1
        else:
            tails += 1
    heads_per_trial.append(heads)
    tails_per_trial.append(tails)
    
    return(heads,tails,heads_per_trial,tails_per_trial)


heads = 0
tails = 0
heads_per_trial = [] 
tails_per_trial = []
p = [0,1]
prob = [0.92,0.08]

# c) Calculating the number of heads (M) for each trial: 
N = 1000

for i in range(N):
    trials(heads,tails,heads_per_trial,tails_per_trial,p,prob)
print("The number of heads per trial = ", heads_per_trial)

# making a histogram for the frequency of getting heads in 1000 trials
x1 = np.arange(0,20,1)
plt.figure()
plt.hist(heads_per_trial,bins = x1, rwidth = 0.9)

# d) graphing the poisson distribution multiplied by 1000: 

plt.plot(l,N*pois)
# the most probable outcome is about 9 heads per trial

# e) repeat b-d for N = 1,000,000
N1 = 10000
for i in range(N1):
    trials(heads,tails,heads_per_trial,tails_per_trial,p,prob)
print("The number of heads per trial = ", heads_per_trial)

# making a histogram for the frequency of getting heads in 1000 trials
x1 = np.arange(0,20,1)
plt.figure()
plt.hist(heads_per_trial,bins = x1, rwidth = 0.9)
plt.plot(l,N1*pois)
# We can colclude that as the number of values increase, the distribution becomes more and more presice.

# 7.3.2 Waiting times

def coin_flips(N2):
    results = []
    for i in range(N2):
        r = random.choices(p,prob)
        if r == [1]:
            results.append(1)
        else:
            results.append(0)
            
    return(results)
head_results = np.nonzero(coin_flips(1000))
waiting_time = np.diff(head_results)
plt.figure()
plt.hist(waiting_time, bins = 5)
plt.title("waiting times")

print("The average of waiting time between heads (1,000) = ",np.mean(waiting_time))

head_results = np.nonzero(coin_flips(1000000))
waiting_time = np.diff(head_results)
plt.figure()
plt.hist(waiting_time, bins = 5)
plt.title("waiting times")

print("The average of waiting time between heads 1,000,000 = ",np.mean(waiting_time))