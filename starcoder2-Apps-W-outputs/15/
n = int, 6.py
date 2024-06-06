
n = int(input())
l = list(map(int, input().split()))
l.sort()
ans = []
for i in range(n):
    if l[i] == 0:
        ans.append(l[i])
    elif l[i] % 10 == 0:
        ans.append(l[i])
if len(ans) == 0:
    print(1)
    print(l[0])
else:
    print(len(ans))
    print(*ans)
