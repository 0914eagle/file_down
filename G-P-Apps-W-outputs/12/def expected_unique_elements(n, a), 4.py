
def expected_unique_elements(n, a):
    prefix_sum = [0] * (n + 1)
    unique_count = [0] * (n + 1)
    
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + (i + 1) - unique_count[a[i]]
        unique_count[a[i]] = i + 1
    
    expected = 0
    for i in range(1, n + 1):
        expected += 2 * (n - i + 1) * prefix_sum[i]
    
    expected /= n * n
    
    return expected

n = int(input())
a = list(map(int, input().split()))

result = expected_unique_elements(n, a)
print('%.6f' % result)
```
