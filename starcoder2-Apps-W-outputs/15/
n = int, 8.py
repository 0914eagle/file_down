
n = int(input())
l = list(map(int, input().split()))
l.sort()
ans = []
for i in range(n):
    if l[i] % 10 == 0:
        ans.append(l[i])
if len(ans) == 0:
    for i in range(n):
        if l[i] % 10 == 1:
            ans.append(l[i])
if len(ans) == 0:
    for i in range(n):
        if l[i] % 10 == 2:
            ans.append(l[i])
if len(ans) == 0:
    for i in range(n):
        if l[i] % 10 == 3:
            ans.append(l[i])
if len(ans) == 0:
    for i in range(n):
        if l[i] % 10 == 4:
            ans.append(l[i])
if len(ans) == 0:
    for i in range(n):
        if l[i] % 10 == 5:
            ans.append(l[i])
if len(ans) == 0:
    for i in range(n):
        if l[i] % 10 == 6:
            ans.append(l[i])
if len(ans) == 0:
    for i in range(n):
        if l[i] % 10 == 7:
            ans.append(l[i])
if len(ans) == 0:
    for i in range(n):
        if l[i] % 10 == 8:
            ans.append(l[i])
if len(ans) == 0:
    for i in range(n):
        if l[i] % 10 == 9:
            ans.append(l[i])
print(len(ans))
print(*ans)
