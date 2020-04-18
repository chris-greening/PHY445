#Author: Chris Greening 
#Date: 3/12/2020 
#Purpose: Convert .Spe file to .csv 

from pathlib import Path 

import pandas as pd 
from scipy.signal import find_peaks

def convert_file(fpath):
    """Convert a Spectrum file to a .csv"""
    
    path_obj = Path(fpath)
    suffix = path_obj.suffix
    
    
    csv_fpath = 


    with open(fpath, 'r') as infile:
        lines = infile.readlines()
       
    #carve metadata off the .Spe files 
    relevant = lines[12:]

    end_index = relevant.find("$ROI:")
    relevant = relevant[:end_index]

    df = pd.DataFrame(relevant)


if __name__ == '__main__':
    abs_fpath = r''
    spe = convert_file(abs_fpath)


