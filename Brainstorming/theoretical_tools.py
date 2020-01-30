#Author: Chris Greening 
#Date: 1/30/2020
#Purpose: Working on some routines to speed up developing later in the semester

from functools import partial
from typing import List

import matplotlib.pyplot as plt 
from numpy import arange 

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