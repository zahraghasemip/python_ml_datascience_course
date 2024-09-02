import numpy as np 
import pandas as pd 
from pandas import Series , DataFrame 
import matplotlib.pyplot as plt 
from pylab import rcParams 
import seaborn as sb 


rcParams['figure.figsize'] = 5, 4 
sb.set_style('whitegrid')

x=range(1,10)
y=[0.2,0.3,5,7,4,6,0.5,9,1]

wide = (0.4,0.4,0.4,0.8,0.8,0.8,0.4,0.4,0.4)
color = ['salmon']

plt.bar(x,y, width=wide , color=color , align='center')
plt.show()
