# /filling missing values using fillna(),replace(), interpolate()

import numpy as np  
import pandas as pd 
from pandas import DataFrame 

data = {'names':['Mary','Julia','Andy','Nina','Shana','Zara','Jack'],
        'age':[21,23,20,24,25,27,28],
        'gender':['female','female','male','female','female','female','male'],
        'rank':[2,3,4,5,1,6,7]}
ranking_df = DataFrame(data)
ranking_df.iloc[2:5,1]=np.nan
ranking_df.iloc[3:6,3]=np.nan
ranking_df.iloc[3,:]=np.nan
print(ranking_df)
print(ranking_df.isnull())
print(ranking_df.notnull())


bool_series = pd.isnull(ranking_df['age'])
age_missing_rows=ranking_df[bool_series]
print(age_missing_rows)

# /filling a missing value with a single value
passzero=ranking_df.fillna(0)
print(passzero)

x=ranking_df.fillna(method='pad')
print(x)
y=ranking_df.fillna(method='bfill')
print(y)
z=ranking_df.interpolate(method='linear')
print(z)
d=ranking_df.dropna()
print(d)

# /rows with no missing values
a=ranking_df.dropna(axis=0)
print(a)