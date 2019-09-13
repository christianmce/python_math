from sympy.interactive import printing
from sympy import Limit, limit, Symbol, S

printing.init_printing(use_latex='mathjax') 

x = Symbol('x') # Creando el simbolo x.
print(Limit(x**2 - x + 2, x, 2))

res = Limit(x**2 - x + 2, x, 2).doit()
print(res)
