
import math


def poly(xs: list, x: float):
    
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    
    def poly(xs, x):
        return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

    def derivative(xs, x):
        return sum([i * coeff * math.pow(x, i - 1) for i, coeff in enumerate(xs) if i > 0])

    def newton_raphson(xs, x0, tol=1e-6, max_iter=100):
        for _ in range(max_iter):
            x1 = x0 - poly(xs, x0) / derivative(xs, x0)
            if abs(x1 - x0) < tol:
                return x1
            x0 = x1
        return None

    if len(xs) % 2 != 0:
        raise ValueError("Number of coefficients must be even.")

    if max(xs) == 0:
        raise ValueError("Largest non-zero coefficient must be non-zero.")

    return newton_raphson(xs, 0)

