
import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))

prefix_sum = [0] * (n + 1)
for i in range(n):
    prefix_sum[i + 1] = prefix_sum[i] + a[i]

count = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if prefix_sum[j + 1] - prefix_sum[i] == a[i] * a[j]:
            count += 1
print(count)

