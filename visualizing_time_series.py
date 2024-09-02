import numpy as np 
import pandas as pd 
from pandas import Series , DataFrame 
import matplotlib.pyplot as plt 
from pylab import rcParams 
import seaborn as sns

rcParams['figure.figsize'] = 10,6
sns.set_style('whitegrid')

address='.\\data\\Superstore-Sales.csv'
df= pd.read_csv(address , index_col='Order Date' , encoding='cp1252', parse_dates=True)
df_weekly = df.resample('W').sum()

# Applying a rolling mean with a window of 4 weeks
df_weekly_smoothed = df_weekly['Order Quantity'].rolling(window=4).mean()

# Plotting the aggregated and smoothed data
plt.figure(figsize=(10, 6))
plt.plot(df_weekly.index, df_weekly['Order Quantity'], color='dodgerblue', alpha=0.6, label='Weekly Total')
plt.plot(df_weekly.index, df_weekly_smoothed, color='tomato', linewidth=2, label='4-Week Rolling Mean')

plt.xlabel('Order Date', fontsize=12)
plt.ylabel('Order Quantity', fontsize=12)
plt.title('Superstore Sales - Weekly Order Quantity with Smoothing', fontsize=14)
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()