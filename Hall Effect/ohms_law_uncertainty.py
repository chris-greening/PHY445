#Author: Chris Greening 
#Date: 2/17/2020
#Purpose: Experimental Ohm's law, takes uncertainty into account 

from decimal import Decimal 

from math import sqrt

def mul_div_error(*args):
    """Takes arbitrary amount of values and their respective uncertainties and 
    returns a final uncertainty"""
    
    radicand = Decimal(0) 
    for arg in args:
        Xo, delX = arg
        X_frac = Decimal(delX/Xo)
        radicand += Decimal(X_frac**2)
    return sqrt(radicand)


def experimental_ohms_law(V, I):
    """Takes tuple containing central value and uncertainty"""

    Vo, delV = V
    Io, delI = I  

    Ro = Vo/Io

    delR = mul_div_error(V, I)

    return (Ro, delR)

if __name__ == '__main__':
    V = (74.05E-3, .1E-3)
    I = (9.2E-6, .1E-6)
    R =   experimental_ohms_law(V, I)

    L = (477.27E-6, .45E-6)
    W = (100.0E-6, .45E-6)
    R_square = (L[0]/W[0])*R[0]
    delR_square = mul_div_error(L, W, R)
    