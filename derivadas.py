import sympy as sp

x = sp.Symbol('x')

derivada1 = sp.diff( pow(sp.E,sp.ln(x**2) ) )
print(derivada1)


derivada2 = sp.diff( derivada1 )
print(derivada2)

derivada = sp.diff( (x**3+2)/3 )
print(derivada)
