
from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
left_counts = {}
right_counts = {}
for i in range(n):
    left_counts[arr[i]] = left_counts.get(arr[i], 0) + 1
    right_counts[arr[n - i - 1]] = right_counts.get(arr[n - i - 1], 0) + 1
ans = 0
for i in range(n):
    right_counts[arr[n - i - 1]] -= 1
    if left_counts[arr[i]] > right_counts[arr[i]]:
        ans += 1
print(ans)

