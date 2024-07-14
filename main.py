# MatPlotLib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from icecream import ic

sns.set()
df = sns.load_dataset('tips')
ic(df.head())

# sns.relplot(x='total_bill' , y='tip',data = df, kind='scatter')
# plt.show()
#
# sns.relplot(x='total_bill' , y='tip',data = df, kind='line')
# plt.show()

# Parameters -
# • x, y
# • data
# • hue: It separtes the colour of dots with their types.
# • size
# • col: It can help to have different sex.
# • style: They are used for showing differnt style of points.

# sns.relplot(x='total_bill' , y='tip',data = df, hue='time', style='sex')
# plt.show()

sns.relplot(x='total_bill' , y='tip',data = df, hue='time', col = 'sex')
plt.show()