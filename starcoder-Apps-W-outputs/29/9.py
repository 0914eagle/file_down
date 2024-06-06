
def solution():
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    r = []
    for i in range(n):
        r.append([])
        for j in range(a[i]):
            if (j % 2 == 0):
                r[i].append(j // 2 % k + 1)
            else:
                r[i].append(k - j // 2 % k)
    if (r[0][0] == r[1][0] and r[1][0] == r[2][0]):
        r[0][0] = r[0][0] + 1 if r[0][0] == r[1][0] else r[0][0]
    for i in range(n):
        for j in range(a[i] - 1):
            if (r[i][j] == r[i][j + 1]):
                r[i][j] = r[i][j] + 1 if r[i][j] == r[i][j + 1] else r[i][j]
    for i in range(n - 1):
        for j in range(a[i]):
            if (r[i][j] == r[i + 1][0]):
                r[i][j] = r[i][j] + 1 if r[i][j] == r[i + 1][0] else r[i][j]
    print('YES')
    for i in range(n):
        print(' '.join(map(str, r[i])))


solution()
