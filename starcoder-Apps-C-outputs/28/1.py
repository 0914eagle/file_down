
n, k = map(int, input().split())
li = []
for i in range(n):
    li.append(list(map(int, input().split())))
flag = True
for j in range(k):
    if sum([li[i][j] for i in range(n)]) == n:
        flag = False
if flag:
    print("YES")
else:
    print("NO")
