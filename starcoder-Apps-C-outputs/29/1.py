
n = int(input())
points = []
for i in range(n):
    points.append(list(map(int, input().split())))
s = 0
for i in range(n):
    s += points[i][0]*points[(i+1)%n][1]
    s -= points[(i+1)%n][0]*points[i][1]
s = abs(s)
ans = s/2
print(ans)
