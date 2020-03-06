#Author: Chris Greening 
#Date: 3/3/2020
#Purpose: Data analysis for Hall Effect 

from typing import List 

import matplotlib.pyplot as plt 
import pandas as pd 
from scipy.optimize import curve_fit

from data.data import * 

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

	def fit(self, func, xcol, ycol, yerr_col):
		"""Returns fit data based on a given function and column headers"""

		#TODO: this only works for linear regression, generalize args for nonlinear fits
		x_data = self[xcol]
		y_data = self[ycol]
		yerr_data = self[yerr_col]
		
		ans, cov = curve_fit(func, x_data, y_data, sigma=yerr_data) 
		m, b = ans 
		y_fit = func(x_data, m, b)
		
		return y_fit 

def import_excel(*args, **kwargs):
	"""Import data to a LabDataFrame"""
	df = pd.read_excel(*args, **kwargs)
	return LabDataFrame(df)



def subtract_offset(arr: List[float], offset: float):
	"""Subtract an offset form an array"""
	return arr - offset 

def B_vs_Vh(df):
	"""Return magnetic field and Hall Voltage values from the dataframe"""
	B_cols = ("B", "delB")
	V_H_cols = ("V_H", "delV_H") 
	return tuplize_df(df, B=B_cols, V_H=V_H_cols)

def tuplize_df(df, **kwargs):
	"""
	Return dict containing tuples of data from a DataFrame containing selected 
	columns. Column headers are passed in as kwargs.
	"""

	return_values = {}
	for key, headers in kwargs.items():
		
		#Build list of selected columns then convert to tuple 
		data = []
		for header in headers:
			data.append(df[header])
		else: 
			data = tuple(data)

		return_values[key] = data 

	return return_values


def import_magnetocalibs(df):
	B_tuple = ("B", "delB")
	data: dict = tuplize_df(df, B_data=B_tuple)
	return data["B_data"]


def det_magnetores(orient1, orient2):
	#look into scipy.stats

	pass


if __name__ == '__main__':

	from equations import linear

	df = LabDataFrame(df_77K)
	
	#Fit data 
	x_data = df['B']
	y_fit_data = df.fit(linear, 'B', 'V_H', 'delV_H')
	plt.plot(x_data, y_fit_data)

	#Experimental data 
	y_exp = df['V_H']
	yerr_exp = df['delV_H']
	plt.errorbar(x_data, y_exp, yerr=yerr_exp, fmt='o')
	
	plt.show()
	

