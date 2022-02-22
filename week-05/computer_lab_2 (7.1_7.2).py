# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 03:38:14 2022

@author: walee
"""

import numpy as np
import matplotlib.pyplot as plt 
import random


# create a function to simulate walks in the 4 possible directions
def random_walks(num_steps,num_walks):
    # setting the start point to (0,0)
    
    x = 0
    y = 0
    X = []
    Y = []
    
    # the following for_loop will run a simulation of 1000 walks each consists of 1000 steps
    for k in range(num_walks):
        # the following for_loop simulates only one random walk that consists of 1000 steps
        for i in range(num_steps):
            step = random.choice(['N', 'S', 'E', 'W'])
            # the following conditional if statement will perform the walk depending on the random decision for direction of the next step
            if step == 'N':
                y = y + 1
            elif step == 'S':
                y = y - 1
            elif step =='W':
                x = x - 1
            else:
                x = x + 1

    # the following two lines will add the coordinates of the final location of one walk to the appropriate list
        X.append(x)
        Y.append(y)

    return (X, Y)

# creating a function that calculates the distance from the original location
def disp(X_final, Y_final, length):

    displacement = []
    
    for k in range(len(length)):
        d = (X_final[k]**2 + Y_final[k]**2)**0.5
        displacement.append(d)
    return(displacement)

# creating a function that calculates the square of the displacement value
def disp_squared(desired_array, length):

    displacement_squared = []
    
    for n in range(len(length)):
        disp1 = desired_array[n]**2
        displacement_squared.append(disp1)

    return(displacement_squared)

# create a graphing function
def graph(array1, array2):
    plt.scatter(array1,array2, marker = '.')
    plt.xlabel("x-coordinate")
    plt.ylabel("y-coordinate")
    plt.axis('square')
    plt.grid()

# 7.1 Assignment: 
    
X1, Y1 = random_walks(1000,100)
X2, Y2 = random_walks(1000,100)
X3, Y3 = random_walks(1000,100)
X4, Y4 = random_walks(1000,100)

plt.figure()
plt.tight_layout()
plt.subplot(2,2,1)
graph(X1,Y1)
plt.subplot(2,2,2)
graph(X2,Y2)
plt.subplot(2,2,3)
graph(X3,Y3)
plt.subplot(2,2,4)
graph(X4,Y4)
plt.suptitle("4 trajectories of random walks")
plt.show()

# 7.2 Assignment: 
    # Part a) 1000 random walks
X5, Y5 = random_walks(1000,1000)
plt.figure()
graph(X5,Y5)
plt.title("Increasing the number of random walks from 100 to 1000")

    # Part b) histogram of displacement
plt.figure()
D = disp(X5,Y5,X5)
plt.hist(D, rwidth = 0.9)
plt.title("Histogram representing the distance from the end of each walk to the origin")

    # Part c) Histogram of the displacement squared
D_squared = disp_squared(D,D)
plt.figure()
plt.hist(D_squared, rwidth = 0.9)
plt.title("Histogram representing the squared distance from the end of each walk to the origin")

    # Part d) plot semi-log and log-log graphs
plt.figure()
plt.hist(D_squared, rwidth = 0.9)
plt.semilogy()
plt.title("changing the axes of histogram of displacement to semilog")

    # Part e) Calculating the mean of the displacement squared
avg = np.mean(D_squared)
print("The mean of the displacement squared = ", avg)

    # Part f) Calculating the mean square displacements of 4000 step walk4

X6, Y6 = random_walks(4000,1)
D_4000 = disp(X6,Y6,X6)
D_4000_squared = disp_squared(D_4000, D_4000)
print("The mean-square displacement of a 4000-step walk = ", D_4000_squared)