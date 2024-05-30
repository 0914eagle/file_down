
def chicken_problem(n, m):
    if n == m:
        return "Dr. Chaz will have {} piece[s] of chicken left over!".format(0)
    elif n > m:
        return "Dr. Chaz will have {} piece[s] of chicken left over!".format(n - m)
    else:
        return "Dr. Chaz needs {} more piece[s] of chicken!".format(m - n)

