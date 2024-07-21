# MatPlotLib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from icecream import ic

sns.set()
df = sns.load_dataset('tips')
ic(df.head())

#These are strip plots

# sns.catplot(x='sex' , y='total_bill' ,data = df)
# plt.show()

# sns.catplot(x='sex' , y='total_bill' ,data = df, jitter= 0.25 , hue = 'smoker')
# plt.show()

# sns.catplot(x='sex' , y='total_bill' ,data = df, jitter= 0.005 , hue = 'smoker')
# plt.show()

# These are swarm plots
# Swarm plots are usually used for small data sets , Swarm plot uses an algorithm to seperate overlying data  .

# sns.catplot(x='sex' , y='total_bill' ,data = df , kind = 'swarm')
# plt.show()

# sns.catplot(x='sex' , y='total_bill' ,data = df , kind = 'swarm' , hue='size')
# plt.show()

# box and whisker plot
# sns.catplot(x='sex' , y='total_bill' ,data = df , kind = 'box')
# plt.show()

