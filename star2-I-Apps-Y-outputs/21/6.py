
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

res = 0
for i in range(n):
    res += a[i] * b[i]

print(res % 998244353)
