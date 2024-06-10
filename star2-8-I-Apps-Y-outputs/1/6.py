
n, k = map(int, input().split())
a = list(map(int, input().split()))
if len(set(a)) < k:
    print('NO')
else:
    print('YES')
    a_set = set(a)
    c = [0] * n
    for i in range(k):
        c[i] = i + 1
    for i in range(k, n):
        c[i] = 1
    print(' '.join(map(str, c)))

