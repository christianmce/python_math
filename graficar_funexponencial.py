import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(x)

x=np.linspace(0,10,100)

plt.plot(x,f(x))
plt.xlabel(‘EJE X')
plt.ylabel('EJE Y')
plt.title('Funcion EXPONENCIAL')

plt.grid()
plt.show()
