#Author: Chris Greening 
#Date: 3/5/2020
#Purpose: Graphs for the experiment 

import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit
import numpy as np 

from equations import linear 
import data_analysis as ds

def graph_metadata(ax, title):
    """Place metadata onto our graph"""

    #Set table metadata
    ax.set_xlabel("Magnetic Field (mT)")
    ax.set_ylabel("Hall Voltage (mV)")
    ax.set_title(title)

def plot_data(ax, *args): 
    """
    Plot data from the passed dataframe's
    
    Pass in optional amount of dataframe's and their label as tuple's then 
    plot them on the same axis.
    Example arg: (dataframe, 'some data')
    """

    #Loop through each argument and plot to axis 
    R_H_arr = []
    for df_tup in args:
        df, label = df_tup 
        
        #Experimental data 
        B = df['B']
        data = df.to_tuple(V_H=('V_H', 'delV_H'))
        V_Ho, sigV_H = data['V_H']

        #Fit data 
        V_Hfit, R_H, b = df.fit(linear, 'B', 'V_H', 'delV_H')

        #Get absolute value of data so that postive
        V_Ho = np.abs(V_Ho)
        V_Hfit = np.abs(V_Hfit)

        #Plot onto the axes
        ax.plot(B, V_Hfit, label=f'{label} best fit')
        ax.errorbar(B, V_Ho, yerr=sigV_H, fmt='.', label=f'{label} observed')

        #append Hall coefficient to arr
        R_H = np.abs(R_H)
        R_H_arr.append(R_H)

    return ax, tuple(R_H_arr)

def graph_77K():
    """Plot Hall voltage at 77K"""

    ax = plt.subplot(111)
    graph_metadata(ax, "Magnetic Field vs. Hall Voltage at 77K and 300K")

    ax, R_H_tuple = plot_data(ax, (ds.df_77K, '77K'))
    
    ax.text(.2, .9, '$R_H = $%0.4f' % R_H_tuple,
            ha='center', va='center', transform=ax.transAxes, fontsize=15)
    ax.legend(loc='upper right')

    plt.show()


def graph_77K_reverse():
    """Plot Hall voltage at 77K"""

    ax = plt.subplot(111)
    graph_metadata(ax, "Magnetic Field vs. Hall Voltage at 77K with Reverse Current")

    ax, R_H_tuple = plot_data(ax, (ds.df_77K_reverse, '77K'))

    ax.text(.2, .9, '$R_H = $%0.4f' % R_H_tuple,
            ha='center', va='center', transform=ax.transAxes, fontsize=15)
    ax.legend(loc='upper right')

    plt.show()


def graph_300K():
    """Plot Hall voltage at 300K"""

    ax = plt.subplot(111)
    graph_metadata(ax, "Magnetic Field vs. Hall Voltage at 300K")

    ax, R_H_tuple = plot_data(ax, (ds.df_300K, '300K'))

    ax.text(.2, .9, '$R_H = $%0.4f' % R_H_tuple,
            ha='center', va='center', transform=ax.transAxes, fontsize=15)
    ax.legend(loc='upper right')
    plt.show()


def graph_300K_reverse():
    """Plot Hall voltage at 300K"""

    ax = plt.subplot(111)
    graph_metadata(ax, "Magnetic Field vs. Hall Voltage at 300K with Reverse Current")

    ax, R_H_tuple = plot_data(ax, (ds.df_300K_reverse, '300K'))

    ax.text(.2, .9, '$R_H = $%0.4f' % R_H_tuple,
            ha='center', va='center', transform=ax.transAxes, fontsize=15)
    ax.legend('upper right')

    plt.show()

def graph_77K_300K():
    """Plot 77K and 300K on the same graph to show difference"""
    
    ax = plt.subplot(111)
    graph_metadata(ax, "Magnetic Field vs. Hall Voltage at 77K")

    ax, R_H = plot_data(ax, (ds.df_77K, '77K'), (ds.df_300K, '300K'))

    # ax.text(10, 2.5, '$R_H = $%0.4f' % R_H, fontsize=15)
    ax.legend(loc='upper right')

    plt.show()

def graph_77K_forward_and_reverse():
    """Plot 77K with forward and reverse currents"""

    ax = plt.subplot(111)
    graph_metadata(ax, "Magnetic Field vs. Hall Voltage at 77K, Forward and Reverse Current")

    ax, R_H = plot_data(ax, (ds.df_77K, '77K Forward Current'), (ds.df_77K_reverse, '77K Reverse Current'))

    # ax.text(10, 2.5, '$R_H = $%0.4f' % R_H, fontsize=15)
    ax.legend(loc='upper right')

    plt.show()


def graph_300K_forward_and_reverse():
    """Plot 77K with forward and reverse currents"""

    ax = plt.subplot(111)
    graph_metadata(
        ax, "Magnetic Field vs. Hall Voltage at 300K, Forward and Reverse Current")

    ax, R_H = plot_data(ax, (ds.df_300K, '300K Forward Current'),
                        (ds.df_300K_reverse, '300K Reverse Current'))

    # ax.text(10, 2.5, '$R_H = $%0.4f' % R_H, fontsize=15)
    ax.legend(loc='upper right')

    plt.show()

if __name__ == '__main__':
    graph_77K()
