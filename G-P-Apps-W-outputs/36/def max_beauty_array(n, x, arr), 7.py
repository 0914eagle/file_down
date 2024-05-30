
def max_beauty_array(n, x, arr):
    prefix_sum = [0]
    for num in arr:
        prefix_sum.append(prefix_sum[-1] + num)

    max_beauty = 0
    for i in range(n + 1):
        for j in range(i, n + 1):
            beauty = prefix_sum[j] - prefix_sum[i] + (x * (j - i))
            max_beauty = max(max_beauty, beauty)

    return max_beauty

# Input
n, x = map(int, input().split())
arr = list(map(int, input().split()))

# Output
print(max_beauty_array(n, x, arr))
```
