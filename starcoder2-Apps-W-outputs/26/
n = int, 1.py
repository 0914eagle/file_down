
n = int(input())
p = list(map(int, input().split()))

ans = []
for i in range(n-1):
    if p[i] == i+1:
        continue
    for j in range(i+1, n):
        if p[j] == i+1:
            ans.append(j+1)
            p[j], p[i] = p[i], p[j]
            break
print(len(ans))
for i in ans:
    print(i)
