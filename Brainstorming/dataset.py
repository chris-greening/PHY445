#Author: Chris Greening 
#Date: 1/31/2020
#Purpose: Unify data analysis and graphing into one class 

import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 
from pandas import Series, DataFrame 

from plotting import professional

class Dataset:
    
    line    = professional(plt.plot)
    bar     = professional(plt.bar)
    scatter = professional(plt.scatter)
    
    def __init__(self):
        """Rough draft of data analysis framework"""
        self.exp_x = None 
        self.exp_y = None 
        self.theo_x = None 
        self.theo_y = None
        self.df = None

    def load_exp(self):
        pass

    def generate_theo(self, theo_func, min_x, max_x, step=.01):
        """
        Takes theoretical function with bound values (not including IV) 
        associated with our dataset as argument
        """

        self.theo_data = theoretical(
                                theo_func, 
                                min_x=min_x, 
                                max_x=max_x, 
                                step=step
                            )

        self.theo_x, self.theo_y = self.theo_data                   

    def graph_exp_vs_theo(self):
        pass

if __name__ == '__main__':

    from functools import partial

    from numpy import exp, sin

    from theoretical_tools import theoretical

    def damped_oscillator(a, b, t):
        return exp(-t/a)*sin(b*t)

    osc_func = partial(damped_oscillator, 3, 3)

    dataset = Dataset()
    dataset.generate_theo(osc_func, 0, 20)
    x,y = dataset.theo_data
    Dataset.line()
    plt.show()
    
