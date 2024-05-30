
def chicken(n, m):
    if n == m:
        print("Dr. Chaz will have {} piece[s] of chicken left over!".format(0))
    elif n > m:
        print("Dr. Chaz will have {} piece[s] of chicken left over!".format(n - m))
    else:
        print("Dr. Chaz needs {} more piece[s] of chicken!".format(m - n))

n, m = map(int, input().split())
chicken(n, m)

