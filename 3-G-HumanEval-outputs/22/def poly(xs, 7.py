
def poly(xs: list, x: float):
    
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    
    def poly(xs: list, x: float):
        return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

    def f(x):
        return poly(xs, x)

    def find_initial_guess():
        largest_non_zero_coeff = max([abs(coeff) for coeff in xs])
        return 1 / largest_non_zero_coeff

    def find_zero_point():
        x = find_initial_guess()
        while abs(f(x)) > 1e-10:
            x = x - f(x) / poly([i * coeff for i, coeff in enumerate(xs)][1:], x)
        return x

    return find_zero_point()
