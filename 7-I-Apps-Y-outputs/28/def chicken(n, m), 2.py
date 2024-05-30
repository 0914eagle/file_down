
def chicken(n, m):
    if n % m == 0:
        print("Dr. Chaz will have {} piece[s] of chicken left over!".format(n - m))
    else:
        print("Dr. Chaz needs {} more piece[s] of chicken!".format(m - n % m))

n, m = map(int, input().split())
chicken(n, m)

