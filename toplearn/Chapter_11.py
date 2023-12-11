import pandas as pd
import numpy as np


df = pd.read_csv('opsd germany daily.csv')
# print(df.info)
# print(df.head())
# print(df.describe())
# print('Average Consumption : ',df['Consumption'].mean())
# print('Standard Deviation Consumption : ',df['Consumption'].std())
# print('Correlation between solar and wind : ',df['Solar'].corr(df['Wind']))
print('min wind+solar : ',df['Wind+Solar'].min())
print('max wind+solar : ',df['Wind+Solar'].max())


