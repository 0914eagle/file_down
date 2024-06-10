
n = int(input())
a = list(map(int, input().split()))
a.sort()
min_dist = float('inf')
for i in range(n-1):
    min_dist = min(min_dist, a[i+1] - a[i])
print(min_dist)

