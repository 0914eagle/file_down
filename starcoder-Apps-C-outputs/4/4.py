
N = int(input())
a = []
for i in range(2*N):
    a.append(list(input().split()))

l = [1, 1, 1]
for i in range(2 * N):
    if a[i][0] == "W":
        if int(a[i][1]) == l[0]:
            l[0] += 1
        elif int(a[i][1]) == l[1]:
            l[1] += 1
        elif int(a[i][1]) == l[2]:
            l[2] += 1
        else:
            l.append(int(a[i][1]))
ans = 0
l.sort()
for i in range(N):
    if l[i] == i + 1:
        pass
    else:
        ans += 1

l = [1, 1, 1]
for i in range(2 * N):
    if a[i][0] == "B":
        if int(a[i][1]) == l[0]:
            l[0] += 1
        elif int(a[i][1]) == l[1]:
            l[1] += 1
        elif int(a[i][1]) == l[2]:
            l[2] += 1
        else:
            l.append(int(a[i][1]))
l.sort()
for i in range(N):
    if l[i] == i + 1:
        pass
    else:
        ans += 1

print(ans)
