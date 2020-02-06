#Author: Chris Greening 
#Date: 2/6/2020
#Purpose: Theoretical equations for the Hall effect lab 

import numpy as np 
from scipy.constants import physical_constants

def mobility(R_h, R_square):
    """Calculate mobility from Hall resistance and Resistance per unit square"""
    return R_h/R_square 

if __name__ == '__main__': 
    import sys 
    sys.path.append('../Brainstorming')
    from functools import partial 
    
    from theoretical_tools import theoretical 
    
    mu = partial(mobility, 100)
    x,y = theoretical(mu, 100, 1, -.01)


