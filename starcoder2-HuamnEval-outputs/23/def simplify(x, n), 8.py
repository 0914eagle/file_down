
def simplify(x, n):
    x_num, x_den = x.split('/')
    n_num, n_den = n.split('/')
    return x_num == n_num and x_den == n_den
