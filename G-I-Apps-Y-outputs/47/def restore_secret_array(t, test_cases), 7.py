
def restore_secret_array(t, test_cases):
    for i in range(t):
        n, x, y = test_cases[i]
        diff = y - x
        result = [y]
        for j in range(1, n):
            next_num = y + j*diff
            result.append(next_num)
        print(*result)

# Input
t = 5
test_cases = [
    (2, 1, 49),
    (5, 20, 50),
    (6, 20, 50),
    (5, 3, 8),
    (9, 13, 22)
]

# Call the function
restore_secret_array(t, test_cases)
```
