import numpy as np
import matplotlib.pyplot as plt
# Linear Regression Problem

x =  np.array([2,1,0,3,1])
y = np.array([1,0,1,1,3])
x_bar = np.mean(x)
y_bar = np.mean(y)

def S_xx(arr, mean):
    sum = 0
    for number in arr:
        sum += (number - mean)**2
    return sum

def S_xy(arr1, arr2, mean1, mean2):
    sum = 0
    lis1 = list(arr1)
    lis2 = list(arr2)
    for i in range(len(arr1)):
        sum += (lis1[i] - mean1) * (lis2[i] - mean2)
    return sum

def line_of_best_fit(B_0, B_1, x):
    return B_0 + (B_1 * x)

SXY = S_xy(x, y, x_bar, y_bar)
SXX = S_xx(x, x_bar)
B1 = SXY / SXX
B0 = y_bar - (B1 * x_bar)
best_fit = line_of_best_fit(B0, B1, x)

# Visualization
plt.scatter(x,y)
plt.plot(best_fit)
plt.show()

