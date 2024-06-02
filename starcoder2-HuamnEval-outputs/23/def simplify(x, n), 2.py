
def simplify(x, n):
    x = x.split('/')
    n = n.split('/')
    return (int(x[0]) * int(n[0])) % (int(x[1]) * int(n[1])) == 0
