
import math

def poly(xs: list, x: float):
    
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    
    if len(xs) % 2 != 0:
        raise ValueError("The number of coefficients must be even.")
    
    largest_non_zero_coeff = max([abs(coeff) for coeff in xs[1:]])
    if largest_non_zero_coeff == 0:
        raise ValueError("No non-zero coefficients found.")
    
    for i in range(-1000, 1000):  # Iterate over a range to find a zero point
        if poly(xs, i) == 0:
            return i

