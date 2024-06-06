
from math import *
import numpy as np
import matplotlib.pyplot as plt
from pylab import *

f = lambda x:sin(x**2)
g = lambda x:x**3
x = np.linspace(0,5,100)
y = f(x)
z = g(x)
plot(x,y)
plot(x,z)
#legend(['sin(x**2)', 'x**3'])
#axis('equal')
plt.show()
