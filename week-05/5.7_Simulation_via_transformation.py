# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 10:17:56 2022

@author: walee
"""

import numpy as np
import matplotlib.pyplot as plt 
def data(N):
    x = np.linspace(0,1,N)
    return x
y = 1/data(10000)

plt.figure()
plt.hist(y, bins = np.arange(0,10,.1), rwidth = 1)
plt.title("Histogram of 1/x")

# changing axes into log-log plot:
    
plt.figure()
plt.hist(y, bins = np.arange(0,10,.1), rwidth = 1)
plt.loglog()
plt.title("Log-log plot of frequencies")

# c) Explaining the results:
    
""" 
The graph of y should be declining as the plot show in this code because the inverse of the continuous numbers between 0 and 1
is expected to decrease as we go along the y axis.
for example the first 3 numbers in the x-sequence are: [0.000100010001,0.000200020002,0.000300030003, .....]
their inverse is: [9999., 4999.5,3333., ......] and they will continue to decrease exponentially by following the same behavior.

The lower right of the histogram does look a little messy. 
"""

# d) Numerical experiments with more samples

y_50000 = 1/data(50000)
plt.figure()
plt.hist(y_50000, bins = np.arange(0,10,.1), rwidth = 1)
plt.title("Replacing 10,000 by 50,000 data points")

plt.figure()
plt.hist(y_50000, bins = np.arange(0,10,.1), rwidth = 1)
plt.loglog()
plt.title("Changing the axis to loglog for 50,000 data points")

""" 
When we replaced 10,000 by 50,000, we don't see the messiness by the end of the loglog plot anymore
"""
