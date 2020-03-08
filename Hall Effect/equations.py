#Author: Chris Greening 
#Date: 2/6/2020
#Purpose: Theoretical equations for the Hall effect lab 

from functools import partial 

import numpy as np 
from scipy.constants import physical_constants

def mobility(R_h, R_square):
    """Calculate mobility from Hall resistance and Resistance per unit square"""
    return R_h/R_square 

def hall_coefficient(B, R_H, I): 
    """Equation for the Hall voltage"""
    
    return R_H*B*I

def linear(x, m, b):
    return m*x + b


if __name__ == '__main__': 
    pass
