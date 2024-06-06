
n = int(input())
a = []
for i in range(n):
    a.append(list(input().split()))
    a[i][0] = int(a[i][0])
x = sorted(a, key=lambda x: x[1], reverse=True)
ans = 1
cnt = 0
y = []
for i in range(n):
    if x[i][1] == '0':
        y.append([ans, x[i][0]])
        ans += 1
    else:
        cnt += 1
y = sorted(y, key=lambda x: x[1])
for i in range(len(y)):
    print("move", y[i][1], y[i][0])
for i in range(cnt, ans):
    print("move", i, ans)
    ans += 1
