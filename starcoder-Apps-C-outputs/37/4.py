
n, m = map(int, input().split())
a = []
for _ in range(m):
    a.append(tuple(map(int, input().split())))
a.sort(key=lambda x: x[2])

i = 0
j = 1
ans = ['-' * n]
flag = 0
while i < m and a[i][2] == 1:
    if a[i][0] == -n:
        ans[0][0] = '+'
        flag = 1
        break
    i += 1

while i < m:
    if a[i][0] != a[i - 1][0]:
        j += 1
        ans.append('-' * n)
    if flag == 1:
        break
    if a[i][0] >= a[i - 1][0] + 2:
        for k in range(i - 1, i + 1):
            if a[k][0] == a[k][1]:
                ans[j][a[k][0] - 1] = '+'
            else:
                ans[j][a[k][0] - 1] = '-'
                ans[j][a[k][1] - 1] = '+'
        flag = 1
        break
    if a[i][0] == a[i - 1][0] + 1 and a[i][1] - a[i - 1][1] >= 3:
        if a[i][1] - a[i - 1][1] == 3:
            ans[j][a[i][0] - 1] = '+'
        else:
            ans[j][a[i][0] - 1] = '-'
            ans[j][a[i][1] - 2] = '+'
        flag = 1
        break
    i += 1

if flag == 0:
    print('impossible')
else:
    for i in range(len(ans)):
        print(ans[i])
