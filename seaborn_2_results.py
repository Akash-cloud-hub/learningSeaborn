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
plt.show()
