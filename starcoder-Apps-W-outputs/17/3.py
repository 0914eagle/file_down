
n = int(input())
a = list(map(int, input().split()))
ans = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        if a[i] > 0 and a[j] > 0:
            a[i] -= 1
            a[j] -= 1
            ans[i][j] = ans[j][i] = 1

if sum(a) == 0:
    print("YES", 2)
    print(sum(map(sum, ans)))
    for i in range(n):
        for j in range(i + 1, n):
            if ans[i][j] == 1:
                print(i + 1, j + 1)
else:
    print("NO")
