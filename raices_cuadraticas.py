import math
from pip._vendor.distlib.compat import raw_input

def discriminante(a,b,c):
    discrim = pow(b,2)-(4*a*c)
    return discrim

def raices(a,b,disc):
    raiz1=(-b+math.sqrt(disc))/(2*a)
    raiz2=(-b-math.sqrt(disc))/(2*a)
    return raiz1,raiz2

print("Calculo de raices")
a=float(raw_input("a: "))
b=float(raw_input("b: "))
c=float(raw_input("c: "))

disc = discriminante(a, b, c)


if disc<0:
    print("no hay raices reales")
else:
    print( str(raices(a,b,disc)) )
    

