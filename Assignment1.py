def arctan_approx(x):
    if x < 0 or x > 1:
        return "Error!"
    a = 0
    n = 0
    term = x
    error_bound = x ** (2 * n + 1) / (2 * n + 1)
    while abs(term) > 0.0001:
        a += term
        n += 1
        term = (-1) ** n * x ** (2 * n + 1) / (2 * n + 1)
        error_bound = x ** (2 * n + 1) / (2 * n + 1)
    return (a, n, error_bound)
print(arctan_approx(-1))
print(arctan_approx(0))
print(arctan_approx(0.25))
print(arctan_approx(0.5))
print(arctan_approx(0.75))
print(arctan_approx(1))
