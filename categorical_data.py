import numpy as np 
import pandas as pd 
from pandas import Series, DataFrame 


address = '.\\data\\mtcars.csv'
cars=pd.read_csv(address)
cars.columns = ['car_names', 'mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']
cars.index = cars.car_names

cars.head(15)
carb = cars.carb 
print(carb.value_counts())

cars_cat = cars[['cyl' , 'vs' , 'am' , 'gear' , 'carb']]
print(cars_cat.head())
gears_group = cars_cat.groupby('gear')
print(gears_group.describe())

# transforming variables to categorical data type
cars['group'] = pd.Series(cars.gear, dtype='category')
dd=cars['group'].dtypes
print(cars['group'].value_counts())

# describing categorical data with crosstabs
print(pd.crosstab(cars['am'], cars['gear']))