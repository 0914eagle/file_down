
n = int(input())
a = list(map(int, input().split()))
a.sort()

snuke_sum = 0
raccoon_sum = sum(a)
min_diff = float('inf')
for i in range(n - 1):
    snuke_sum += a[i]
    raccoon_sum -= a[i]
    min_diff = min(min_diff, abs(snuke_sum - raccoon_sum))
print(min_diff)

