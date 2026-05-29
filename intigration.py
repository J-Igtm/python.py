from sympy import *

x = symbols('x')
expr = sin(x)

result = integrate(expr, x)
print(result)