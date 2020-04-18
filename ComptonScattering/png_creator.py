#Author: Chris Greening 
#Date: 4/18/2020
#Purpose: Create .png for each of the files so we can get an idea of what this looks like 

import os 
from pathlib import Path 

import matplotlib.pyplot as plt 
import imageio


from labpandas import LabDataFrame, import_csv

def png_loop(dir_fpath):
    """Loop through dir at given arg and create a .png for each .csv"""

    dataframes = [(import_csv(csv_fpath), csv_fpath) for csv_fpath in get_csv_fpaths(dir_fpath)]
    
    #loop through dataframes and create png's from the data 
    images = []
    for df, csv_fpath in dataframes:
        png_fpath = convert_to_png(csv_fpath)

        # Get sample title for the png
        title_str = Path(png_fpath).stem
        # degrees = raw_str.split("-")[1]
        # title_str = f"Cesium137 at {degrees} degrees"

        #save the fig 
        df.plot()
        plt.title(title_str)
        fig = plt.gcf()
        fig.set_size_inches(12,6)
        plt.savefig(png_fpath, dpi=100)
    
    #     images.append(imageio.imread(png_fpath))
    # imageio.mimsave(r'C:\Users\Chris\Documents\pythonstuff\PHY445\ComptonScattering\data\cesium\cesium137.gif', images, duration=.40)

def convert_to_png(fpath):
    """Convert an fpath to .png"""
    suffix = Path(fpath).suffix
    return fpath.replace(suffix, ".png")

def get_csv_fpaths(dir_fpath):
    """Return list of .csv abs fpath's in the directory"""
    csv_fpaths = []
    for fpath in os.listdir(dir_fpath):
        abs_fpath = os.path.join(dir_fpath, fpath)
        if Path(abs_fpath).suffix == '.csv':
            csv_fpaths.append(abs_fpath)
        
    return csv_fpaths

if __name__ == '__main__':
    fpath = r'C:\Users\Chris\Documents\pythonstuff\PHY445\ComptonScattering\data\calibrations'
    global data 
    data = png_loop(fpath)
