# Utilizamos distribuciones normales y binomiales para generar valores aleatorios.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import bernoulli, norm

n = 100

s = norm(0, 1).rvs(size=n)
h = norm(0, 0.5 * np.abs(5)).rvs(size=n)

sns.scatterplot(data=s)
sns.scatterplot(data=h)

D = np.random.binomial(n=1, p=0.5, size=n)
histar = h.copy()
histar[D == 1] = np.nan

d2 = np.random.binomial(n=1, p=np.where(s > 0, 0.80, 0))
Hstar = h.copy()
Hstar[D == 1] = np.nan

plt.scatter(s, h, color='gray', alpha=0.8, linewidth=2)
plt.scatter(s, Hstar, color='red', alpha=1, linewidth=3)
plt.show()

s2 = np.random.normal(size=n)
h2 = np.random.normal(loc=1 - np.exp(-0.7 * s2), size=n)
d2 = np.random.binomial(n=1, p=np.where(s2 > 0, 0.1, 0))
Hstar = h2.copy()
Hstar[d2 == 1] = np.nan
plt.scatter(s2, h2, color='gray', alpha=0.8, linewidth=2)
plt.scatter(s2, Hstar, color='red', alpha=1, linewidth=3)
plt.show()

d2 = np.random.binomial(n=1, p=np.where(s > 0, 0.9, 0))


Hstar = h.copy()
Hstar[D == 1] = np.nan



plt.scatter(s, h, color='gray', alpha=0.8, linewidth=2)
plt.scatter(s, Hstar, color='red', alpha=1, linewidth=3)





plt.show()

