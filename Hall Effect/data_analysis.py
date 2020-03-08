#Author: Chris Greening 
#Date: 3/3/2020
#Purpose: Data analysis for Hall Effect 

from typing import List, Callable

import matplotlib.pyplot as plt 
import pandas as pd 
from scipy.optimize import curve_fit
from scipy.stats import ttest_ind
import numpy as np 

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
		ans, cov = curve_fit(func, x_data, y_data, sigma=yerr_data) 
		m, b = ans 
		y_fit = func(x_data, m, b)
		
		return y_fit 

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

def import_excel(*args, **kwargs):
	"""Import data to a LabDataFrame"""
	df = pd.read_excel(*args, **kwargs)
	return LabDataFrame(df)

def import_csv(*args, **kwargs):
	"""Import data to a LabDataFrame"""
	df = pd.read_csv(*args, **kwargs)
	return LabDataFrame(df)

def subtract_offset(arr: List[float], offset: float):
	"""Subtract an offset form an array"""
	return arr - offset 

def B_vs_Vh(df):
	"""Return magnetic field and Hall Voltage values from the dataframe"""
	B_cols = ("B", "delB")
	V_H_cols = ("V_H", "delV_H") 
	return df.to_tuple(B=B_cols, V_H=V_H_cols)

def import_magnetocalibs(df):
	R_tuple = ("R", "delR")
	data = df.to_tuple(R=R_tuple)
	return data["R"]

def det_magnetores(orient1, orient2):
	test_results = ttest_ind(orient1, orient2, equal_var=False)
	print(test_results)
	if test_results[1] >= 0.05:
		# In this case accept null hypothesis
		return False
	else:
		# In this case reject null hypothesis
		return True

df_77K = import_excel("data/77K.xlsx")
df_77K_reverse = import_excel("data/77KReverse.xlsx")
df_300K = import_excel("data/300K.xlsx")
df_300K_reverse = import_excel("data/300KReverse.xlsx")
df_leads = import_excel("data/leads_without_mag.xlsx")
df_mag_leads = import_excel("data/leads_with_mag.xlsx")

if __name__ == '__main__':

	from equations import linear
	# Determining if there is magnetoresistance for the Hall Voltage and voltage measurements
	magnetores_results = []

	# Resistance measurements across the set of leads with the magnetic field active
	mag_leads_2_8 = import_magnetocalibs(df_mag_leads)[0][3]
	mag_leads_8_2 = import_magnetocalibs(df_mag_leads)[0][12]

	# Resistance measurements across the set of leads with the magnetic field not active
	leads_2_8 = import_magnetocalibs(df_leads)[0][3]
	leads_8_2 = import_magnetocalibs(df_leads)[0][12]

	# Compiling data and determining if there is magnetoresistance
	mag_sample = [mag_leads_2_8, mag_leads_8_2]
	magless_sample = [leads_2_8, leads_8_2]
	magnetores_results.append(det_magnetores(mag_sample, magless_sample))

	# Resistance measurements across the set of leads with the magnetic field active
	mag_leads_3_4 = import_magnetocalibs(df_mag_leads)[0][5]
	mag_leads_4_3 = import_magnetocalibs(df_mag_leads)[0][8]

	# Resistance measurements across the set of leads with the magnetic field not active
	leads_3_4 = import_magnetocalibs(df_leads)[0][5]
	leads_4_3 = import_magnetocalibs(df_leads)[0][8]

	# Compiling data and determining if there is magnetoresistance
	mag_sample = [mag_leads_3_4, mag_leads_4_3]
	magless_sample = [leads_3_4, leads_4_3]
	magnetores_results.append(det_magnetores(mag_sample, magless_sample))

	# Procedures for handling the cases where there is magnetoresistance and there is no magnetoresistance
	for result in magnetores_results:
		if not result:
			pass
		else:
			# Placeholder for factoring in magnetoresistance should there be any
			print("There is magnetoresistance")

	# Removing voltage offsets from dataframes
	feb_18_offset = 0.003 * 10**(-3)
	feb_25_offset = -0.030 * 10**(-3)
	feb_18_data = [df_77K, df_77K_reverse, df_300K]
	feb_25_data = [df_300K_reverse]

	for df in feb_18_data:
		df["V_H"] -= feb_18_offset

	for df in feb_25_data:
		df["V_H"] -= feb_25_offset

	df_77K.graph(
			'B', 'V_H', yerr_col='delV_H', xlabel='Magnetic Field (mT)', 
			ylabel='Hall Voltage', title='Magnetic Field vs. Hall Voltage at 77K', 
			fit_func=linear, data_label='77K', legend=True
		)

	df_300K.graph(
            'B', 'V_H', yerr_col='delV_H', xlabel='Magnetic Field (mT)',
         			ylabel='Hall Voltage', title='Magnetic Field vs. Hall Voltage at 77K',
         			fit_func=linear, data_label='300K', legend=True
        )


