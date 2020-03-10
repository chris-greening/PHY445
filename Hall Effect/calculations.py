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

    data_dict['n'] = car_dens.n
    data_dict['deln'] = car_dens.s 

    data_dict['Mu'] = mu.n 
    data_dict['delMu'] = mu.s 

    data_dict['Tau'] = tau.n 
    data_dict['delTau'] = tau.s 

    data_dict['MFP'] = mfp.n 
    data_dict['delMFP'] = mfp.s 

    data_dict = {key: [val] for key,val in data_dict.items()}

    return DataFrame(data_dict)

if __name__ == '__main__': 

    R = ufloat(8048.91,88.16)
    L = ufloat(177.27E-6,.45E-6)
    w = ufloat(100E-6,.45E-6)
    I = ufloat(9.67E-6, .1E-6)

    V_H_77K = ufloat(1.3125E-3,.011E-3)  
    B_77K = ufloat(74.8E-3,.071E-3)

    V_H_300K = ufloat(.7765E-3, .0007E-3)
    B_300K = ufloat(75.9E-3, .071E-3)

    df_77K_calc = solve_everything(R,w,L,V_H_77K,I,B_77K).T
    df_300K_calc = solve_everything(R,w,L,V_H_300K, I, B_300K).T

    df_77K_calc = df_77K_calc.rename(columns={0: '77K'})
    df_300K_calc = df_300K_calc.rename(columns={0: '300K'})
    df_total = df_77K_calc.join(df_300K_calc)

    #pretty print the data 
    string = ''
    i = 0 
    while i < len(df_total):
        row1 = df_total.iloc[i]
        new_row_name = row1.name 

        row2 = df_total.iloc[i+1]
        
        left = str(row1['77K']) + r' $\pm$ ' + str(row2['77K'])
        right = str(row1['300K']) + r' $\pm$ ' + str(row2['300K'])

        string += f'{new_row_name} & {left} & {right} \\\\\n'
        
        i += 2 
    print(string)

