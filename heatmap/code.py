import sys
import matplotlib
import numpy as np
from numpy import random 
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt

temp = pd.read_csv('/Users/doctorflu/Desktop/Thesis/sampledata.csv')
temp.dropna(inplace= True)

x = temp.to_string()
data = temp.iloc[:, 1:].values


fig, ax = plt.subplots()

heatmap = plt.imshow(data, cmap= 'Spectral_r') #cmap = Spectral_r
plt.title('Heatmap')
plt.xlabel('X - coord')
plt.ylabel('Y - coord')
cbar = plt.colorbar(heatmap)
plt.gca().invert_yaxis()

plt.savefig('/Users/doctorflu/Desktop/Thesis/Thesis-repo/heatmap/test1.png')
plt.show()
sys.stdout.flush()
