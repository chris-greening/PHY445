#Author: Chris Greening 
#Date: 2/6/2020
#Purpose: Theoretical equations for the Hall effect lab 

from functools import partial 

import numpy as np 
from scipy import constants

e = constants.e
m_star = .067

def resistance_per_square(R, w, L):
    return (L/w)*R

def hall_coefficient(V_H, I, B):
    return V_H/(I*B)

def carrier_density(R_H):
    return 1/(R_H*e)

def mobility(R_H, R_square):
    """Calculate mobility from Hall resistance and Resistance per unit square"""
    return R_H/R_square 

def relaxation_time(mu):
    return (mu*m_star)/e

def mean_free_path(tau):
    return 1/tau

def linear(x, m, b):
    return m*x + b


if __name__ == '__main__': 
    pass
