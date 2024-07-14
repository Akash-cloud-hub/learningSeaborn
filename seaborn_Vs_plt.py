# MatPlotLib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

x = np.linspace(0,10,1000)
plt.plot(x,np.sin(x),x,np.cos(x))
# plt.show()
plt.clf()

sns.set()
x = np.linspace(0,10,1000)
plt.plot(x,np.sin(x),x,np.cos(x))
plt.show()
