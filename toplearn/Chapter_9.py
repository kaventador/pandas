import pandas as pd
import numpy as np

df = pd.read_csv('file.csv')
# print(df)
mygp = df.groupby('Name')
# print(mygp.groups)
# def myfunction(self):
#     return df.loc[self].Test1 > df.loc[self].Test2
#
# print(df.groupby(myfunction).groups)


# print(mygp['Test3'].agg(np.mean))


# for name,group in mygp:
#     print('Name')
#     print(group)


getgp = mygp.get_group('Ali')
print(getgp)

