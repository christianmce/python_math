# Autor: Dr. Christian Mauricio Castillo Estrada
# Universidad Autónoma de Chiapas - LIDTS Facultad de Negocios

import numpy as np
from matplotlib import pyplot as plt

def f(x):
    return x * x

x = np.arange(-4,4,1/40.)
plt.plot(x,f(x))


section = np.arange(-4, 0, 1/20.)
plt.fill_between(section,f(section))


plt.axhline(0,color="black")
plt.axvline(0,color="black")
plt.xlim(-11,11)
plt.ylim(-11,11)
plt.grid()
plt.show()
