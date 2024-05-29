
def max_absolute_diff(t, test_cases):
    for n, m in test_cases:
        if n == 1:
            print(0)
        elif n == 2:
            print(m)
        else:
            print(2 * m)

# Input
t = 5
test_cases = [(1, 100), (2, 2), (5, 5), (2, 1000000000), (1000000000, 1000000000)]

# Call the function
max_absolute_diff(t, test_cases)
```
