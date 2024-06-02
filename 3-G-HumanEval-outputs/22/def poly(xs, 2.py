
def poly(xs: list, x: float):
    
    return sum([coeff * x**i for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    
    if len(xs) % 2 != 0:
        raise ValueError("The number of coefficients must be even.")
    if xs[-1] == 0:
        raise ValueError("The largest non-zero coefficient must be non-zero.")

    def poly(x):
        return sum([coeff * x**i for i, coeff in enumerate(xs)])

    # Using Newton's method for finding zero
    x0 = 1.0  # Initial guess
    while abs(poly(x0)) > 1e-6:
        x0 = x0 - poly(x0) / poly(1)

    return x0
