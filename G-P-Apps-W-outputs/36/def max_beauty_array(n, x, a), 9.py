
def max_beauty_array(n, x, a):
    max_sum = current_sum = 0
    prefix_max = [0] * (n + 1)
    suffix_max = [0] * (n + 1)

    for i in range(n):
        current_sum = max(0, current_sum + a[i])
        max_sum = max(max_sum, current_sum)
        prefix_max[i + 1] = max_sum

    max_sum = current_sum = 0

    for i in range(n - 1, -1, -1):
        current_sum = max(0, current_sum + a[i])
        max_sum = max(max_sum, current_sum)
        suffix_max[i] = max_sum

    ans = 0
    for i in range(n):
        ans = max(ans, max(prefix_max[i], 0) + max(suffix_max[i + 1], 0))
    
    for i in range(n):
        for j in range(i, n):
            ans = max(ans, prefix_max[i] + suffix_max[j + 1] + x * sum(a[i:j + 1]))

    return ans

# Input parsing
n, x = map(int, input().split())
a = list(map(int, input().split()))

result = max_beauty_array(n, x, a)
print(result)
```
