import matplotlib.pyplot as plt 
import seaborn as sns  
from pandas import DataFrame
data = {'names':['shana' , 'mina' , 'niki' , 'fei' , 'zara' , 'lili' , 'jack'],
        'age':[20,22,28,21,24,24,25],
        'gender':['female','female','female','female','female','female','male'],
        'rank':[2,3,1,7,4,5,6]}
df=DataFrame(data)
print(df)

# creating simple bar chart
plt.bar(df['names'] , df['age'])
plt.xlabel('Names')
plt.ylabel('Age')
plt.title('comparing ages')
plt.show()