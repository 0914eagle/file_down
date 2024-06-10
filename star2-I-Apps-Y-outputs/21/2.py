
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b.sort()

prefix_sum = [0] * (n + 1)
for i in range(n):
    prefix_sum[i + 1] = prefix_sum[i] + a[i] * b[i]

suffix_sum = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    suffix_sum[i] = suffix_sum[i + 1] + a[i] * b[n - 1 - i]

result = float('inf')
for i in range(n + 1):
    result = min(result, prefix_sum[i] + suffix_sum[i])

print(result % 998244353)

