#Author: Chris Greening 
#Date: 1/31/2020
#Purpose: Decorator for matplotlib that allows for 

from functools import partial, wraps

import matplotlib.pyplot as plt 
from numpy import exp, sin

from theoretical_tools import theoretical

#alternative color scheme because matplotlib is uuuuuugly 
tableau20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),    
            (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),    
            (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),    
            (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),    
            (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]

#matplotlib color arg accepts values between 0 and 1, recalc rgb vals  
tableau20 = [(r/255, g/255, b/255) for r,g,b in tableau20]

def professional(func):
    """Decorator that applies nicer default stylings to pyplot graphs"""
    i = 0
    plt.style.use("ggplot") #default plot style 
    def wrapper_with_args(*args, **kwargs):
        nonlocal i 
        i += 1
        color = tableau20[i]
        return func(*args, **kwargs, color=color)
    return wrapper_with_args

if __name__ == '__main__':
    
    #example function 
    def damped_oscillator(a, b, t):
            return exp(-t/a)*sin(b*t)

    def graph(plot_func, title):
        """Takes plot function and title as args"""
        for val in range(1,5):
            osc_func = partial(damped_oscillator, val, val) #bind values    
            data = theoretical(osc_func, 0, 20, .01)   #generate theoretical data 
            x,y = data 
            plot_func(x, y)
        plt.title(title)

    #ugly graph 
    plt.figure(0)
    graph(plt.plot, "Ugly Graph")
    
    #pretty graph
    plt.figure(1)
    pretty_plot = professional(plt.plot)  #apply decorator 
    graph(pretty_plot, "Pretty Graph")

    plt.show()


          
        