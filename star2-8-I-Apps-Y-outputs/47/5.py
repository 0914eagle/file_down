
n, p, k = map(int, input().split())
t = list(map(int, input().split()))
sum_time = 0
for i in range(n):
    speed = 1 + (i * p) / 100
    sum_time += (t[i] - sum_time) / speed
sum_time += (k - sum_time) / (1 + n * p / 100)
print(sum_time)

