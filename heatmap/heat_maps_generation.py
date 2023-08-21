import sys
import matplotlib
from numpy import random 
matplotlib.use('Agg')

import matplotlib.pyplot as plt

x = list(range(1,11)) #if x points are not mentioned -> (1,2,3,...)
y = random.randint(100, 300, size= 10)
data = [[],[],[],[],[],[],[],[],[],[]]
data1 = random.rand(12,12)

y1 = y
for i in y1:
    i = i/3

fig, ax = plt.subplots()

heatmap = plt.imshow(data1, cmap= 'Spectral_r') #cmap = Spectral_r
plt.title('Heatmap')
plt.xlabel('Serial No.')
plt.ylabel('Temprature')
cbar = plt.colorbar(heatmap)

plt.savefig('/Users/doctorflu/Desktop/Thesis/Thesis-repo/heatmap/test1.png')
plt.show()
sys.stdout.flush()
