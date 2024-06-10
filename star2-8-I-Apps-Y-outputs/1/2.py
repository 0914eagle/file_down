
n, k = map(int, input().split())
a = list(map(int, input().split()))
a = set(a)
if len(a) < k:
    print('NO')
else:
    print('YES')
    c = [i % k + 1 for i in range(n)]
    print(' '.join(map(str, c)))

