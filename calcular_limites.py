from sympy import Limit, Symbol, S, sqrt

x = Symbol('x') # Creando el simbolo x.


res = Limit(x**2 - x + 2, x, 2).doit()
print("Para x**2 -x + 2, el limite es  " + str(res) + "  cuando x = 2")


res2 = Limit(1/x, x, S.Infinity).doit()
print("Para 1/x, el limite es  " + str(res2) + "  cuando x = infinito")


res3 = Limit((x-2)/(sqrt(7+x)-3), x, 2).doit()
print("Para (x-2)/raiz(7+x)-3, el limite es  " + str(res3) + "  cuando x =2")


e1 = pow(32*x**10 - 4*x**7 + 4*x**3 - 3*x**2,1/5)
e2 = pow(8*x**6 - 5*x**4 + 1,1/3)
e3 = pow(64*x**12 - 9*x + 1,1/6)
e4 = pow(128*x**14 - 5*x**9 + 7*x,1/7)

res4 = Limit((e1+e2)/(e3+e4),x,0).doit()
print(res4)
