#3/16/2020

from scipy.optimize import curve_fit
import numpy as np 
from numpy import pi, sqrt, exp, array 
import matplotlib.pyplot as plt 


def gaussian_with_exponential(x, a, x0, sigma):
    # return (1/(sqrt(2*pi)*sigma))*exp(-(x-x0)**2/(2*sigma**2))
    x = array(x)
    return a*exp(-(x-x0)**2/(2*sigma**2)) + 1248*exp(-.008015*x) + -1000.1191

def exponential_background(x, a, b, c):
    return a*exp(-b*x) + c

if __name__ == '__main__':
    import labpandas as lpd 
    cesium = lpd.import_spe('data/StrongCs137.Spe')

    peak_with_bg = cesium.iloc[600:1200]
    x = array(range(len(peak_with_bg)))
    y = peak_with_bg[0].to_numpy()

    xbg_left = x[:170]
    ybg_left = y[:170]
    xbg_right = x[440:]
    ybg_right = y[440:]
    xbg_total = np.append(xbg_left, xbg_right)
    ybg_total = np.append(ybg_left, ybg_right)

    gaussianx = x[200:400] - 170
    gaussiany = y[200:400]

    bg_popt, pcov = curve_fit(exponential_background, xbg_total, ybg_total)
    popt, pcov = curve_fit(gaussian_with_exponential, gaussianx, gaussiany, p0=[200,200,200])
    
    plt.plot(x, y)
    plt.plot(gaussianx+170, gaussiany)
    plt.plot(gaussianx+170, gaussian_with_exponential(gaussianx, *popt))

    plt.legend()
    plt.show()
