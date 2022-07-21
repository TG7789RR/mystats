import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

n = 10
p = 0.1667
x = np.arange(0, n+1)


binomial_pmf = binom.pmf(x, n, p)
print(binomial_pmf)

fig = plt.figure(figsize=(5,5))
ax = plt.bar(x, binomial_pmf, color='blue')
plt.title(f"Binomial Distribution (n={n}, p={p})")
plt.savefig('binomial.png')


#geometric
from scipy.stats import geom

geom_pmf = geom.pmf(x, p)
print(geom_pmf)

fig = plt.figure(figsize=(5,5))
ax = plt.bar(x, geom_pmf, color='red')
plt.title(f"Geometric Distribution (n={n}, p={p})")
plt.savefig('geom.png')
