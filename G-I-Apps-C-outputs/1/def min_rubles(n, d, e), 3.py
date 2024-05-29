
def min_rubles(n, d, e):
    min_rubles = n
    for i in range(n // d + 1):
        rubles_left = n - i * d
        euros = rubles_left // e
        rubles_left -= euros * e
        min_rubles = min(min_rubles, rubles_left)
    return min_rubles

n = int(input().strip())
d = int(input().strip())
e = int(input().strip())
print(min_rubles(n, d, e))
