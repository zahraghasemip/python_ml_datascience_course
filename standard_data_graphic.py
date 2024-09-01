import numpy as np 
from numpy.random import randn 
import pandas as pd 
from pandas import Series, DataFrame

import matplotlib.pyplot as plt 
from matplotlib import rcParams


# Setting plot size and style (optional)
rcParams['figure.figsize'] = 8, 6  # Setting default figure size
plt.style.use('ggplot')  # Applying a style to the plot

# Data for the line plot
x = range(1, 10)
y = [1, 0, 4, 4, 5, 2, 7, 8, 6]

# Creating the line plot
plt.plot(x, y, marker='o', linestyle='-', color='b', label='Sample Line')

# Adding title and axis labels
plt.title('Line Chart Example with Custom Data')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Displaying the legend
plt.legend()

# Showing the plot
plt.show()
