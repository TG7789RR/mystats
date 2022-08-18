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

#negative binomial

# using a new data set as it needs to be bigger
# X = Discrete negative binomial random variable representing number of rolls required to get a number 6 times
# rememeber the dice rolls are even, you would change the probability in a real world example
# P = Probability of roll

n = 100
p = 0.1667
r = 6
x = np.arange(0, n+1)

from scipy.stats import nbinom
nbin_pmf = nbinom.pmf(x, r, p)
print(nbin_pmf)
fig = plt.figure(figsize=(5,5))
ax = plt.bar(x, nbin_pmf, color='orange')
plt.title(f"Negative Binomial Distribution (n={n}, p={p}, r={r})")
plt.savefig('nbinomial.png')

#hypergeometric distribution
from scipy.stats import hypergeom
#these are standard notition I think, not the most logical for me
M = 15 #pop
n = 5 #target - number of red candies
N = 5  #samples we want to draw

x = np.arange(0, n+1)
rv = hypergeom(M, n, N)
pmf_candy = rv.pmf(x)
print(pmf_candy)
fig = plt.figure(figsize=(5,5))
ax = plt.bar(x, pmf_candy, color='green')
plt.title(f"Hyper Geometric Distribution (M={M}, n={n}, N={N})")
plt.savefig('hypergeometric.png')


# not apply the above examples to the flu shot