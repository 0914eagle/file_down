
def calc(a, m):
    a.sort()
    res = 1
    for i in range(len(a) - 1):
        res *= abs(a[i] - a[i + 1])
        res %= m
    return res
n, m = map(int, input().split())
a = list(map(int, input().split()))
print(calc(a, m))

