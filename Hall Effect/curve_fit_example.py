#Author: Chris Greening 
#Date: 3/5/2020 
#Purpose: Scipy example! 

from numpy import array 
import numpy as np 

import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def func(x, a, b, c):
    return a * np.exp(-b * x) + c

#noisy data 
xdata = np.linspace(0, 4, 50)
test = np.linspace(0, 4, 50)
y = func(xdata, 2.5, 1.3, 0.5)
np.random.seed(1729)
y_noise = 0.2 * np.random.normal(size=xdata.size)
ydata = y + y_noise
plt.plot(xdata, ydata, 'b-', label='data')

#theoretical data 
popt, pcov = curve_fit(func, xdata, ydata)
popt
array([2.55423706,  1.35190947,  0.47450618])
plt.plot(xdata, func(xdata, *popt), 'r-',
                        label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))

#Constrain the optimization to the region of 0 <= a <= 3, 0 <= b <= 1 and 0 <= c <= 0.5:
# popt, pcov = curve_fit(func, xdata, ydata, bounds=(0, [3., 1., 0.5]))
# popt
# array([2.43708906,  1.,  0.35015434])
# plt.plot(xdata, func(xdata, *popt), 'g--',
#                 label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
