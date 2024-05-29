
def restore_array(t, test_cases):
    for n, x, y in test_cases:
        diff = y - x
        positions = [i for i in range(1, n)]
        for i in range(1, n):
            if diff % i == 0 and diff // i < n and (diff // i != i or diff // i == 1):
                positions[0] = x
                for j in range(1, n):
                    positions[j] = positions[j-1] + diff // i
                break
        print(*positions)

t = 5
test_cases = [(2, 1, 49), (5, 20, 50), (6, 20, 50), (5, 3, 8), (9, 13, 22)]
restore_array(t, test_cases)
```
