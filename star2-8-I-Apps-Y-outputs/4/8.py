
N = int(input())
a = list(map(int, input().split()))
a.sort()

sum_s = 0
sum_r = sum(a)

min_diff = float("inf")
for i in range(N):
    sum_s += a[i]
    sum_r -= a[i]
    min_diff = min(min_diff, abs(sum_s - sum_r))

print(min_diff)

