#concatenating and transforming data
import numpy as np  
import pandas as pd 
from pandas import Series, DataFrame 

DF_obj = DataFrame(np.arange(36).reshape(6,6))
DF_obj_2 = DataFrame(np.arange(15).reshape(5,3))

concatobjects=pd.concat([DF_obj,DF_obj_2],axis=1)
print(concatobjects)

# drop data
dropping=DF_obj.drop([0,2],axis=1)
print(dropping)

# adding data
series_obj = Series(np.arange(6))
series_obj.name = "added_variable"
print(series_obj)
variable_added = DataFrame.join(DF_obj,series_obj)
print(variable_added)
added_datatable = pd.concat([variable_added, variable_added], ignore_index=True)
print(added_datatable)

# sorting data
DF_sorted = DF_obj.sort_values(by=[5],ascending=[False])
print(DF_sorted)



