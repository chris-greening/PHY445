#Author: Chris Greening 
#Date: 1/30/2020
#Purpose: Working on some routines to speed up developing later in the semester

from functools import partial
from typing import List

import matplotlib.pyplot as plt 
from numpy import arange, sin, exp 

def theoretical(
        func,
        min_x: float, 
        max_x: float, 
        step: float = .01
    ) -> List[float]:
    
    """
    Takes a function as an arg and calculates theoretical data for it,
    returning a tuple of x and y coordinates
    """

    x_data = arange(min_x, max_x, step)
    y_data = func(x_data)
    return (x_data, y_data)

if __name__ == '__main__':
   
    def quadratic_example():
        def quadratic(a, b, c, x):
            """Model of quadratic function"""

            return a*x**2 + b*x + c
            
            #bind a,b,c values 
            quad_func = partial(quadratic, 1, 2, 1)

            #calculate data 
            data = theoretical(quad_func, -50, 50,.1)
            
            #unpack tuple of data 
            x,y = data

            #plot
            plt.plot(x,y)
            plt.show()

    def damped_oscillator_example():
        def damped_oscillator(a, b, t):
            return exp(-t/a)*sin(b*t)

        osc_func = partial(damped_oscillator, 3, 3)
        data = theoretical(osc_func, 0, 20, .1)
        x,y = data 
        plt.plot(x,y)
        plt.show()

    damped_oscillator_example()
