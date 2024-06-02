
def poly(xs: list, x: float):
    
    return sum([coeff * x**i for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    
    if len(xs) % 2 != 0:
        raise ValueError("Number of coefficients must be even.")
    
    if xs[-1] == 0:
        raise ValueError("Largest non-zero coefficient must be non-zero.")
    
    def poly_eq(x):
        return poly(xs, x)
    
    from scipy.optimize import fsolve
    return fsolve(poly_eq, 0)[0]
