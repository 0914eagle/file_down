
k = int(input())
l = list(map(int, input().split()))
l.sort()
ans = []
for i in range(k):
    if l[i] == 0:
        ans.append(l[i])
for i in range(k):
    if l[i] % 10 == 0:
        ans.append(l[i])
print(len(ans))
print(*ans)
