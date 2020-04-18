#Author: Chris Greening 
#Date: 3/3/2020
#Purpose: Leveraging pandas for lab specific data structures and functions 

from typing import List, Callable

import matplotlib.pyplot as plt 
import pandas as pd 
from scipy import stats, optimize 
from uncertainties import ufloat 

import numpy as np 

from equations import linear 

class LabDataFrame(pd.DataFrame):
	def __init__(self, *args, **kwargs):
		"""
		Wrapper around pandas.DataFrame with tasks specialized to what 
		we will be doing for lab.
		"""
		super().__init__(*args, **kwargs)
		self.args = args 
		self.kwargs = kwargs 
	
	def to_tuple(self, **kwargs):
		return_values = {}
		for key, headers in kwargs.items():
			
			#Build list of selected columns then convert to tuple 
			data = []
			for header in headers:
				data.append(self[header])
			else: 
				data = tuple(data)

			return_values[key] = data 

		return return_values

	def fit(
			self, func: Callable[[float], float], 
			xcol: str, ycol: str, 
			yerr_col: str
		) -> np.array:
		"""Returns y-axis fit data based on a given function and column headers"""

		#TODO: this only works for linear regression, generalize args for nonlinear fits
		x_data = self[xcol]
		y_data = self[ycol]
		yerr_data = self[yerr_col]
		
		#Create the y-axis fit data 
		ans, cov = optimize.curve_fit(func, x_data, y_data, sigma=yerr_data) 
		m, b = ans 
		y_fit = func(x_data, m, b)
		
		return y_fit, m, b 

	def chisquare(self, obs_col, fit_col):
		"""Calculate the chisquare between two columns"""

		observed = self[obs_col].to_numpy()
		expected = self[fit_col].to_numpy()
		return stats.chisquare(observed, f_exp=expected)

	def graph(
			self, xcol: str, ycol: str, xlabel: str ='', 
			ylabel: str ='', title: str ='', xerr_col: str = '', 
			yerr_col: str ='', fit_func: Callable[[float], np.array] =None,
			data_label: str ='', legend: bool =False
		) -> None:
		"""
		Graph data from our LabDataFrame

		Parameters
			REQUIRED:
			xcol :: str 
				Column header for the independent variable 
			ycol :: str 
				Column header for dependent variable.
			
			OPTIONAL:	
			xlabel :: str = ''
				Label for the x-axis 
			ylabel :: str = ''
				Label for the y-axis 
			title :: str = ''
				Title for the plot
			xerr_col :: str = ''
				Column header for x-axis error data  
			yerr_col :: str = ''
				Column header for y-axis error data
			fit_func :: Callable[[float], np.array] = None 
				Function for fitting the data with 
			legend :: bool = False 
				Plot legend
		"""

		x_data = self[xcol]
		y_data = self[ycol]

		#x-axis error data
		if xerr_col:
			xerr_data = self[xerr_col]
		else: 
			xerr_data = np.zeros(len(x_data))

		#y-axis error data 
		if yerr_col: 
			yerr_data = self[yerr_col]
		else: 
			yerr_data = np.zeros(len(y_data))

		#Plot experimental data 
		plt.errorbar(x_data, y_data, xerr=xerr_data, yerr=yerr_data, fmt='.', label=data_label)
		plt.xlabel(xlabel)
		plt.ylabel(ylabel)
		plt.title(title)

		if legend:
			plt.legend()

		#Get fit data and plot it to the graph 
		if fit_func is not None:
			if not yerr_col:
				raise ValueError('Cannot fit data without specified y-axis errors')
			y_fit = self.fit(fit_func, xcol, ycol, yerr_col)
			fit_label = f'{data_label} fit'
			plt.plot(x_data, y_fit, label=fit_label)

		plt.show()

	def sort_values(self, *args, **kwargs):
		"""Return the sorted DataFrame as a LabDataFrame"""

		sorted_df = super().sort_values(*args, **kwargs)
		return LabDataFrame(sorted_df)

	def round(self, *args, **kwargs):
		rounded_df = super().round(*args, **kwargs)
		return LabDataFrame(rounded_df)

def import_excel(*args, **kwargs):
	"""Import data to a LabDataFrame"""
	df = pd.read_excel(*args, **kwargs)
	return LabDataFrame(df)

def import_csv(*args, **kwargs):
	"""Import data to a LabDataFrame"""
	df = pd.read_csv(*args, **kwargs)
	return LabDataFrame(df)

def import_spe(fpath):
	"""Import data from an Spe file to a LabDataFrame"""
	"""Convert a Spectrum file to a .csv"""

    path_obj = Path(fpath)
    suffix = path_obj.suffix
    

    with open(fpath, 'r') as infile:
        lines = infile.readlines()
       
    #carve metadata off the .Spe files 
    relevant = lines[12:]

    end_index = relevant.find("$ROI:")
    relevant = relevant[:end_index]

    df = pd.DataFrame(relevant)

