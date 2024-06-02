
def poly(xs: list, x: float):
    
    return sum([coeff * x**i for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    
    if len(xs) % 2 != 0:
        raise ValueError("The number of coefficients must be even.")
    
    if xs[-1] == 0:
        raise ValueError("The largest non-zero coefficient must be non-zero.")
    
    def poly(x):
        return sum([coeff * x**i for i, coeff in enumerate(xs)])
    
    # Using Newton's method to find the zero
    x = 1.0  # Initial guess
    while abs(poly(x)) > 1e-10:
        derivative = sum([i * coeff * x**(i-1) for i, coeff in enumerate(xs)])
        x = x - poly(x) / derivative
    
    return x
