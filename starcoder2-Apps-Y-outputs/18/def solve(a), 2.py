
def solve(a):
    n = len(a)
    res = [0] * n
    i = 0
    while i < n and a[i] < a[i + 1]:
        i += 1
    while i < n and a[i] > a[i + 1]:
        res[i] = 1
        i += 1
    while i < n and a[i] < a[i + 1]:
        res[i] = 1
        i += 1
    while i < n and a[i] > a[i + 1]:
        i += 1
    if i < n:
        return 'NO'
    return 'YES\n' + ' '.join(map(str, res))

n = int(input())
a = list(map(int, input().split()))
print(solve(a))

