
def restore_array(t, test_cases):
    for test_case in test_cases:
        n, x, y = test_case
        diff = y - x
        min_elem = min(x, y)
        remaining = n - 2
        interval = diff
        array = [min_elem]

        for i in range(1, n):
            value = min_elem + i * interval
            if remaining == 0:
                array.append(max(x,y) - i*interval)
            else:
                array.append(value)
                remaining -= 1

        print(*array)

# Input parsing
t = int(input())
test_cases = []
for _ in range(t):
    n, x, y = map(int, input().split())
    test_cases.append((n, x, y))

# Function call
restore_array(t, test_cases)
```
