import streamlit as st 
import time 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

animals = ['cow','cat','dog','rooster']
heights = [100,30,40,25]
weights = [400,4,6,2]
fig,ax = plt.subplots()

x= np.arange(len(heights))
width = 0.40

ax.bar(x-0.2, heights, width , color='red')
ax.bar(x+0.2, heights, width , color='orange')

ax.legend(['heights' , 'weight'])
ax.set_xticks(x)
ax.set_xticklabels(animals)

st.pyplot(fig)

explode = [0.2, 0.1 , 0.1 , 0.1]
plot_pie , ax = plt.subplots()
ax.pie(heights , explode=explode , labels=animals , autopct='%1.1f%%',shadow=True)
ax.axis('equal')
st.pyplot(plot_pie)