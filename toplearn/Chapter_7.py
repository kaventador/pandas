import numpy as np
import pandas as pd

df = pd.read_csv('file.csv')
# print(df)
# print(np.shape(df))
# print(df.shape)
# print(df.count())
# print(df.values)
# print(df.describe())
# print(df.set_index('Age'))
print(df.sort_values('Age',ascending=False,inplace=False))
