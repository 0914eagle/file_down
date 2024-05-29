
def max_absolute_diff(t, test_cases):
    ans = []
    for i in range(t):
        n, m = test_cases[i]
        if n == 1:
            ans.append(0)
        elif n == 2:
            ans.append(2)
        else:
            ans.append(2 * m)
    return ans

# Test the function with the given example
t = 5
test_cases = [(1, 100), (2, 2), (5, 5), (2, 1000000000), (1000000000, 1000000000)]
output = max_absolute_diff(t, test_cases)
for val in output:
    print(val)
```
