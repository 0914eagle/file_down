
def chicken_problem(n, m):
    if n == m:
        return "Dr. Chaz will have 0 piece of chicken left over!"
    elif n > m:
        return "Dr. Chaz will have {} piece of chicken left over!".format(n - m)
    else:
        return "Dr. Chaz needs {} more piece of chicken!".format(m - n)

n, m = map(int, input().split())
print(chicken_problem(n, m))

