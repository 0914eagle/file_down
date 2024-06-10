
n = int(input())
a = list(map(int, input().split()))

a.sort()

min_diff = 10000
left_sum = 0
right_sum = sum(a)

for i in range(n):
    left_sum += a[i]
    right_sum -= a[i]
    min_diff = min(min_diff, abs(left_sum - right_sum))

print(min_diff)

