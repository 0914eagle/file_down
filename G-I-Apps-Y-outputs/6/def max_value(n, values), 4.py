
def max_value(n, values):
    prefix_sum_sq = [0] * (n+1)
    suffix_sum = [0] * (n+1)

    for i in range(1, n+1):
        prefix_sum_sq[i] = prefix_sum_sq[i - 1] + values[i - 1] * values[i - 1]

    for i in range(n-1, -1, -1):
        suffix_sum[i] = suffix_sum[i + 1] + values[i]

    max_val = 0
    for k in range(n):
        max_val = max(max_val, prefix_sum_sq[k] * suffix_sum[k + 1])

    return max_val


if __name__ == "__main__":
    n = int(input())
    values = [int(input()) for _ in range(n)]
    
    result = max_value(n, values)
    print(result)
```
