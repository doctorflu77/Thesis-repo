import sys
import matplotlib
from numpy import random 
matplotlib.use('Agg')

import matplotlib.pyplot as plt

x = list(range(1,101)) #if x points are not mentioned -> (1,2,3,...)
y = random.randint(100, 300, size= 100)
data = [{'x' : x_val, 'y': y_val} for x_val, y_val in zip(x,y)]
y1 = y
for i in y1:
    i = i/3


plt.scatter(x,y, c= y1, cmap= 'Reds') #cmap = Spectral_r
plt.title('Heatmap')
plt.xlabel('Serial No.')
plt.ylabel('Temprature')
plt.colorbar()

plt.savefig('/Users/doctorflu/Desktop/ML Thesis/heatmap/test1.png')
plt.show()
sys.stdout.flush()
