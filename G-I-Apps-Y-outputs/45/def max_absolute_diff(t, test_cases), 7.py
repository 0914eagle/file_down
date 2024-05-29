
def max_absolute_diff(t, test_cases):
    for n, m in test_cases:
        if n == 1:
            print(0)
        elif n == 2:
            print(2)
        else:
            if m >= n:
                print(2 * m)
            else:
                result = 2 * m - 2 * n
                print(result)

# Example test cases
test_cases = [(1, 100), (2, 2), (5, 5), (2, 1000000000), (1000000000, 1000000000)]
max_absolute_diff(5, test_cases)
```
