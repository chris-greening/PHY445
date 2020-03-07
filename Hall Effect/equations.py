#Author: Chris Greening 
#Date: 2/6/2020
#Purpose: Theoretical equations for the Hall effect lab 

from functools import partial 

import numpy as np 
from scipy.constants import physical_constants

def mobility(R_h, R_square):
    """Calculate mobility from Hall resistance and Resistance per unit square"""
    return R_h/R_square 

def hall_coefficient(B, V_H, I): 
    """Equation for the Hall voltage"""
    
    return V_H/(B)

def linear(x, m, b):
    return m*x + b


if __name__ == '__main__': 
    # import sys 
    # sys.path.append('../Brainstorming')
    # from functools import partial 
    
    # from theoretical_tools import theoretical 
    
    # mu = partial(mobility, 100)
    # x,y = theoretical(mu, 100, 1, -.01)

    from data.data import df_77K
    from data_analysis import tuplize_df

    data = tuplize_df(df_77K, B=("B", "delB"))
    B = data['B']

    #noisy data
    xdata = B 
    y = hall_voltage(xdata, 2.5, 1.3, 0.5)
    
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
