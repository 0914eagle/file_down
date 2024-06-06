
n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(n):
    for j in range(i+1, n):
        if a[i][0] == a[j][0] and a[i][1] == a[j][1] and a[i][2] == a[j][2] and a[i][3] == a[j][3]:
            print("YES")
            exit()
print("NO")
