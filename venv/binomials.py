import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
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


# now apply the above examples to the flu shot example that jim had
#geometric - need split view with two different distributions based on those who had jab and those that didnt
#didn't complete this in the end, may finish at later date

#zscores - there are differnt ways to do this

#calc sd's for each value in array from mean
print("zscores from known values")
from scipy import stats
values = np.array([4,5,6,6,6,7,8,9,9,12,13,13,14,18])
print('Mean = ' + np.mean(values).astype(str))
zscores = stats.zscore(values)
print(zscores)
print("this is returning the number of SD for each value")

#zcore on df
print("zscores from a DF")
df = pd.DataFrame.from_dict({
    'Name': ['Nik', 'Kate', 'Joe', 'Mitch', 'Alana'],
    'Age': [32, 30, 67, 34, 20],
    'Income': [80000, 90000, 45000, 23000, 12000],
    'Education' : [5, 7, 3, 4, 4]
})

print("for a specific column")
df['Income zscore'] = stats.zscore(df['Income'])
print(df.head())

#this can be used to normalise values
df = df.select_dtypes(include='number').apply(stats.zscore)
print(df.head())

#from a population mean
print("z score from pop mean")
import statistics
mean = 7
standard_deviation = 1.3

zscore = statistics.NormalDist(mean, standard_deviation).zscore(5)
print(zscore)

#apply the above to jim example
print("z score for jim example")

orangemean = 140
applemean = 100
orangesd = 25
applesd = 15
print("Jim example of Apple/Orange of 100g with differnt pops")
ozscore = statistics.NormalDist(orangemean, orangesd).zscore(100)
apscore = statistics.NormalDist(applemean, applesd).zscore(110)
print(ozscore)
print(apscore)


