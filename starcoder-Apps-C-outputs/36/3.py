
n, m = [int(i) for i in input().split()]

l = [int(i) for i in input().split()]

lst = [[] for i in range(n + 1)]

for i in range(m):
    s = [int(i) for i in input().split()]
    s = s[1:]
    lst[s[0]] = lst[s[0]] + s[1:]

for i in range(1, n + 1):
    if len(lst[i]) == 1:
        if l[i - 1] == 1:
            l[lst[i][0] - 1] = (l[lst[i][0] - 1] + 1) % 2
        else:
            l[lst[i][0] - 1] = (l[lst[i][0] - 1] - 1) % 2

if 0 in l:
    print('NO')
else:
    print('YES')
