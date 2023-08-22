import sys
import matplotlib
import numpy as np
from numpy import random 
matplotlib.use('Agg')

import matplotlib.pyplot as plt

x = np.arange(1,26) #if x points are not mentioned -> (1,2,3,...)
y = np.arange(25,0, -1) #x & y coords
min_val = 100
max_val = 300
data = random.randint(min_val, max_val, size= (25,25)  )


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
