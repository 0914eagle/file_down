
n = int(input())
a = list(map(int, input().split()))
a.sort()
m = sum(a) / n
left, right = 0, 0
for i in range(n):
    left += abs(a[i] - m)
    right += abs(a[i] - m - 1)
print(min(left, right))

