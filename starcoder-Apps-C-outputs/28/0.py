
n, k = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(n):
    if 1 in a[i]:
        for j in range(k):
            if a[i][j] == 1:
                a[i][j] = 0
            else:
                a[i][j] = 1

for i in range(n):
    if sum(a[i]) > k // 2:
        print("NO")
        exit(0)
print("YES")
