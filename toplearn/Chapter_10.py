import pandas as pd
import numpy as np

# print(pd.to_datetime('2023-09-09 3:45 pm'))

# print(pd.to_datetime(['2023-09-09 3:45 pm','7/8/2010','sep 10 1998']))
# print(pd.to_datetime('2/25/10',format = '%m/%d/%y'))

opsd_daily = pd.read_csv('opsd germany daily.csv')
# print(opsd_daily.shape)
# print(opsd_daily.head(10))
# print(opsd_daily.tail(10))
# print(opsd_daily.dtypes)
# opsd_daily = opsd_daily.set_index('Date')
opsd_daily = opsd_daily.set_index(pd.DatetimeIndex(opsd_daily['Date'].values))
# print(opsd_daily)

print(opsd_daily.loc['2017-10-8':'2017-10-10'])
print(opsd_daily.loc['2017-10'])

