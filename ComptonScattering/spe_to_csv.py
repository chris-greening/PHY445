#Author: Chris Greening 
#Date: 3/12/2020 
#Purpose: Convert .Spe file to .csv 

import os 
from pathlib import Path 

import pandas as pd 
from scipy.signal import find_peaks

from labpandas import import_spe

def convert_folder_spe(fpath):
    """Convert all the .spe files within a folder to .csv's"""
    
    #Filter dir down to only .Spe files 
    spe_files = [os.path.join(fpath, infile) 
                for infile in os.listdir(fpath) 
                    if Path(infile).suffix == '.Spe']
    
    #Import .Spe files as LabDataframes
    dataframes = [(import_spe(fpath), create_csv_fpath(fpath)) for fpath in spe_files]

    #Write each of the imported Spe's as .csv 
    for df, fpath in dataframes:
        df.to_csv(fpath, index=False)

def create_csv_fpath(fpath):
    """Removes the suffix of fpath arg and returns as .csv"""
    fpath_suffix = Path(fpath).suffix 
    return fpath.replace(fpath_suffix, ".csv")

if __name__ == '__main__':
    fpath = r'C:\Users\Chris\Documents\pythonstuff\PHY445\ComptonScattering\data\calibrations\Spe'
    convert_folder_spe(fpath)


