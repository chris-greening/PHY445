#Author: chris Greening 
#Date: 3/10/2020
#Purpose: Figuring our curve fitting for Gaussian's

import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np 
from scipy import asarray as ar, exp

# x = ar(range(10))
# y = ar([0, 1, 2, 3, 4, 5, 4, 3, 2, 1])

# n = len(x)  # the number of data
# mean = sum(x*y)/n  # note this correction
# sigma = sum(y*(x-mean)**2)/n  # note this correction


def gaus(x, a, x0, sigma):
    return a*exp(-(x-x0)**2/(2*sigma**2))


# popt, pcov = curve_fit(gaus, x, y, p0=[1, mean, sigma])

# plt.plot(x, y, 'b+:', label='data')
# plt.plot(x, gaus(x, *popt), 'ro:', label='fit')
# plt.legend()
# plt.title('Fig. 3 - Fit for Time Constant')
# plt.xlabel('Time (s)')
# plt.ylabel('Voltage (V)')
# plt.show()

y = np.random.normal(20, 1,10000)
plt.hist(y, 10)
plt.show()