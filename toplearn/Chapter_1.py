import pandas as pd
import numpy as np

data = np.array(['t','o','p','l','e','a','r','n'])
myseries = pd.Series(data,index=[10,20,30,40,50,60,70,80])
print(myseries)
print(myseries[1:5])
print(myseries.values)


# data = {'first' : 'ali','second' : 'majid','third' : 'hossein'}
# ser = pd.Series(data,index=['second','first','third'])
# print(ser)
# print(ser.values)

