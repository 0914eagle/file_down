
def max_value_of_expression(n, values):
    prefix_sums = [0] * (n + 1)
    prefix_sums[1] = values[0] ** 2
    for i in range(2, n + 1):
        prefix_sums[i] = prefix_sums[i - 1] + values[i - 1] ** 2

    max_value = float("-inf")
    for k in range(1, n):
        sum_of_squares = prefix_sums[k]
        sum_ = sum(values[k:])
        max_value = max(max_value, sum_of_squares * sum_)

    return max_value

if __name__ == "__main__":
    n = int(input())
    values = [int(input()) for _ in range(n)]
    result = max_value_of_expression(n, values)
    print(result)
```
