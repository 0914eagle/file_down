
def restore_secret_array(t, test_cases):
    for i in range(t):
        n, x, y = test_cases[i]
        diff = y - x
        min_element = min(x, y)
        result = [min_element]
        for j in range(n-1):
            next_element = min_element + diff
            result.append(next_element)
            min_element = next_element
        print(*result)

# Test the function with the provided example
t = 5
test_cases = [(2, 1, 49), (5, 20, 50), (6, 20, 50), (5, 3, 8), (9, 13, 22)]
restore_secret_array(t, test_cases)
```
