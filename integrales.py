from sympy import integrate,cos
from sympy.abc import x,y,a,b,c,d,pi
from sympy import simplify

I1 = integrate(1, (y,d,c))
print( simplify( integrate(I1, (x,b,a) ) ) )


print(integrate(cos(x), (x,0,pi/2.0)))

