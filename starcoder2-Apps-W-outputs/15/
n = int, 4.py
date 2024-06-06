
n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = []
for i in range(n):
    if a[i] == 0:
        ans.append(0)
        break
for i in range(n):
    if a[i] != 0 and a[i] % 10 == 0:
        ans.append(a[i])
        break
print(len(ans))
print(*ans)
