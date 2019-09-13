import numpy as np
import matplotlib.pyplot as plt

def f1(a,x,b,c):
    return (c-a*x)/b

def f2(d,x,e,f):
    return (f-d*x)/e

a = int(input("Ingresa el valor de a: "))
b = int(input("Ingresa el valor de b: "))
c = int(input("Ingresa el valor de c: "))
d = int(input("Ingresa el valor de d: "))
e = int(input("Ingresa el valor de e: "))
f = int(input("Ingresa el valor de f: "))

dets = (a*e)-(d*b)
detx = (c*e)-(f*b)
dety = (a*f)-(d*c)
px=detx/dets
py=dety/dets
print (px,py)


x = np.linspace(px-2,px+2,10)
plt.plot(x,[f1(a,i,b,c) for i in x])
plt.plot(x,[f2(d,i,e,f) for i in x])

plt.axhline(0,color="black")
plt.axvline(0,color="black")
plt.xlim(-11,11)
plt.ylim(-11,11)
plt.grid()
plt.show()
