#Author: Chris Greening 
#Date: 3/5/2020
#Purpose: Data loaded from excel spreadsheets 

import pandas as pd 

#dataframes with Hall Effect data
df_77K = pd.read_excel("data/77K.xlsx")
df_77K_reverse = pd.read_excel("data/77KReverse.xlsx")
df_300K = pd.read_excel("data/300K.xlsx")
df_300K_reverse = pd.read_excel("data/300KReverse.xlsx")
df_leads = pd.read_excel("data/leads.xlsx")