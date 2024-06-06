
n, h, m, k = list(map(int, input().split()))
T = []
for i in range(n):
    T.append(list(map(int, input().split())))
for t in range(0, m//2):
    cancel = 0
    for i in range(n):
        if T[i][0] == 0 and T[i][1] >= t and T[i][1] < t + k:
            cancel = 1
            break
        if T[i][0] == h-1 and T[i][1] + m - t >= m - k and T[i][1] + m - t < m:
            cancel = 1
            break
        for j in range(i+1, n):
            if T[i][0] == T[j][0] and abs(T[i][1] - T[j][1]) < m - k:
                cancel = 1
                break
        if cancel == 1:
            break
    if cancel == 0:
        print(0, t)
        exit(0)

print(1, 0)
