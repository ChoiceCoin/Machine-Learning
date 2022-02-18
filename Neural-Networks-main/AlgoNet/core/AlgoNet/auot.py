import pandas as pd
import numpy as np
import os
# Copy CSV File here
def auto(filename):
    data  = pd.read_csv(filename)
    # PriceDate Column - Does not contain Saturday and Sunday stock entries
    data = data.fillna(method = "ffill")
    # Copy CSV file here
    data.to_csv(path_or_buf = filename, index = False)