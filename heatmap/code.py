import sys
import matplotlib
import numpy as np
from numpy import random 
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt

x = np.arange(1,251) 
y = np.arange(250,0, -1) #x & y coords
min_val = 100
max_val = 300
data = random.randint(min_val, max_val, size= (250,250)  )


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
