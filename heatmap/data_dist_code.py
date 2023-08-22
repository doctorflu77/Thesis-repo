import sys
import matplotlib
matplotlib.use('Agg')

import seaborn as sns
import matplotlib.pyplot as plt

import numpy as np
from numpy import random 


y = random.randint(140, 300, 100)


sns.distplot(y, hist= False, )
plt.xlabel('Temprature')
plt.ylabel('Probability')
plt.savefig('/Users/doctorflu/Desktop/test2.png')
plt.show()


sys.stdout.flush()