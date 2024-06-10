
n = int(input())
a = list(map(int, input().split()))
from collections import Counter
counter = Counter(a)
prefix_sum = [0] * (n + 1)
for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + counter[a[i - 1]]
ans = 0
for i in range(1, n + 1):
    left = prefix_sum[i]
    right = prefix_sum[n] - prefix_sum[i]
    if left > right:
        ans += 1
print(ans)

