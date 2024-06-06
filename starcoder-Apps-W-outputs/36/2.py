
n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
m = int(input())
arr2 = [list(map(int, input().split())) for i in range(m)]

flag = 1
for i in range(n):
    for j in range(m):
        if arr[i][0] * arr2[j][0] + arr[i][1] * arr2[j][1] == 0:
            flag = 0
            break
if flag:
    print("YES")
else:
    print("NO")
