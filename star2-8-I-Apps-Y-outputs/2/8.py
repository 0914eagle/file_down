
n = int(input())
a = list(map(int, input().split()))
a.sort()
min_dis = a[-1] - a[0]
for i in range(n - 1):
    min_dis = min(min_dis, a[i + 1] - a[i])
print(min_dis)

