import matplotlib.pyplot
import numpy as np
from numpy import meshgrid

delta = 0.025
xrange = np.arange(-np.pi, np.pi, delta)
yrange = np.arange(-np.pi, np.pi, delta)
X, Y = meshgrid(xrange, yrange)

# F is one side of the equation, G is the other
F = 2 * np.cos(X)
G = np.cos(Y)

matplotlib.pyplot.contour(X, Y, (F + G), [1], colors='black')
matplotlib.pyplot.show()