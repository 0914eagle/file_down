
 def simplify(x, n):
    
    x_num, x_den = x.split('/')
    n_num, n_den = n.split('/')
    x_num = int(x_num)
    x_den = int(x_den)
    n_num = int(n_num)
    n_den = int(n_den)
    if x_den == 0 or n_den == 0:
        return False
    if x_den == n_den:
        return True
    if x_den % n_den == 0:
        return True
    if n_den % x_den == 0:
        return True
    if x_den > n_den:
        if x_den % n_den == 0:
            return True
    if n_den > x_den:
        if n_den % x_den == 0:
            return True
    return False
 