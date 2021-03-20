import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
#for latex equations
v=np.linspace(0,10,100)
plt.plot(v,np.exp(-v/2)/2)
plt.xlabel("$x$")
plt.ylabel("$f_X(x)$")
plt.show()
