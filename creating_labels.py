import numpy as np 
import pandas as pd 
from pandas import Series , DataFrame 
import matplotlib.pyplot as plt 
from pylab import rcParams 
import seaborn as sb 

rcParams['figure.figsize'] = 5, 4 
sb.set_style('whitegrid')


address='.\\data\\mtcars.csv'
cars=pd.read_csv(address)
cars.columns = ['car_names', 'mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']

mpg=cars.mpg

fig=plt.figure()
ax = fig.add_axes([.1,.1,1,1])

mpg.plot()

ax.set_xticks(range(32))
ax.set_xticklabels(cars.car_names, rotation=60, fontsize='medium')
ax.set_title('miles per gallon of cars in mtcars')

ax.set_xlabel('car names')
ax.set_ylabel('miles/gal')

ax.legend(loc='best')

plt.show()