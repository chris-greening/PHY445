#Author: Chris Greening 
#Date: 3/9/2020
#Purpose: Calculations for Hall Effect 

from pandas import DataFrame 
from equations import * 

from scipy import constants
from uncertainties import ufloat 


def solve_everything(R, w, L, V_H, I, B):
    data_dict = {}
    
    R_square = resistance_per_square(R, w, L)
    R_H = hall_coefficient(V_H, I, B)
    
    car_dens = carrier_density(R_H)
    
    mu = mobility(R_H, R_square)
    tau = relaxation_time(mu)
    mfp = mean_free_path(tau)

    data_dict['R'] = R.n 
    data_dict['delR'] = R.s 

    data_dict['W'] = w.n
    data_dict['delW'] = w.s

    data_dict['L'] = L.n
    data_dict['delL'] = L.s

    data_dict['V_H'] = V_H.n
    data_dict['delV_H'] = V_H.s

    data_dict['I'] = I.n
    data_dict['delI'] = I.s

    data_dict['B'] = B.n
    data_dict['delB'] = B.s 

    data_dict['R_square'] = R_square.n 
    data_dict['delR_square'] = R_square.s 

    data_dict['Carrier Density'] = car_dens.n
    data_dict['delCarrier Density'] = car_dens.s 

    data_dict['Mu'] = mu.n 
    data_dict['delMu'] = mu.s 

    data_dict['Tau'] = tau.n 
    data_dict['delTau'] = tau.s 

    data_dict['MFP'] = mfp.n 
    data_dict['delMFP'] = mfp.s 

    data_dict = {key: [val] for key,val in data_dict.items()}

    return DataFrame(data_dict)

if __name__ == '__main__': 
    #300K calculations 
    R = ufloat(8048.91,88.16)
    w = ufloat(177.27E-6,.45E-6)
    L = ufloat(100E-6,.45E-6)

    V_H = ufloat(.903997E-3,.001E-3) 
    I = ufloat(9.67E-6,.1E-6) 
    B = ufloat(89.8E-3,.1E-3)

    df = solve_everything(R,w,L,V_H,I,B)


