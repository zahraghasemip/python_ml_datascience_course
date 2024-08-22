import numpy as np  
import pandas as pd 
from pandas import DataFrame 

numbers_df = DataFrame(np.arange(0,90,3).reshape(10,3) , index = ['row 1' , 'row 2' , 'row 3' , 'row 4' , 'row 5' , 'row 6' , 'row 7' , 'row 8' , 'row 9' , 'row 10'],
columns = ['column 1' , 'column 2' , 'column 3'])

a=numbers_df.iloc[[1,2,3],[1,2]]
print(a)
mask= numbers_df>30
print(mask)
b=numbers_df[mask]
print(b)
numbers_df [numbers_df>30] = 0
print(numbers_df)