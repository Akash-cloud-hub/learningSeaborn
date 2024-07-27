# MatPlotLib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from icecream import ic

sns.set()
df = sns.load_dataset('iris')
ic(df.head())

sns.catplot(x='species' , y='sepal_length' , data = df , kind='violin' , hue='species')
# plt.show()
plt.clf()



#homework
sns.catplot(x='species' , y='sepal_length' , data = df , kind='swarm' , hue='species')
# plt.show()
plt.clf()


sns.set()
df = sns.load_dataset('tips')
ic(df.head())
sns.catplot(x='day' , y='total_bill' , data = df , kind='violin' , hue="sex" )
plt.show()
