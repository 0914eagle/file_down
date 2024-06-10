

def ncr(n, r):
    if n < r:
        return 0
    if n == r:
        return 1
    return ncr(n - 1, r - 1) + ncr(n - 1, r)


def count(n, m, a, b):
    if a == b:
        return 0
    count = 0
    for i in range(n):
        if a[i] == 0 and b[i] == 0:
            count += m
    return count


def solve(n, m, a, b):
    if a == b:
        return 0
    count = 0
    for i in range(n):
        if a[i] == 0 and b[i] == 0:
            count += m
        elif a[i] == 0 and b[i] != 0:
            count += b[i] - 1
        elif a[i] != 0 and b[i] == 0:
            count += m - a[i]
        elif a[i] < b[i]:
            count += b[i] - a[i]
    return count


n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
count = solve(n, m, a, b)
total = m ** n
if count == 0:
    print(0)
else:
    res = ncr(total, count)
    mod = 10 ** 9 + 7
    res = res // count
    print(res % mod)


