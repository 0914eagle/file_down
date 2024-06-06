
n = int(input())
m = 2 ** n
ls = []
for i in range(m):
    ls.append(int(input()))
if ls[0] != 0:
    print('impossible')
else:
    ls.sort()
    s = set()
    a = [0] * n
    for i in range(m):
        if ls[i] == 0:
            continue
        for j in range(n):
            if (ls[i] - a[j]) in s:
                a[j] = ls[i]
                s.add(ls[i])
                break
    if a[n - 1] == 0:
        print('impossible')
    else:
        for i in range(n):
            print(a[i])
