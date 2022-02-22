# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 21:30:54 2022

@author: walee
"""

import numpy as np
import matplotlib.pyplot as plt
import random as rand

# a) sums of random variables

x1 = np.random.normal(-0.5,0.5,50000)
x2 = np.random.normal(-0.5,0.5,50000)

plt.figure()
y_hist = x1 + x2
plt.hist(y_hist, bins = 25, rwidth = 0.5, color = 'blue')
sigma1 = np.std(y_hist)
mean1 = np.mean(y_hist)
x_plot1 = np.linspace(-5,5,50000)
y_plot1 = (1/(sigma1 * np.sqrt(2*np.pi))) * np.e**(-(x_plot1-mean1)**2 / (2*sigma1**2))
plt.plot(x_plot1, 12000*y_plot1, color = 'red')
plt.title("part a1")

x3 = np.random.normal(-0.5,0.5,50000)
x4 = np.random.normal(-0.5,0.5,50000)

plt.figure()
y_hist2 = x1 + x2 + x3 + x4
plt.hist(y_hist2, bins = 25, rwidth = 0.5, color = 'blue')
sigma2 = np.std(y_hist2)
mean2 = np.mean(y_hist2)
x_plot2 = np.linspace(-5,5,50000)
y_plot2 = (1/(sigma2 * np.sqrt(2*np.pi))) * np.e**(-(x_plot2-mean2)**2 / (2*sigma2**2))
plt.plot(x_plot2, 17000*y_plot2, color = 'red')
plt.title("part a2")
# b) sums of more random variables

x5 = np.random.normal(-0.5,0.5,50000)
x6 = np.random.normal(-0.5,0.5,50000)
x7 = np.random.normal(-0.5,0.5,50000)
x8 = np.random.normal(-0.5,0.5,50000)
x9 = np.random.normal(-0.5,0.5,50000)
x10 = np.random.normal(-0.5,0.5,50000)

plt.figure()
y_hist3 = x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x10
plt.hist(y_hist3, bins = 40, rwidth = 0.5, color = 'blue')
sigma3 = np.std(y_hist3)
mean3 = np.mean(y_hist3)
x_plot3 = np.linspace(-11,1,50000)
y_plot3 = (1/(sigma3 * np.sqrt(2*np.pi))) * np.e**(-(x_plot3-mean3)**2 / (2*sigma3**2))
plt.plot(x_plot3, 16000*y_plot3, color = 'red')
plt.title("part b")

# c) sum of numuniform discrete random variables

x = [1, 2, 3, 4]
prob_x = [1/3, 2/9, 1/9, 1/3]
def random(n):
    array_1 = []
    array_2 = []
    array_3 = []
    array_4 = []
    for i in range(n):
        r = rand.choices(x, prob_x)
        if r == [1]:
            array_1.append(r)
        elif r == [2]:
            array_2.append(r)
        elif r == [3]:
            array_3.append(r)
        else:
            array_4.append(r)
    return array_1, array_2, array_3, array_4

y1, y2, y3, y4 = random(10000)
data = {'1':len(y1), '2':len(y2), '3':len(y3), '4':len(y4)}
options = list(data.keys())
values = list(data.values())
plt.figure()
plt.title("frequencies or selecting the discrete values: 1, 2, 3, 4")
plt.bar(options, values, color = 'red')