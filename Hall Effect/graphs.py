#Author: Chris Greening 
#Date: 3/5/2020
#Purpose: Graphs for the experiment 

import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit

from equations import linear 
import data_analysis as ds

def hall_graphs(ax, df, title): 
    
    #Set table metadata 
    ax.set_xlabel("Magnetic Field (mT)")
    ax.set_ylabel("Hall Voltage (mV)")
    ax.set_title(title)

    #Experimental data 
    B = df['B']
    data = df.to_tuple(V_H=('V_H', 'delV_H'))
    V_Ho, sigV_H = data['V_H']

    #Fit data 
    V_Hfit, R_H, b = df.fit(linear, 'B', 'V_H', 'delV_H')
    
    #Hall coefficient placed onto graph 
    ax.text(10,2.5,'$R_H = $%0.4f' % R_H, fontsize=15)

    #Plot onto the axes 
    ax.plot(B, V_Hfit, label='best fit')
    ax.errorbar(B, V_Ho, yerr=sigV_H, fmt='.')

    ax.legend()

def graph_77K():
    """Plot Hall voltage at 77K"""

    ax = plt.subplot(111)
    hall_graphs(ax, ds.df_77K, "Magnetic Field vs. Hall Voltage at 77K")
    plt.show()

if __name__ == '__main__':
    graph_77K()
