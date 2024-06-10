
n = int(input())
arr = list(map(int, input().split()))

prefix_sum = [0]
for i in range(n):
    prefix_sum.append(prefix_sum[-1] + arr[i])

count = 0
for i in range(1, n+1):
    for j in range(i+1, n+1):
        if prefix_sum[j] - prefix_sum[i-1] == arr[i-1] * (j - i + 1):
            count += 1

print(count)

