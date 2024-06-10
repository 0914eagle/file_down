
n, p, k = map(int, input().split())
t = list(map(int, input().split()))

sum = 0
for i in range(n):
    sum += (t[i] - sum) * (100 + i * p) / 100
sum += (k - sum) * (100 + n * p) / 100

print(sum)

