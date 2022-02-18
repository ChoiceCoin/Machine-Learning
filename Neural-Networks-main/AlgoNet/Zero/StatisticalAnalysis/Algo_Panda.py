#Imports
import pandas as pd
from pandas import DataFrame

#Define variable for file
df = pd.read_csv('ALGO_DATA.csv')

#Process Data
print(df.head())
print(df.tail())
print(df.index)
print(df.columns)
print("-----")
#Describe Data
print(df.describe())
#Median
print('median')
print(df.median())
print("-----")
#Mode
print('mode')
print(df.mode())
print("-----")
