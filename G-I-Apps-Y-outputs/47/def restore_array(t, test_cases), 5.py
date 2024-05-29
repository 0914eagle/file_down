
def restore_array(t, test_cases):
    for n, x, y in test_cases:
        diff = y - x
        max_element = min(y + diff*(n-2), x + diff*(n-2))
        array = [max_element - diff*i for i in range(n)]
        print(*array)

# Example Usage
t = 5
test_cases = [(2, 1, 49), (5, 20, 50), (6, 20, 50), (5, 3, 8), (9, 13, 22)]
restore_array(t, test_cases)
```
