# Imports
import pandas as pd
import numpy as np
import os
# Copy CSV File here
data  = pd.read_csv('/home/archie/Neural-Networks-main/Dataset/Two/Currencies/USDINR=X.csv')
# PriceDate Column - Does not contain Saturday and Sunday stock entries
data['Date'] =  pd.to_datetime(data['Date'], format='%m/%d/%y')
data = data.sort_values(by=['Date'], ascending=[True])
data.set_index('Date', inplace=True)
# Samples previous day
data = data.resample('D').ffill().reset_index()
print(data)
# Copy CSV file here
data.to_csv(path_or_buf = "/home/archie/Neural-Networks-main/Dataset/Two/Currencies/USDINR=X.csv", index = False)
