#Author: Chris Greening 
#Date: 2/6/2020 
#Purpose: Example with scipy.optimize.curve_fit in action 

import numpy as np 
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit 

def func(x, a, b, c):
    return a * np.exp(-b*x) + c

#Define the data to be fit with some noise 
x_data = np.linspace(0, 4, 50)
y = func(x_data, 2.5, 1.3, 0.5)
np.random.seed(1729)
y_noise = 0.2 * np.random.normal(size=x_data.size)
y_data = y + y_noise 
plt.plot(x_data, y_data, 'b-', label='data')

#fit for the parameters a,b,c of func
popt, pcov = curve_fit(func, x_data, y_data)
plt.plot(x_data, func(x_data, *popt), 'r-', label="fit")

plt.show()