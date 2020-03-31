import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
from scipy.interpolate import interpn

mu, sigma = 0, 0.1  # mean and standard deviation
num = 1000
s = np.random.normal(mu, sigma, num)

# Generate fake data
x = np.random.normal(size=num)
y = x * 3 + np.random.normal(size=num)

# Calculate the point density
xy = np.vstack([x, y])
z = gaussian_kde(xy)(xy)

# Sort the points by density, so that the densest points are plotted last
idx = z.argsort()
xs, ys, zs = x[idx], y[idx], z[idx]

fig, ax = plt.subplots()
ax.scatter(x, y, c=z, s=100, edgecolor='')

fig, ax = plt.subplots()
ax.scatter(xs, ys, c=zs, s=50, edgecolor='')


"""
Scatter plot colored by 2d histogram
"""

fig, ax = plt.subplots()
data, x_e, y_e = np.histogram2d(x, y, bins=20)
z = interpn((0.5 * (x_e[1:] + x_e[:-1]), 0.5 * (y_e[1:] + y_e[:-1])),
            data, np.vstack([x, y]).T, method="splinef2d", bounds_error=False)

# Sort the points by density, so that the densest points are plotted last
idx = z.argsort()
x, y, z = x[idx], y[idx], z[idx]
ax.scatter(x, y, c=z)
plt.show()
