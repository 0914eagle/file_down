
def chicken(n, m):
    if n%m == 0:
        return "Dr. Chaz will have {} piece[s] of chicken left over!".format(n-m)
    else:
        return "Dr. Chaz needs {} more piece[s] of chicken!".format(m-n%m)

