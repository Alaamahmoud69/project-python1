import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

#import data

data = pd.read_csv('C:/Users/ALLA/Desktop/SampleSuperstore.csv')
print(data)
print('___________________________________')

#data cleaning

print(data.isnull().sum())
print('___________________________________')

print(data.info())
print('___________________________________')


#data exploration

print(data.describe())
print('___________________________________')
print(data['Profit'].groupby(data['Region']).max())

print('____________________________________')
print(data['Profit'].groupby(data['Ship Mode']).max())

print('___________________________________')
print(data['Sales'].groupby(data['State']).agg(['min','max','mean','sum','count']))

print('___________________________________')
print(data['Quantity'].groupby(data['Category']).sum())

print('___________________________________')
print(data['Profit'].groupby(data['Segment']).max())

print('___________________________________')
print(data['Quantity'].groupby(data['Region']).count())

print('___________________________________')
print(data['Sales'].groupby(data['Category']).agg(['min','max','mean','sum','count']))


# data visualization

plt.bar(data['Ship Mode'],data['Profit'],color='red',edgecolor ='black',width=0.4)
plt.show()

plt.bar(data['Segment'],data['Sales'],color='green',edgecolor='black',width=0.4)
plt.show()

plt.bar(data['Category'],data['Quantity'],color='b',edgecolor='black',width=0.4)
plt.show()

plt.bar(data['Region'],data['Profit'],color='yellow',edgecolor='black',width=0.4)
plt.show()

PI = data['Profit'].groupby(data['Ship Mode']).max()
plt.pie(PI.values,labels=PI.index,autopct ='%1.4f%%')
plt.show()

PI1 = data['Sales'].groupby(data['Region']).max()
plt.pie(PI1.values,labels=PI1.index,autopct ='%1.4f%%')
plt.show()



plt.scatter(data['City'],data['Profit'],color='black')
plt.show()

plt.hist2d(data['percentage'],data['Sales'])


















