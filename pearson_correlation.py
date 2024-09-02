import numpy as np 
import pandas as pd 
from pandas import Series , DataFrame 
import matplotlib.pyplot as plt 
from pylab import rcParams 
import seaborn as sns
import scipy 
from scipy.stats import pearsonr 

rcParams['figure.figsize'] = 8, 4 
sns.set_style('whitegrid')

address='.\\data\\mtcars.csv'
cars=pd.read_csv(address)
cars.columns = ['car_names', 'mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']

# sns.pairplot(cars)
x=cars[['mpg','hp','qsec','wt']]
sns.pairplot(x)
plt.show()
# using scipy to calculate pearson correlation coefficient
mpg = cars['mpg']
hp = cars['hp']
qsec = cars['qsec']
wt= cars['wt']
pearson_coefficient , p_value = pearsonr(mpg, hp)
print('PearsonR Correlation Coefficient 0.3' % (pearson_coefficient))

pearson_coefficient , p_value = pearsonr(mpg, qsec)
print('PearsonR Correlation Coefficient 0.3' % (pearson_coefficient))

pearson_coefficient , p_value = pearsonr(mpg, wt)
print('PearsonR Correlation Coefficient 0.3' % (pearson_coefficient))

# using pandas to calculate pearson correlation coefficient
corr = x.corr()
print(corr)

# using seaborn to visualize the pearson correlation coefficient
sns.heatmap(corr, xticklabels=corr.columns.values, yticklabels=corr.columns.values)
plt.show()
