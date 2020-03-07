#Author: Chris Greening 
#Date: 3/5/2020
#Purpose: Graphs for the experiment 

import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit

import data_analysis as ds

def hall_graphs(ax, title): 
    ax.set_xlabel("Magnetic Field (mT)")
    ax.set_ylabel("Hall Voltage (mV)")
    ax.set_title(title)
    ax.legend()

def graph_77K():
    ax = plt.subplot(111)
    hall_graphs(ax, "77K")
    plt.show()

if __name__ == '__main__':
    graph_77K()