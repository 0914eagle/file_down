
n = int(input())
l = list(map(int, input().split()))
ans = []
for i in range(n):
    for j in range(i + 1, n):
        if l[i] <= l[j]:
            continue
        else:
            ans.append((i + 1, j + 1))
            l[j] = l[j] + (l[i] - l[j])
print(len(ans))
for x, y in ans:
    print(x, y)
