
def restore_secret_array(t, test_cases):
    for test_case in test_cases:
        n, x, y = test_case
        diff = y - x
        
        # Find the smallest common difference
        smallest_diff = float('inf')
        for i in range(1, diff):
            if diff % i == 0 and i < diff:
                smallest_diff = i
                
        arr = [x]
        value = x
        for _ in range(n-1):
            value += smallest_diff
            arr.append(value)
        
        print(*arr)

# Input
t = 5
test_cases = [
    (2, 1, 49),
    (5, 20, 50),
    (6, 20, 50),
    (5, 3, 8),
    (9, 13, 22)
]

# Solve the problem
restore_secret_array(t, test_cases)
```
