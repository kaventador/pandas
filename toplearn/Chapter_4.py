import numpy as np
import pandas as pd

# mylist = ['kasra', 'pandas', 'toplearn']
# df = pd.DataFrame(mylist,index=['first','second','third'],columns=['test'])
#

data = {
    'name':['kasra','setareh','arezoo'],
    'age':[25,23,50],
    'city':['torento','torento','vancover']
        }
df = pd.DataFrame(data,index=['person1','person2','person3'])
print(df)
print("-----------------------")
print(df[['name','city']])
print("-----------------------")
print(df.loc[['person2','person1']])
print("-----------------------")
print(df.loc['person1':'person3'])
print("-----------------------")
print(df.iloc[[1]])
print("-----------------------")
print(df.iloc[0:2,1:2])


