
def simplify(x, n):
    x_num, x_den = x.split('/')
    n_num, n_den = n.split('/')
    if int(x_num) * int(n_den) == int(x_den) * int(n_num):
        return True
    return False
