#Author: Chris Greening 
#Date: 3/3/2020
#Purpose: Data analysis for Hall Effect 

from typing import List 

import pandas as pd 
import matplotlib.pyplot as plt 

def subtract_offset(arr: List[float], offset: float):
	"""Subtract an offset form an array"""
	return arr - offset 

def B_vs_Vh(df):
	"""Return magnetic field and Hall Voltage values from the dataframe"""
	B = (df.B.to_numpy(), df.delB.to_numpy())
	V_H = (df.V_H.to_numpy(), df.delV_H.to_numpy())
	return B, V_H

def tuplize_df(df, **kwargs):
	"""
	This function is a general means of taking data (with uncertainty) from a dataframe and making tuples
	"""
	return_values = {}
	for key in kwargs:
		col1, col2 = kwargs[key]

		central = df[col1]
		uncertainty = df[col2]
		return_values[key] = (central, uncertainty)

	return return_values


def import_magnetocalibs(df):
	B_tuple = ("B", "delB")
	data: dict = tuplize_df(df, B_data=B_tuple, V_H=V_H)
	return data["B_data"]


def det_magnetores(orient1, orient2):
	#look into scipy.stats

	pass

#dataframes with Hall Effect data 
df_77K = pd.read_excel("data/77K.xlsx")
df_77K_reverse = pd.read_excel("data/77KReverse.xlsx")
df_300K = pd.read_excel("data/300K.xlsx")
df_300K_reverse = pd.read_excel("data/300KReverse.xlsx")

if __name__ == '__main__':
	# B, V = B_vs_Vh(df_77K)

	B_cols = ("B", "delB")
	V_H = ("V_H", "delV_H")
	data = tuplize_df(df_77K, B=B_cols, V_H=V_H)


	# plt.plot(B[0], V[0])
	# plt.title("77K")
	# plt.show()

