
def restore_secret_array(t, test_cases):
    for i in range(t):
        n, x, y = test_cases[i]
        diff = y - x
        arr = [x]
        for j in range(n - 1):
            arr.append(arr[j] + diff)
        print(*arr)

# Input
t = 5
test_cases = [(2, 1, 49), (5, 20, 50), (6, 20, 50), (5, 3, 8), (9, 13, 22)]

# Output
restore_secret_array(t, test_cases)
```
