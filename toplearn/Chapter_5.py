import numpy as np
import pandas as pd

# data = {
#     'name':['ali','hamid','sadegh','reza'] ,
#     'age':[18,40,23,25],
#     'city':['tehran','shiraz','tabriz','esfahan'],
#     'teaching':['pandas','numpy','scipy','matplotlib']
#     }

# df = pd.DataFrame(data,index=[True,False,True,False])
# print(df.loc[True])
# print('----------------------------')
# print(df.loc[False])
# print('----------------------------')
# print(df['age']>24)
# print('----------------------------')
# print(df['city']=='tehran')
# print('----------------------------')
# print(df[df.index<=1])
# print('----------------------------')
# print(df[df.columns=='city'])
# print('----------------------------')
# print(df[df['age']>=25])


data = {
    'name':['ali','hamid',np.nan,'reza'] ,
    'age':[18,40,23,25],
    'city':['tehran','shiraz','tabriz',np.nan],
    'teaching':['pandas','numpy','scipy','matplotlib']
    }
df = pd.DataFrame(data)
print(df[df.notnull()])
print('----------------------------')
print(df[df.isnull()])
print('----------------------------')
print(df.fillna('undifind'))
print('----------------------------')
print(df.dropna())

