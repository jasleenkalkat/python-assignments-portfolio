import numpy as np

def roots(f, a, b, tol=1e-10):
    while (b - a) / 2.0 > tol:
        midpoint = (a + b) / 2.0
        if f(midpoint) == 0:
            return midpoint
        elif f(a) * f(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
    return (a + b) / 2.0

def f1(x):
    return np.exp(x) + np.log(x)

def f2(x):
    return np.arctan(x) - x**2

def f3(x):
    return np.sin(x) / np.log(x)

def f4(x):
    return np.log(np.cos(x))

print(roots(f1, 0.1, 1))
print(roots(f2, 0, 2))
print(roots(f3, 3, 4))
print(roots(f4, 5, 7))
