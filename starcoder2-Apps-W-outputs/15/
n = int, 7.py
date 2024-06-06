
n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = []
for i in range(n):
    if a[i] == 0:
        ans.append(a[i])
    if a[i] > 9:
        ans.append(a[i])
print(len(ans))
print(*ans)
