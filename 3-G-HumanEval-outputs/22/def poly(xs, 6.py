
def poly(xs: list, x: float):
    
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    
    def poly(xs: list, x: float):
        return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

    def find_zero_helper(xs: list, start: float, end: float, tol: float = 1e-6):
        if poly(xs, start) == 0:
            return start
        if poly(xs, end) == 0:
            return end
        mid = (start + end) / 2
        if poly(xs, mid) == 0 or abs(end - start) < tol:
            return mid
        if poly(xs, start) * poly(xs, mid) < 0:
            return find_zero_helper(xs, start, mid, tol)
        else:
            return find_zero_helper(xs, mid, end, tol)

    if len(xs) % 2 != 0:
        raise ValueError("Number of coefficients should be even.")
    if all(coeff == 0 for coeff in xs):
        raise ValueError("All coefficients are zero.")
    largest_non_zero_coeff = max([abs(coeff) for coeff in xs if coeff != 0])
    if largest_non_zero_coeff == 0:
        raise ValueError("All coefficients are zero.")
    start = -largest_non_zero_coeff - 1
    end = largest_non_zero_coeff + 1
    return find_zero_helper(xs, start, end)
