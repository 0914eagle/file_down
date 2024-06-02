
def poly(xs: list, x: float):
    
    return sum([coeff * x**i for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    
    if len(xs) % 2 != 0:
        raise ValueError("The number of coefficients must be even.")
    
    if all(coeff == 0 for coeff in xs[:-1]):
        raise ValueError("All coefficients are zero except the last one.")
    
    def poly(x):
        return sum([coeff * x**i for i, coeff in enumerate(xs)])
    
    def derivative(x):
        return sum([i * coeff * x**(i-1) for i, coeff in enumerate(xs) if i > 0])
    
    x = 1.0
    while abs(poly(x)) > 1e-10:
        x = x - poly(x) / derivative(x)
    
    return x
