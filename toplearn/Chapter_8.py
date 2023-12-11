import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# df = pd.read_csv('file.csv')
# df['Grade'].plot()
# plt.show()


# df_1 = pd.DataFrame({'name':['ali','kasra','sadegh'],
#                      'grade':[70,85,63],
#                      'qualification':['mid','high','low']})
# df_2 = pd.DataFrame({'name':['ali','kasra','sadegh'],
#                      'grade':[56,82,73],
#                      'qualification':['low','high','mid']})
# df_3 = pd.DataFrame({'name':['ali','kasra','sadegh'],
#                      'grade':[42,72,84],
#                      'email':['test1','test2','test3']})

# print(pd.merge(df_1,df_2,on='name'))

# df_1.set_index('name',inplace=True)
# df_2.set_index('name',inplace=True)
# my_join = df_1.join(df_3,lsuffix='_left')
# print(my_join)



df_1 = pd.DataFrame({'name':['ali','sara','sadegh','kasra'],
                     'grade':[70,85,63,45],
                     'qualification':['mid','high','low','low']})
df_2 = pd.DataFrame({'name':['omid','kasra','sadegh','kasra'],
                     'grade':[56,82,73,89],
                     'qualification':['low','high','mid','high']})
df_3 = pd.DataFrame({'name':['ali','kasra','sadegh'],
                     'grade':[42,72,84],
                     'email':['test1','test2','test3']})


merged = pd.merge(df_1,df_2,on='name',how='outer')
merged.set_index('name',inplace=True)
print(merged)

