# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 02:46:57 2022

@author: walee
"""

import numpy as np
import random
import matplotlib.pyplot as plt
from numpy.random import default_rng
import statistics as stat
rand = default_rng().random

beta = 1
N = 400
u = rand(N)
u1 = rand(N)
y = -np.log(u)
y1 = -np.log(u1)
t = y/beta
t1 = y1/beta

# elapsed times

time = t.cumsum()
time1 = t1.cumsum()

# probability of each direction is equal (0.5)

xi = 0.5

steps = 2*(rand(N) < xi) -1
steps1 = 2*(rand(N) < xi) -1
location = steps.cumsum()
location1 = steps1.cumsum()
# plotting two random walks with random waiting times
plt.figure()
plt.plot(time, location)
plt.plot(time1, location1)


def random_walks(N):
    xi = 0.5
    
    steps = 2*(rand(N) < xi) -1
    steps1 = 2*(rand(N) < xi) -1
    location = steps.cumsum()
    location1 = steps1.cumsum()
    return (location[N-1], location1[N-1])

# for 400 seconds

ending_position = []
ending_position1 = []

for i in range(50):
    x, x1 = random_walks(400)
    ending_position.append(x)
    ending_position1.append(x1)
    
# let's only consider the first random walk

sample_mean = np.mean(ending_position)
variance = stat.pvariance(ending_position)
print("\nrepeat 50 trajectories with duration 400 seconds\n")
print("mean_400s = ", sample_mean)
print("Variance = ", variance)

# for 200 seconds

ending_position = []
ending_position1 = []

for i in range(50):
    x, x1 = random_walks(200)
    ending_position.append(x)
    ending_position1.append(x1)
    
# let's only consider the first random walk

sample_mean = np.mean(ending_position)
variance = stat.pvariance(ending_position)
print("\nrepeat 50 trajectories with duration 200 seconds\n")
print("mean_200s = ", sample_mean)
print("Variance = ", variance)

# for 600 seconds

ending_position = []
ending_position1 = []

for i in range(50):
    x, x1 = random_walks(600)
    ending_position.append(x)
    ending_position1.append(x1)
    
# let's only consider the first random walk

sample_mean = np.mean(ending_position)
variance = stat.pvariance(ending_position)
print("\nrepeat 50 trajectories with duration 600 seconds\n")
print("mean = ", sample_mean)
print("Variance = ", variance) 

# simulating 2 dimensional random walks

def random_walks(n):
    # set initial position to zero (origin)
    x_1 = 0
    y_1 = 0
    for i in range(n):
        step = random.choice(['north', 'south', 'east', 'west'])
        if step == 'north':
            y_1 = y_1 + 1
        elif step == 'south':
            y_1 = y_1 - 1
        elif step == 'east':
            x_1 = x_1 + 1
        else:
            x_1 = x_1 - 1
    return(x_1, y_1)

x_1, y_1 = random_walks(100)
plt.figure()
plt.plot(x_1, y_1, '.')

