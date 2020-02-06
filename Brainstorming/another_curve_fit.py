#Author: Chris Greening 
#Date: 2/6/2020 
#Purpose: Another experiment with curve_fit 

import matplotlib.pyplot as plt 
import numpy as np 
from scipy.optimize import curve_fit

def damped_oscillator(a, b, t):
    return np.exp(-t/a)*np.sin(b*t)

#Define the data to be fit with some noise 
x_data = np.linspace(0, 2*np.pi, 200)
y = damped_oscillator(3, 3, x_data)
np.random.seed(1729)
y_noise = 0.1 * np.random.normal(size=x_data.size)
y_data = y + y_noise 
plt.plot(x_data, y_data, 'b-', label='data')

#fit for the parameters a,b,c of func
popt, pcov = curve_fit(damped_oscillator, x_data, y_data)
plt.plot(x_data, damped_oscillator(x_data, *popt), 'r-', label="fit")

plt.show()