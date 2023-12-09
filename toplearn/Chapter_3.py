import pandas as pd
import numpy as np

data = np.array(['k','a','s','r','a'])
myseries = pd.Series(data,index=['first','second','third','fourth','fifth'])
print(myseries.iloc[3])
print(myseries.loc['first'])
