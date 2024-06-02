
import math

def poly(xs: list, x: float):
    
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    
    if len(xs) % 2 != 0:
        raise ValueError("The number of coefficients must be even.")
    
    if xs[0] == 0:
        raise ValueError("The largest non-zero coefficient must be the first element.")
    
    def poly_eq(x):
        return poly(xs, x)
    
    from scipy.optimize import fsolve
    return fsolve(poly_eq, 0)[0]

