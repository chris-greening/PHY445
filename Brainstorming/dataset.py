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
        self.x = None 
        self.y = None 
        self.theo_x = None 
        self.theo_y = None
        self.df = None

    def load_exp(self, x, y, x_err, y_err):
        
        x = np.array(x) 
        y = np.array(y) 
        x_err = np.array(x_err)
        y_err = np.array(y_err)

        len_x = str(len(x))
        len_y = str(len(y))
        if len(x) != len(y):
            raise ValueError(f'Length mismatch: x has {len_x} elements, y has {len_y} elements')

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

    #theoretical data 
    dataset = Dataset()
    dataset.generate_theo(osc_func, 0, 20)
    theo_x,theo_y = dataset.theo_data

    #experimental data 
    noise = np.random.normal(0,.03,len(theo_x))
    exp_x = theo_x
    exp_y = theo_y + noise 
    
    Dataset.line(exp_x, exp_y)
    Dataset.line(theo_x, theo_y)
    
    plt.show()
    
